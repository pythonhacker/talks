# Build the cython extension
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("mandelbrotc.pyx")
    )
