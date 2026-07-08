
from NIR import *
from roots_unity import *

def compute_s_hq(p_poly, h=0, q=1, NIR_vals=None, rev=False):
    if NIR_vals is None or len(NIR_vals) != q:
        NIR_vals = [compute_NIR(p_poly, roots_of_unity(q, g), rev=rev) for g in range(q)]
    tmp_sum = np.sum([roots_of_unity(q, g * (h + 1)) * NIR_vals[g] for g in range(q)])
    return tmp_sum / q



def compute_s_hq_from_dict(p_poly, h, q, denom_q, NIR_vals_dict):
    eff_q = denom_q // q
    tmp_sum = np.sum([roots_of_unity(q, (g // eff_q) * (h + 1)) * NIR_vals_dict[g]
                 for g in range(denom_q) if g % eff_q == 0])
    return tmp_sum / q