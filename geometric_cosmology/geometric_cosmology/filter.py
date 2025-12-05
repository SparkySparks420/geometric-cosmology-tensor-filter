"""
Geometric Cosmology Tensor Filter Template (v1.0 — Dec 2025)
Unique prediction of "ΛCDM from Motion in the Fifth Dimension"
arXiv:2512.xxxxx

Author: Anonymous Collaboration + Grok 4 (xAI)
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Physical constants ---
H0 = 67.74e5 / (3.08568e24)          # H0 in s⁻¹
c = 2.99792458e10                    # speed of light (cm/s)
Mpc = 3.08568e24                     # cm
h = 0.6774

# Planck length² in Mpc² (exact conversion)
L_PL_SQ = (1.616255e-35 / 3.08568e22)**2   # ≈ 2.74e-122 Mpc²

# Effective AdS curvature scale squared (microscopic, TeV-scale example)
K_EFF_SQ = (1e12 / 1e-18)**2         # TeV → 1/Mpc → (1/Mpc)²

# Comoving distance to last scattering
CHI_STAR = 14000.0                   # Mpc

def k_gb_squared(alpha_over_lpl2=10.0):
    """k_GB² = 24 α k_eff²  (central equation of the model)"""
    alpha = alpha_over_lpl2 * L_PL_SQ
    return 24.0 * alpha * K_EFF_SQ

def tensor_suppression(k, alpha_over_lpl2=10.0):
    """T_GB(k) = exp(-k² / k_GB²) — the smoking-gun filter"""
    return np.exp(-k**2 / k_gb_squared(alpha_over_lpl2))

# === CMB B-modes ===
def suppress_clbb(ell, clbb_lcdm, alpha_over_lpl2=10.0):
    k = ell / CHI_STAR
    return clbb_lcdm * tensor_suppression(k, alpha_over_lpl2)

# === Stochastic GW Background ===
def suppress_omegagw(f_hz, omegagw_lcdm, alpha_over_lpl2=10.0):
    k = 2 * np.pi * f_hz * (Mpc / c) / h   # frequency → comoving wavenumber
    return omegagw_lcdm * tensor_suppression(k, alpha_over_lpl2)

# ====================== DEMO ======================
if __name__ == "__main__":
    alpha_val = 10.0
    print(f"α = {alpha_val} ℓ_Pl²")
    print(f"k_GB ≈ {np.sqrt(k_gb_squared(alpha_val)):.2e} Mpc⁻¹")

    # CMB
    ell = np.arange(2, 501)
    clbb_base = 1e-6 * (ell/100)**-2 * np.exp(-(ell/30)**2)
    clbb_sup = suppress_clbb(ell, clbb_base, alpha_val)

    # SGWB
    f = np.logspace(-18, -7, 200)
    omegagw_base = 1e-16 * np.ones_like(f)
    omegagw_sup = suppress_omegagw(f, omegagw_base, alpha_val)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    ax1.loglog(ell, clbb_base, '--', label='ΛCDM', color='gray')
    ax1.loglog(ell, clbb_sup, label=f'Geometric Model (α={alpha_val})', lw=2)
    ax1.set_xlabel('ℓ'); ax1.set_ylabel('C_ℓ^{BB}'); ax1.legend(); ax1.grid(alpha=0.3)
    ax1.set_title('Primordial B-mode Suppression')

    ax2.loglog(f, omegagw_base, '--', label='ΛCDM', color='gray')
    ax2.loglog(f, omegagw_sup, label=f'Geometric Model', lw=2)
    ax2.set_xlabel('f [Hz]'); ax2.set_ylabel('Ω_GW(f)'); ax2.legend(); ax2.grid(alpha=0.3)
    ax2.set_title('SGWB High-Pass Filter')

    plt.suptitle('ΛCDM from Motion in the Fifth Dimension — Unique Tensor Signature')
    plt.tight_layout()
    plt.show()
