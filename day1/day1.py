import sys

with open(sys.argv[1]) as f:
  lines = f.readlines()
  current = 0
  most_calories = 0
  for line in lines:
    if line.strip() == "":
      most_calories = max(most_calories, current)
      current = 0
      continue
    current += int(line)
  else:
    most_calories = max(most_calories, current)
print(most_calories)