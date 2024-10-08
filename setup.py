# __init__.py

from setuptools import setup, find_packages
# TODO: Redo __init__.py to contain my information
# setuptools is a Python library used to facilitate packaging and distribution of Python packages.
# It provides necessary functions to specify what files and dependencies are needed.

setup(
    name="modular_tic_tac_toe",  # This is the name of your package
    version="0.1",  # The initial release version
    packages=find_packages(where='src'),  # This function automatically finds all packages in the 'src' directory.
    package_dir={'': 'src'},  # This specifies that the packages are located under the 'src' directory.

    # Here we specify dependencies. These are external packages that your project depends on.
    # These packages will be installed automatically when installing your package.
    install_requires=[
        # For this project, there are no dependencies, but typically it would look like this:
        # 'numpy', 'pandas', etc.
    ],

    # Metadata for your project
    author="Max McWhae",
    author_email="20085898@tafe.wa.ed.au",
    description="A refactored version of a Tic Tac Toe game",
    license="MIT",
    keywords="tic-tac-toe refactoring",
    url="http://github.com/your_username/tic-tac-toe",  # project home page
)

# With this __init__.py in place, you can install your project in another environment with pip:
# pip install .
# The '.' means that __init__.py is in the current directory

