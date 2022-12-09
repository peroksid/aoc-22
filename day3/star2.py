import sys

priorities = {}

for ch in range(ord('a'), ord('z')+1):
  priorities[chr(ch)] = ch - ord('a') + 1

for ch in range(ord('A'), ord('Z')+1):
  priorities[chr(ch)] = ch - ord('A') + 27

total = 0
for i, line in enumerate(sys.stdin, start=1):
  if i % 3 == 1:
    items = set(line.strip())
  else:
    items &= set(line.strip())
  print(items)
  if i % 3 == 0:
    assert len(items) == 1
    ch = items.pop()
    total += priorities[ch]
print(total)
