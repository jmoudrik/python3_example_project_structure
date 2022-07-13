import sys

# make sure pycharm does not remove the import on auto format
# noinspection PyUnresolvedReferences
from context import mylib

print(sys.path)

from mylib.io.console import println

println("hello!")
