import sys
from typing import List, Tuple

def do_overlap(a, b):
  return b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1] or a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]

counter = 0
for line in sys.stdin:
  assignments: List[List[int]]  = [[int(y) for y in x.split('-')] for x in line.strip().split(',')]
  a, b = assignments
  if do_overlap(a, b):
    counter += 1
    #print(f"{a}:{b} -- OVERLAP")
  else:
    pass
    #print(f"{a}:{b} -- NOT overlap")
print(counter)

