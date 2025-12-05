from setuptools import setup, find_packages

setup(
    name="geometric-cosmology",
    version="0.1.0",
    description="Geometric Cosmology Tensor Filter",
    author="Andre Swart",
    license="MIT",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
    python_requires=">=3.8",
)
