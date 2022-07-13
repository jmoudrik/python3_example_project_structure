import os
import sys

# add .. to python module search path
# this is un-necessary in pycharm
#    (as it adds dirs marked as Source or Tests there on its own)
# but important in notebook & when running from console
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# next we import mylib from the directory above

# make sure pycharm does not remove the import on auto format
# noinspection PyUnresolvedReferences
import mylib
