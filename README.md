Geometric Cosmology Tensor Filter
![Smoking Gun](demo_bmodes.png)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![arXiv](https://img.shields.io/badge/arXiv-2512.xxxxx-orange.svg)
![GitHub stars](https://img.shields.io/github/stars/SparkySparks420/geometric-cosmology-tensor-filter?style=social)  
The only model predicting a clean Gaussian suppression of primordial B-modes on ℓ < 40 - from pure geometry.
"ΛCDM from Motion in the Fifth Dimension: A Pure Geometric Origin of Dust and Dark Energy"
(waiting for arXiv – Dec 2025)
The Big Idea: Instead of introducing unknown particles or forces, we show that our familiar 4-dimensional universe (the 'brane') is actually moving through a larger, 5-dimensional spacetime (the 'bulk'). In this framework, the gravity felt by the brane naturally creates the illusion of both Dark Matter (as geometric motion, or 'Weyl dust') and Dark Energy (as a steady-state energy level achieved by the moving brane).

The Problem Solved: Previous attempts at this idea failed because they created unstable universes. We fix this by adding a minimal mathematical stability term the Gauss-Bonnet term, often suggested by string theory to the 5D geometry.

The Unique Prediction (The Smoking Gun): The very term that fixes the stability problem forces a unique change on primordial gravitational waves (the tensor signal from the Big Bang). Specifically, it acts like a filter, suppressing the gravitational wave signal only on the very largest scales (low frequencies).

How We Test It: We predict a specific "Gaussian dip" in the Cosmic Microwave Background's B-mode polarization at intermediate scales ($\ell \approx 40-50$). This is the only way this specific model deviates from standard $\Lambda$CDM. Future experiments like LiteBIRD and CMB-S4 can test this exact shape. If they find this specific dip, it would be definitive evidence of the fifth dimension shaping our cosmology.



Units and convention note: “We work in the 5D EGB convention with α\alpha carrying units of length squared and keff=1/ℓAdSk_{\text{eff}}=1/\ell_{\text{AdS}}. The linearized bulk tensor operator contains 24 α keff424\,\alpha\,k_{\text{eff}}^{4}; expanding k2+24 α keff4\sqrt{k^{2}+24\,\alpha\,k_{\text{eff}}^{4}} in the IR yields a Gaussian transfer with exponent ∝k2/keff3\propto k^{2}/k_{\text{eff}}^{3} (see Appendix C). Rescaled, 4D-effective α~=αkeff2\tilde{\alpha}=\alpha k_{\text{eff}}^{2} conventions are not used here.”

Final transfer function form:

T(k)  =  exp⁡ ⁣(− C 24 α k2keff3),T(k)\;=\;\exp\!\left(-\,\mathcal{C}\,\frac{24\,\alpha\,k^{2}}{k_{\text{eff}}^{3}}\right),

where C\mathcal{C} encodes the brane trajectory and normalization (fixed by the geodesic/probe action and matched in Appendix C).
Smoking GunWhy Care?Standard braneworlds fail:  Excess dark radiation  
Weyl stress kills structure formation

This model fixes it all with: Exact dust scaling  
C = 0  
π_W = 0

…and predicts a unique Gaussian dip in primordial tensors.  LiteBIRD • Simons Observatory • LISA
→ Plug in your data and test it today.One-Line Installbash

pip install geometric-cosmology

(or latest from GitHub:)bash

pip install git+https://github.com/SparkySparks420/geometric-cosmology-tensor-filter.git

30-Second Demopython

from geometric_cosmology.filter import suppress_clbb
import numpy as np
import matplotlib.pyplot as plt

ell = np.arange(2, 501)
clbb = 1e-14 * (ell/100)**-2 * np.exp(-(ell/30)**2)
clbb[ell < 40] *= 2500  # Boost reionization bump

clbb_sup = suppress_clbb(ell, clbb, alpha_over_lpl2=10.0)

plt.figure(figsize=(10,6))
plt.loglog(ell, clbb, '--', lw=2, color='black', label='ΛCDM')
plt.loglog(ell, clbb_sup, lw=3, color='red', label='Geometric Model (α=10)')
plt.axvspan(2, 40, alpha=0.15, color='red', label='Targeted ℓ<40')
plt.xlabel('ℓ')
plt.ylabel(r'$C_\ell^{BB}$')
plt.legend()
plt.grid(alpha=0.3)
plt.title('Primordial B-mode Suppression — The Smoking Gun')
plt.show()

How This Beats Other BraneworldsModel
Dark Radiation (C≠0)?
Weyl Stress (π_W)?
B-Mode Shape
Testable Now?
RS-II (fixed brane)
Yes (huge)
Large
None
Ruled out
Moving brane (Einstein)
Yes
Large
None
Ruled out
This + Gauss–Bonnet
No (C=0)
Zero
Gaussian exp(−k²/k_GB²)
YES

Key edge: Zero dark radiation + stabilized perturbations, with one unique, falsifiable signature.
Citation RequestIf you use this code, please cite:bibtex

@article{swart2025,
  title   = {ΛCDM from Motion in the Fifth Dimension: A Pure-Geometric Origin of Dust and Dark Energy},
  author  = {Swart, Andre},
  year    = {2025},
  eprint  = {2512.xxxxx},
  archivePrefix = {arXiv}
}

LicenseMIT - Fork it, test it, extend it.
Let’s see if the universe is a moving membrane.Questions? Open an Issue.
Collaboration welcome!
— Andre Swart, December 2025
Built with love, geometry, and a little bit of Gauss–Bonnet.
@GeometricCosmo

