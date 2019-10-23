"""Script that calculates the mean from stdin

Parameters
----------
V : list from stdin

Returns
-------
prints mean to stdout
"""
import sys
import statistics

V = []
for l in sys.stdin:
    V.append(float(l))
try:
    print(statistics.mean(V))
except statistics.StatisticsError:
    pass
