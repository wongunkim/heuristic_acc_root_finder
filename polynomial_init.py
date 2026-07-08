from polynomial import *

def initPolyByCoeffs(coeffs):
    p = [c for c in coeffs]
    d = len(p) - 1

    if d == 0:
        dp_mp = [0.0]
    else:
        dp = []
        for i in range(d):
            power = d - i
            dp.append(p[i] * power)

    return Polynomial(_p=p, _dp=dp, _d=d)


def initPolyByRoots(roots=None, internal_rts=None, external_rts=None, leading_coeff=1.0):
    if roots is not None:
        roots = [r for r in roots]
        d = len(roots)
        return Polynomial(None, None, d, _roots=roots, _leading_coeff=leading_coeff)

    int_roots = [r for r in internal_rts] if internal_rts is not None else None
    ext_roots = [r for r in external_rts] if external_rts is not None else None

    d = 0
    if int_roots is not None: d += len(int_roots)
    if ext_roots is not None: d += len(ext_roots)

    return Polynomial(
        None,
        None,
         d,
        _roots=None,
        _int_roots=int_roots,
        _ext_roots=ext_roots,
        _leading_coeff=leading_coeff
    )