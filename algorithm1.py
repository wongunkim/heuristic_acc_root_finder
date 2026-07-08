import numpy as np
from NIR import NIRNumericalAlarm,compute_NIR
from roots_unity import roots_of_unity
from power_sums import compute_s_hq_from_dict


def sigma_soft_ei_test_I(p_poly, sigma, u_plus, max_q=None, log_level=0):
    d = p_poly.getDegree()

    max_q = 2 ** u_plus
    NIR_vals = {0: compute_NIR(p_poly, roots_of_unity(max_q, 0))}
    num_NIR_evals = 1

    for u in range(1, u_plus + 1):
        q = 2 ** u
        for g in range(1, q, 2):
            idx = g * max_q // q
            NIR_vals[idx] = compute_NIR(p_poly, roots_of_unity(max_q, idx))
        num_NIR_evals += q // 2

        if log_level > 0:
            print(f"Testing u={u}, q={q}...")

        for h in range(q):
            s_hq = compute_s_hq_from_dict(p_poly, h, q, max_q, NIR_vals)
            s_neg_hq = compute_s_hq_from_dict(p_poly, -h, q, max_q, NIR_vals)
            cond1 = np.abs(s_hq) / d > np.power(sigma, h) / (np.power(sigma, q) - 1.0)
            cond2 = np.abs(s_neg_hq) / d > np.power(sigma, -h) + np.power(sigma, -h) / (
                        np.power(sigma, q) - 1.0)
            if cond1 or cond2:
                if log_level > 0:
                    print(f"Inclusion certified at h={h}, q={q}")
                return 1, h, num_NIR_evals
    if log_level > 0:
        print("Exclusion certified")
    return 0, h, num_NIR_evals
