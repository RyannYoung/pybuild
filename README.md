# Pybuild

An opinionated script that runs automated linting, testing and building through a variety of well-known pip modules.

![pybuild](https://user-images.githubusercontent.com/33287530/227072818-fa070022-b29c-452e-8d7f-2f0aa7bf272d.gif)

## Installation

Download the latest `pybuild-*.whl` file from [here](https://github.com/RyannYoung/pybuild/releases)

Then install it using `pip` for example

``` shell
# Change to directory
cd /path/to/pybuild-*.whl

# Install via pip
pip install pybuild-*.whl
```

You should then have access to the pybuild script. Run it

``` shell
# Run build script on current folder
python3 -m build -i . 
```

If the script finds valid files within the input directory (`-i`) pybuild will run all the linting and test on all .py files within the folder (it does not run recursively)

## Technologies
Pybuild runs the following technologies
- [mypy](https://www.mypy-lang.org/): Static type checker for python
- [pylint](https://pypi.org/project/pylint/): Static code analyser
- [pycodestyle](https://pypi.org/project/pycodestyle/): Style guide checker using convention PEP 8
- [pydocstyle](https://pypi.org/project/pydocstyle/): Static docstring analysis using PEP 257
- tabnanny: Standard library for checking white-space correctness
- [bandit](https://pypi.org/project/bandit/): A security-based linter
- [doctest](https://docs.python.org/3/library/doctest.html): Run tests using docstrings
- [pytest](https://docs.pytest.org/en/7.2.x/): Runs py_test tests
