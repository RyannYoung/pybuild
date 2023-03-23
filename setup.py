"""Setup tool for the buildtool package."""

from setuptools import setup, find_packages

setup(
    name="pybuild",
    version="0.0.1",
    description="An intuitive build script that enforces clean and maintainable code",
    author="Ryan Young",
    packages=find_packages(),
    install_requires=[
        "bandit",
        "mypy",
        "pylint",
        "pycodestyle",
        "pydocstyle",
    ],
    py_modules=["pybuild"],
)
