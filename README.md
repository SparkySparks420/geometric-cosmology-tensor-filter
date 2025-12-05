a polished all‑in‑one README.md you can paste directly into your repo. I’ve cleaned up formatting, ensured consistent Markdown, and placed your image and demo code in the right spots:

markdown
# Geometric Cosmology Tensor Filter

**The only model predicting Gaussian B‑mode suppression on ℓ < 40 from pure geometry**  
→ *"ΛCDM from Motion in the Fifth Dimension"* (arXiv:2512.xxxxx)

![Smoking Gun](demo_bmodes.png)

---

## One‑line install

```bash
pip install geometric-cosmology
Demo
python
from geometric_cosmology.filter import suppress_clbb
import numpy as np, matplotlib.pyplot as plt

ell = np.arange(2, 501)
clbb = 1e-14 * (ell/100)**-2 * np.exp(-(ell/30)**2)
clbb[ell < 40] *= 2500
clbb_sup = suppress_clbb(ell, clbb)

plt.loglog(ell, clbb, '--', label='ΛCDM')
plt.loglog(ell, clbb_sup, label='Geometric Model')
plt.legend(); plt.show()
Project Motivation
Cosmology today faces the challenge of explaining dark energy and dust without introducing arbitrary new fields. This project implements a purely geometric model where ΛCDM arises naturally from motion in a fifth dimension. Unlike traditional braneworld scenarios, this approach eliminates dark radiation and Weyl anisotropic stress, while predicting a distinctive Gaussian suppression of B‑mode polarization. The filter provided here allows researchers to test these predictions directly against upcoming CMB experiments such as LiteBIRD and the Simons Observatory.

Unique Gaussian B‑mode suppression from the model "ΛCDM from Motion in the Fifth Dimension: A Pure‑Geometric Origin of Dust and Dark Energy" (arXiv:2512.xxxxx – Dec 2025)

Installation
You can install the package directly from PyPI:

bash
pip install geometric-cosmology
Or install the latest version from GitHub:

bash
pip install git+https://github.com/YOURUSERNAME/geometric-cosmology-tensor-filter.git
Quick Test
python
from geometric_cosmology.filter import suppress_clbb
import numpy as np
import matplotlib.pyplot as plt

ell = np.arange(2, 501)
clbb = 1e-6 * (ell/100)**-2 * np.exp(-(ell/30)**2)
clbb_sup = suppress_clbb(ell, clbb, alpha_over_lpl2=10.0)

plt.loglog(ell, clbb, '--', label='ΛCDM')
plt.loglog(ell, clbb_sup, label='Geometric Model')
plt.legend(); plt.show()
This produces a direct comparison between the standard ΛCDM prediction and the geometric suppression model.

Note on the Quick Test
The quick test provided above is only a sanity check to confirm that the package installs correctly and the filter runs without errors. Because it uses a toy baseline spectrum, the ΛCDM and suppressed curves may look very similar.

The real difference appears when you apply the filter to actual CMB B‑mode spectra from simulations or experiments. With real data, the geometric model predicts a distinctive Gaussian suppression that upcoming missions like LiteBIRD and the Simons Observatory can test directly.

How This Compares to Other Braneworld Models
Model	Dark Radiation (C≠0)	Weyl anisotropic stress	B‑mode suppression shape	Testable in next 5 years?
Standard RS‑II (fixed brane)	Yes (huge)	Large	None	Already ruled out
Moving brane (Einstein only)	Yes	Large	None	Ruled out by Planck
This model + GB	No (C=0)	Suppressed to zero	Gaussian exp(−k²/k_GB²)	YES — LiteBIRD/SO
Key point: This is the only model with 
𝐶
=
0
 and 
𝜋
𝑊
=
0
 that survives current constraints and remains testable with upcoming experiments.

Citation Request
If you use this code, please cite: Andre Swart, ΛCDM from Motion in the Fifth Dimension: A Pure‑Geometric Origin of Dust and Dark Energy, arXiv:2512.xxxxx (2025)

License
MIT

License
MIT

License
MIT
