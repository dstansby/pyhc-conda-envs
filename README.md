# Python in Heliophyisics conda environments

## Available environments
### `environment_core.yml`
- Python 3.11
- Includes all PyHC core packages
- Does *not* include `kamodo`, as it is not compatible with Python 3.11
- Does *not* include `spacepy`, as I couldn't work out how install it on my laptop

## Testing
Continous integration is set up to test that:
- The environment files work on Linux
- The PyHC packages can be imported

**There is no testing that the packages work correctly.**

## Creation method

1. Create a new conda environment and install Python.
1. Set the only conda channel to be `conda-forge`.
1. Install as many PyHC projects from conda as possible.
1. For remaining PyHC projects, install as many of their dependencies from conda as possible.
1. Install any remaining dependencies using pip.
1. Install remaining PyHC projects using pip.
1. Remove any packages that are not generally available across operating system.
   These will still be installed if needed as dependencies, but aren't pinned to specific versions in the environment file.
   Currently these are:
    - `libev`
    - `ncurses`
    - `libgfortran5`
    - `brunsli`
    - `libcxx`
    - `libnghttp2`
    - `readline`
    - `libedit`
