import sys
import os


sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))