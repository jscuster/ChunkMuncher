import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "chunkmuncher",
    version = "0.0.1",
    author = "Jason Custer",
    author_email = "jscuster@gmail.com",
    description = "Recharge of the chunk module that was removed as of Python 3.13.",
    license = "PSF-2.0",
    keywords = "python chunk IFF PEP594",
    url = "https://github.com/jscuster/ChunkMuncher",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "Topic :: File Formats",
        "License :: OSI Approved :: Python Software Foundation License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
    ],
    include_package_data=True,  # Include all package data, including docs and tests
)
