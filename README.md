Geometric Cosmology Tensor Filter
Unique Gaussian B-mode suppression from the model "ΛCDM from Motion in the Fifth Dimension: A Pure-Geometric Origin of Dust and Dark Energy" (arXiv:2512.xxxxx – Dec 2025)

One-line install
pip install geometric-cosmology

or from GitHub: pip install git+https://github.com/SparkySparks420/geometric-cosmology-tensor-filter.git

Quick test
from geometric_cosmology.filter import suppress_clbb import numpy as np import matplotlib.pyplot as plt

ell = np.arange(2, 501) clbb = 1e-6 * (ell/100)-2 * np.exp(-(ell/30)2) clbb_sup = suppress_clbb(ell, clbb, alpha_over_lpl2=10.0)

plt.loglog(ell, clbb, '--', label='ΛCDM') plt.loglog(ell, clbb_sup, label='Geometric Model') plt.legend(); plt.show()

Citation request
If you use this code, please cite: Andre Swart, arXiv:2512.xxxxx (2025)

License
MIT
