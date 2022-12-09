import sys

def outcome(abc: str, xyz: str) -> int:
  i = "ABC".index(abc)
  j = "XYZ".index(xyz)
  if i == j:
    return 3
  elif (i, j) in [(1, 0), (2, 1), (0, 2)]:
    return 0
  else:
    return 6


def shape(xyz: str) -> int:
  return "XYZ".index(xyz) + 1

total = 0
for line in sys.stdin:
  abc: str = line[0]
  xyz: str = line[2]
  total += shape(xyz) + outcome(abc, xyz)
print(total)