# Python in Heliophyisics conda environments
This respoitory contains a conda environment file that can be used to install [Python in Heliophysics](https://heliopython.org/) core packages in a single new conda environment

## Using
See [Creating an Environment from an Environment yml File](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).

The environment has the following spec:
- Python 3.11
- Includes all PyHC core packages
- Does *not* include `kamodo`, as it is not compatible with Python 3.11
- Does *not* include `spacepy`, as I couldn't work out how install it on my laptop

## Testing
Continous integration is set up to test that:
- The environment files work on Linux and macOS
- The PyHC packages can be imported

**There is no testing that the packages work correctly.**

## Design
The goal of the environment file is to make it possible to quickly create a fresh conda environment with all the core PyHC projects installed on any operating system.
This motivates the following design choices:
- Packages are installed from conda where possible.
- Packages are pinned to specific versions, to make sure the environment file as tested is the one that users use.


## Creation method

1. Create a new conda environment and install Python.
1. Set the only conda channel to be `conda-forge`.
1. Install as many PyHC projects from conda as possible.
1. For remaining PyHC projects, install as many of their dependencies from conda as possible.
1. Install any remaining dependencies using pip.
1. Install remaining PyHC projects using pip.
1. Remove any packages that are not generally available across operating system.
   Currently this is just `libgfortran`.
