## Numerical experiments for Algorithm 1. in the paper: 
**Heuristic Acceleration of Near-Optimal Polynomial Root-Finders**
by Soo Go, Won Geun Kim, and Victor Y. Pan

#### Experimental Setup
We implemented the algorithm 1  in Python, by using the $\texttt{NumPy}$ library for efficient numerical operations and polynomial handling. 

#### Python environments and library versions ($\texttt{pip freeze > requirements.txt}$):

- numpy==2.5.0
- pandas==3.0.4
- python-dateutil==2.9.0.post0
- six==1.17.0
- tzdata==2026.2

#### The main entry of the program is located in the file: ***testing_algorithms.py***

#### Implementation and Parameters 
For each test polynomial of degree $d$, we have chosen its $m$ roots uniformly at random in the disc $D(0, 1/1.00001)$ and its other  $d-m$  roots  uniformly at random in the ring $A(0, 1,  10^{14})$.  Tiny isolation $\theta=1.00001$ of the sets of $m$ internal and $d-m$ external roots from one another  ensured that the  roots in these sets were counted  correctly in our experiments. 

In our experiments we only dealt with soft e/i tests for polynomials $p$ having roots in specified domains, and so double  complex precision (15 decimal digits per component -  the default complex type [128 bits] in $\texttt{NumPy}$)  was suffiicient to ensure correctness of our computations.

We performed our tests for $d = 6400, 12800, 25600$, $\sigma = 1.4$, $\theta=1.00001$ and $m=0, 1, 2, 3, 4, 5, 10, 50, 100, d/16, d/8 d/4, d/2, 3d/4, d-1, d$.

For each of the 21 pairs $(d, \nu)$ we run 100 independent trials.

We set $u_- = 0$ and $u_+ = \lceil \log_2(\log_\sigma (d) + 1) \rceil$ equal to $5$ in  our tests. We displayed the test results (see below for a consle output) in a table format (below). In all 2,100 trials, Algorithm 1 succeeded in 100\% tests, by correctly outputting 0 for $\nu=0$ and 1 otherwise. 

We displayed the maximal number of points at which NIRs were evaluated and the maximal integert $h$ used. The dominant cost of computing NIR remained stable as $d$ scaled but decreased significantly as $m$ increased. 

#### Sample Console Output of the Tests with Various Numbers $\mu$ of Internal Roots
- **Processor**: AMD Ryzen 7 5825U with Radeon Graphics          (2.00 GHz)
- **RAM**: 16.0 GB
  
C:\Users\wkim2\PycharmProjects\semi_heuristic_6_29_2026\venv\Scripts\python.exe 

C:\Users\wkim2\PycharmProjects\semi_heuristic_6_29_2026\testing_algorithms.py 

Testing degree d=25600 with sigma=1.4, isolation(theta)=1.00001: fl(log_sigma(d)) = 31

max_q=31, u=5...

Results for sigma-soft EI test: d=25600, r_1 upper bound=1.000000e+14

Exclusion counts by m:

m=0: 100 out of 100

m=1: 0 out of 100

m=2: 0 out of 100

m=3: 0 out of 100

m=4: 0 out of 100

m=5: 0 out of 100

m=10: 0 out of 100

m=20: 0 out of 100

m=50: 0 out of 100

m=100: 0 out of 100

m=1600: 0 out of 100

m=3200: 0 out of 100

m=6400: 0 out of 100

m=12800: 0 out of 100

m=19200: 0 out of 100

m=25599: 0 out of 100

m=25600: 0 out of 100



d          m   sigma  isolation  incorrect  max_evals  max_h

25600      0    1.4    1.00001          0         32     31

25600      1    1.4    1.00001          0         32      0

25600      2    1.4    1.00001          0         32      0

25600      3    1.4    1.00001          0         32      0

25600      4    1.4    1.00001          0         32      0

25600      5    1.4    1.00001          0         32      0

25600     10    1.4    1.00001          0         32      0

25600     20    1.4    1.00001          0         32      0

25600     50    1.4    1.00001          0         32      0

25600    100    1.4    1.00001          0         32      0

25600   1600    1.4    1.00001          0         16      0

25600   3200    1.4    1.00001          0          8      0

25600   6400    1.4    1.00001          0          8      0

25600  12800    1.4    1.00001          0          4      0

25600  19200    1.4    1.00001          0          4      0

25600  25599    1.4    1.00001          0          4      0

25600  25600    1.4    1.00001          0          4      0

Process finished with exit code 0

| Input Parameter: $d$ | Input Parameter: $\sigma$ | Input Parameter: $\theta$ | Number of roots $m$ in $D(0,1/\theta)$ | Max # NIR Evals | Max h | Output: incorrect |
|---|---|---|---|---|---|---|
| 25600 | 1.4 | 1.00001 | $m = 0$ | 32 | 31 | 0 |
| 25600 | 1.4 | 1.00001 | $m \in [1, 2, 3, 4, 5, 10, 50, 100]$ | 32 | 0 | 0 |
| 25600 | 1.4 | 1.00001 | $m = 1600$ | 16 | 0 | 0 |
| 25600 | 1.4 | 1.00001 | $m \in [3200, 6400]$ | 8 | 0 | 0 |
| 25600 | 1.4 | 1.00001 | $m \in [12800, 19200, 25599, 25600]$ | 4 | 0 | 0 |




