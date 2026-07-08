# heuristic_acc_root_finder
Heuristic Acceleration of Near-Optimal Polynomial Root-Finders

---
## Python environments and library versions (pip freeze > requirements.txt):

numpy==2.5.0
pandas==3.0.4
python-dateutil==2.9.0.post0
six==1.17.0
tzdata==2026.2

---
## Numerical experiments for Alg. 1. in the paper
### Experimental Setup
We implemented the algorithm 1  in Python, by using the $\texttt{NumPy}$ library for efficient numerical operations and polynomial handling. See above *requirements.txt*

For each test polynomial of degree $d$, we have chosen its $m$ roots uniformly at random in the disc $D(0, 1/1.00001)$ and its other  $d-m$  roots  uniformly at random in the ring $A(0, 1,  10^{14})$.  Tiny isolation of the sets of $m$ internal and $d-m$ external roots from one another  ensured that the  roots in these sets were counted  correctly in our experiments. 

In our experiments we only dealt with soft e/i tests for polynomials $p$ having roots in specified domains, and so double  complex precision (15 decimal digits per component -  the default complex type [128bits] in \texttt{NumPy})  was suffiicient  to ensure correctness of our computations.


### Implementation and Parameters.
- We performed  our tests for $d = 6400, 12800, 25600$, $\sigma = 1.4$, and $\mu= 0, 1, d/4, d/2, 3d/4, d-1, d$.
 

For each of the 21 pairs $(d, \nu)$ we run 100 independent trials.
   
%{\bf Tests for Alg. 1.}
We set $u_- = 0$ and $u_+ = \lceil \log_2(\log_\sigma (d) + 1) \rceil$ equal to $5$ in  our tests. We displayed the test results in Table~\ref{tabalg1results}. In all 2,100 trials, Alg.~1 succeeded in 100\% tests, by correctly outputting 0 for $\nu=0$ and 1 otherwise. 

We  displayed the maximal number of points at which NIRs were  evaluated and the maximal integert  $h$ used. The dominant cost of computing NIR remained stable as $d$ scaled but decreased significantly as $m$ increased. 
We are still testing Algs. 2 and 3. According to our initial test results, they perfrom slightly worse than Alg. 1, besides being limited to discs, while Alg.1 also test rings. 

