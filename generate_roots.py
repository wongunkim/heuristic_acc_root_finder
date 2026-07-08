import numpy as np

RT_LOWER_BOUND = 1e-14
RT_UPPER_BOUND = 1e14

def generate_roots_with_isolation(d, m, c=0, r=1, isolation=1, return_r_d=False):

    internal_rts, external_rts = [], []
    r_d = None
    if m > 0:
        angs = list(np.random.uniform(0, 2 * np.pi, m))
        radii = list(np.random.uniform(RT_LOWER_BOUND, r / isolation, m))
        internal_rts = [c + radii[i] * np.exp(1j * angs[i]) for i in range(m)]
        if return_r_d:
            r_d = min(radii)
    if m < d:
        angs = list(np.random.uniform(0, 2 * np.pi, d - m))
        radii = list(np.random.uniform(r * isolation, RT_UPPER_BOUND, d - m))
        external_rts = [c + radii[i] * np.exp(1j * angs[i]) for i in range(d - m)]
        if return_r_d and r_d is None:
            r_d = min(radii)
    if return_r_d:
        return internal_rts, external_rts, r_d

    return internal_rts, external_rts