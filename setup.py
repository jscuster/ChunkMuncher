import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "chunkmuncher",
    version = "0.0.2",
    author = "Jason Custer",
    author_email = "jscuster@gmail.com",
    description = "Recharge of the chunk module that was removed as of Python 3.13.",
    license = "PSF-2.0",
    keywords = "python chunk IFF PEP594",
    url = "https://github.com/jscuster/ChunkMuncher",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: File Formats",
        "License :: OSI Approved :: Python Software Foundation License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    #data_files=[('docs', ['docs'])],
    # Exclude the tests from being installed to site-packages
    exclude_package_data={'': ['tests']},
)
