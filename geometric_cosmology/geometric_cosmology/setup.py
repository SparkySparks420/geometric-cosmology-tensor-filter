from setuptools import setup, find_packages

setup(
    name="geometric-cosmology",
    version="1.0.0",
    description="Gaussian tensor suppression from pure-geometric ΛCDM (arXiv:2512.xxxxx)",
    author="Anonymous Collaboration + Grok 4",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
    python_requires=">=3.8",
)
