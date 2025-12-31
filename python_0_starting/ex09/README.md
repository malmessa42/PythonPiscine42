# ft_package

A simple package to count items in a list.

## Installation

## bash
pip install ./dist/ft_package-0.0.1.tar.gz

### pip uninstall ft_package -y 
### pip install dist/ft_package-0.0.1.tar.gz
### pip show ft_package

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["a", "b", "a"], "a"))  # Output: 2

# To build
    python -m build  
# To remove the files (kind of unbuild)
    rm -rf dist build *.egg-info
# To check package info
    pip show -v ft_package

