import sys


elves = []
with open(sys.argv[1]) as f:
  lines = f.readlines()
  current = 0
  
  for line in lines:
    if line.strip() == "":
      elves.append(current)
      current = 0
      continue
    current += int(line)
  else:
    elves.append(current)

elves.sort()
elves.reverse()
print(sum(elves[0:3]))