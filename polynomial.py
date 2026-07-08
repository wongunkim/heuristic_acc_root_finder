import numpy as np

DIVIDED_DIFF_EPS = 1e-10

class Polynomial(object):
    def __init__(self, _p, _dp, _d, _roots=None, _int_roots=None, _ext_roots=None, _leading_coeff=None):
        self.p = _p  # coefficients in decreasing order of powers, dense representation. This is opposite of numpy
        self.dp = _dp
        self.degree = _d
        self.internal_roots = _int_roots
        self.external_roots = _ext_roots

        if _int_roots is not None or _ext_roots is not None:
            if _int_roots is None: self.internal_roots = []
            if _ext_roots is None: self.external_roots = []
            self.roots = list(self.internal_roots) + list(self.external_roots)
        else:
            self.roots = _roots

        if self.roots is not None:
            self.leading_coeff = _leading_coeff
        else:
            self.leading_coeff = self.p[0]

    def getDegree(self):
        return self.degree

    def getRoots(self):
        return self.roots

    def getInternalRoots(self):
        return self.internal_roots

    def getExternalRoots(self):
        return self.external_roots

    def getLeadingCoeff(self):
        return self.leading_coeff

    def eval(self, x, rev=False):
        #x_mp = mp.mpc(x)

        if self.roots is None:
            if rev:
                return np.polyval(self.p[::-1], x)
                # return mp.polyval(self.p, 1.0/x)*mp.power(x, self.degree)
            return np.polyval(self.p, x)

        acc = self.leading_coeff
        for r in self.roots:
            term = (1.0 - r * x) if rev else (x - r)
            acc *= term
        return acc

    def eval2(self, x, rev=False, divided_diff=False):
        #x_mp = mp.mpc(x)
        p_val = self.eval(x, rev=rev)

        if divided_diff:
            h = DIVIDED_DIFF_EPS
            p_fwd = self.eval(x + h, rev=rev)
            dp_val = (p_fwd - p_val) / h
            return p_val, dp_val

        if self.roots is None:
            if rev:
                x_inv = 1.0 / x
                dp_inv = np.polyval(self.dp, x_inv)
                dp_val = self.degree * np.power(x, self.degree - 1) * p_val - np.power(x,
                                                                                          self.degree - 2) * dp_inv
            else:
                dp_val = np.polyval(self.dp, x)
            return p_val, dp_val

        # dp_val = mp.mpc(0.0)
        # for i in range(self.degree):
        #     term_acc = mp.mpc(1.0, 0.0)
        #     for j, rt in enumerate(self.roots):
        #         if j != i:
        #             term = (x_mp - 1.0/rt) if rev else (x_mp-rt)
        #         else:
        #             term = mp.mpc(1.0, 0.0)
        #         term_acc *= term
        #     dp_val += term_acc
        # dp_val *= self.leading_coeff

        sum_terms = 0.0
        zero_term_idx = -1

        for i, rt in enumerate(self.roots):
            term = (1.0 - rt * x) if rev else (x - rt)
            if term == 0.0:
                zero_term_idx = i
                break

        if zero_term_idx != -1:
            dp_val = 1.0
            for j, rt in enumerate(self.roots):
                if j != zero_term_idx:
                    dp_val *= (1.0 - rt * x) if rev else (x - rt)
            dp_val *= self.leading_coeff
            if rev:
                dp_val *= -self.roots[zero_term_idx]
        else:
            for rt in self.roots:
                if rev:
                    sum_terms += (-rt) / (1.0 - rt * x)
                else:
                    sum_terms += 1.0 / (x - rt)
            dp_val = p_val * sum_terms

        return p_val, dp_val
