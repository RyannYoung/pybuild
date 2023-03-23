"""Builds and universal wheel file of the project"""

import os

if __name__ == "__main__":
    os.system("python3 setup.py bdist_wheel --universal")
