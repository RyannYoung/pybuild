#!/usr/bin/python

"""An intuitive build script that enforces clean and maintainable code.

How to use: Run it > read it > fix it
Author: Ryan Young

"""

from typing import List
import os
import argparse
from colorama import init, Fore, Style

init()


def get_python_files(dir_path: str) -> List[str]:
    """Find python files (ending with .py) and returns their path.

    Args:
        dir_path (str): The path to search (non-recursive)

    Returns:
        List[str]: A list of python files
    """
    return [filename for filename in os.listdir(dir_path) if filename.endswith(".py")]


def run_command(title: str, command: str) -> None:
    """Run a command using os.system().

    Args:
        command (str): The command to run
    """
    print(
        f"{Fore.GREEN}\033[1m========== START: {title.upper()} =========={Style.RESET_ALL}"
    )
    os.system(command)
    print(
        f"{Fore.GREEN}\033[1m========== FIN: {title.upper()} =========={Style.RESET_ALL}\n\n"
    )


def run(path: str = "."):
    """Run the build tool/linter.

    Args:
        path (str, optional): The path to specify the build tool on. Defaults to ".".
    """
    # Construct files
    files = get_python_files(path)
    file_string = " ".join(files)

    # LINTERS (opinionated precedence)
    run_command("mypy", f"python3 -m mypy {file_string}")
    run_command("pylint", f"python3 -m pylint {file_string}")
    run_command("pycodestyle", f"python3 -m pycodestyle {file_string}")
    run_command("pydocstyle", f"python3 -m pydocstyle {file_string}")
    run_command("tabnanny", f"python3 -m tabnanny -v {file_string}")

    # SECURITY
    run_command("bandit", f"python3 -m bandit -r {file_string}")

    # TESTING
    run_command("doctest", f"python3 -m doctest {file_string}")
    run_command("pytest", f"python3 -m pytest {path}")


# ========== MAINLINE
if __name__ == "__main__":

    # Create a shell cmdline parser
    parser = argparse.ArgumentParser(
        prog="build.py",
        description="An intuitive build script that enforces clean and maintainable code",
    )

    # Add arguments
    parser.add_argument(
        "-i",
        "--input",
        help="Input file to run the build process on",
        required=False,
        default=".",
    )

    # Parse and destructure args
    args = parser.parse_args()
    path = args.input

    run(path)
