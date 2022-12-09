import sys

priorities = {}

for ch in range(ord('a'), ord('z')+1):
  priorities[chr(ch)] = ch - ord('a') + 1

for ch in range(ord('A'), ord('Z')+1):
  priorities[chr(ch)] = ch - ord('A') + 27

total = 0
for line in sys.stdin:
  a = set(line[:len(line) / 2])
  b = set(line[len(line) / 2:])
  c = a & b
  assert len(c) == 1
  ch = c.pop()
  total += priorities[ch]
print(total)
