import re
from setuptools import setup, find_packages

setup(
    name="Sorting-Algorithm-Visualiser",
    version="0.0.1",
    description="This is a visualiser of 6 different sorting algorithm using python and the pygame module.",
    url="https://github.com/ernum/Sorting-Algorithm-Visualiser",
    author="Ernest Umeh",
    packages=find_packages(where="."),
    package_data={
        "Visualiser.images": ["*.png"],
    },
    include_package_data=True,
    install_requires=[
        'pygame'
    ],
    python_requires='>=3'
)
