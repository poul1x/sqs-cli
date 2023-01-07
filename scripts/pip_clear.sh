#!/bin/sh

# Get all packages we want to remove
pip freeze > uninstall.txt

# Remove packages if uninxtall.txt is not empty
grep -q . uninstall.txt && pip uninstall -y -r uninstall.txt

# Remove temporary file
rm uninstall.txt