"""
Sample project setup file.
"""
from setuptools import setup


setup(
    name="prom_client_generics",
    version="0.0.1", # Change to 0.0.1 for new projects.
    author="Hashim Colombowala",
    author_email="",
    description="A sample Python package project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/MichaelCurrin/python-package-quickstart",
    packages=["prom_client"],
    package_dir={"prom_client_generics": "client"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)