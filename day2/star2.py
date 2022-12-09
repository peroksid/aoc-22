import sys


def outcome(xyz: str) -> int:
  return "XYZ".index(xyz) * 3

def shape(abc: str, xyz: str) -> int:
  i = "ABC".index(abc)
  j = "XYZ".index(xyz)
  if j == 1:
    return i + 1
  elif j == 0:
    return {
      0: 3,
      1: 1,
      2: 2}[i]
  elif j == 2:
    return {
      0: 2,
      1: 3,
      2: 1}[i]

total = 0
for line in sys.stdin:
  abc = line[0]
  xyz = line[2]

  total += outcome(xyz) + shape(abc, xyz)
print(total)