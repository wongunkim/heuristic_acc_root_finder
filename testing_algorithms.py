import pandas as pd
from math import ceil, floor, log, log2
from generate_roots import generate_roots_with_isolation
from polynomial_init import initPolyByRoots
from algorithm1 import *
from analysis import *

pd.set_option('display.max_rows', None)


#### SETTINGS for the paper ####

RT_LOWER_BOUND = 1e-14
RT_UPPER_BOUND = 1e14

DEFAULT_Q=32

unit_c = 0
unit_r = 1
d_vals = [6400, 12800, 25600]
sigma_vals = [1.4]

num_tests = 100

def q_fcn(d, sigma):
    return int(log(d, sigma)) + 1

def u_fcn(d, sigma):
    return ceil(log2(q_fcn(d, sigma)))


# TESTING CODE FOR ALG 1

results_list = []

for deg in d_vals:

    m_vals = [0, 1, 2, 3, 4, 5, 10, 20, 50, 100, deg // 16, deg // 8, deg // 4, deg // 2, 3 * deg // 4, deg - 1, deg]


    for sigma in sigma_vals:
        isolation = 1.00001
        # isolation = sigma

        print(
            f"Testing degree d={deg} with sigma={sigma}, isolation(theta)={isolation}: fl(log_sigma(d)) = {DEFAULT_Q if sigma == 1 else q_fcn(deg, sigma)}"
        )

        if sigma == 1:
            u = floor(log2(DEFAULT_Q))
            max_q = DEFAULT_Q
        else:
            u = u_fcn(deg, sigma)
            max_q = q_fcn(deg, sigma)

        print(f"max_q={max_q}, u={u}...")
        # for h in h_vals:
        print(f"Results for sigma-soft EI test: d={deg}, r_1 upper bound={RT_UPPER_BOUND:e}")
        res_excl = {m: 0 for m in m_vals}
        max_numNIRevals = {m: 0 for m in m_vals}  # max per m across num_tests
        numNIRevals_all = {m: [] for m in m_vals}  # retain all trial counts per m

        for m in m_vals:
            for trial in range(num_tests):
                int_rts, ext_rts = generate_roots_with_isolation(deg, m, c=unit_c, r=unit_r, isolation=isolation)
                p = initPolyByRoots(internal_rts=int_rts, external_rts=ext_rts)  # ------ Black-Box Polynomial

                try:
                    res, max_h, num_NIR_evals = sigma_soft_ei_test_I(p, sigma=sigma, u_plus=u, max_q=max_q, log_level=0)
                    # print(m, res, max_h, num_NIR_evals ) # ------- 6/27/2026 for checking
                except NIRNumericalAlarm as e:
                    print(f"[ALARM] {e}")
                    continue
                # Append record to list
                results_list.append(
                    {
                        "test_type": "I",
                        "d": deg,
                        "m": m,
                        "sigma": sigma,
                        "isolation": isolation,
                        "result": res,
                        "h": max_h,
                        "num_NIR_evals": num_NIR_evals,
                    }
                )
                if res == 0:
                    res_excl[m] += 1
        print("Exclusion counts by m:")
        for m in m_vals:
            print(f"m={m}: {res_excl[m]} out of {num_tests}")

# Create the DataFrame
results_df = pd.DataFrame(results_list)

print(analyze_results(results_df))
