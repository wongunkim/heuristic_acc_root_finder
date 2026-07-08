class NIRNumericalAlarm(RuntimeError):
    pass

def compute_NIR(p_poly, x, rev=False):
    roots = p_poly.getRoots()

    if roots is not None:

        nir=0.0
        if not rev:
            for r in roots:
                den = x - r
                if den == 0.0: raise ValueError("Pole collision: evaluation point matches root exactly.")
                nir += 1.0 / den
        else:
            for r in roots:
                den = r * x - 1.0
                if den == 0.0: raise ValueError("Reverse pole collision.")
                nir += r / den
        return nir

    p_val, dp_val = p_poly.eval2(x, rev=rev)
    if p_val == 0: raise ValueError("Cannot compute NIR at a root.")
    return dp_val / p_val

