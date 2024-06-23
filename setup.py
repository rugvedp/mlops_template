from setuptools import find_packages,setup
from typing import List

setup(
    name='House Price',
    version='0.0.1',
    author='rugvedp',
    author_email='rugvedbpatil2003@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)