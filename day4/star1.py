import sys
from typing import List, Tuple

def in_it(a, b):
  return b[0] <= a[0] <= a[1] <= b[1]

counter = 0
for line in sys.stdin:
  assignments: List[List[int]]  = [[int(y) for y in x.split('-')] for x in line.strip().split(',')]
  a, b = assignments
  if in_it(a, b) or in_it(b, a):
    counter += 1
print(counter)

