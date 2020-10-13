"""Setuptools module"""
from setuptools import setup, find_packages

setup(
    name="dobharchu",
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click>=7.1.2",
        "Requests>=2.22.0",
    ],
    entry_points={"console_scripts": ["dobharchu = dobharchu.cli:main"]},
)
