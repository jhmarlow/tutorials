# Install a pip package in the current Jupyter kernel
import sys
!{sys.executable} -m pip install <package>

# Multiline editing
Hold option

# Quick docs
select func, etc.
Hold Option

# Refactor all
select
press F2
# Refactor file
select
press Ctrl + F2

# Define linting strength by creating a .pylintrc file and enable/disable
.pylintrc

# Capture requirements
requirements.txt
pip freeze