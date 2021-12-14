import os
import sys

# Check dir/file path

if os.path.exists('test_dir/test_file.csv'):
    print('File exists in the specific path')
else:
    print('Nope, no file here.')

################################################################################
# Check directory
if os.path.isdir('test_dir'):
    print("Directory exists")
else
    print('Directory does not exist')

################################################################################

#Get current working directory using : sys.path[0]
pwd = sys.path[0]
# Use os.path.join to join path components
# os.chdir to change directories
os.chdir(os.path.join(pwd, 'test_dir'))

# Check file name only
if os.path.isfile('test_file.csv')
    print('File exists')
else:
    print('File not present')
