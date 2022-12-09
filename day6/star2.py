import sys

def log_in_test(line):
  if __name__ != "__main__":
    sys.stderr.write(line + "\n")

def solve(line: str) -> int:
  """
  >>> solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
  19
  >>> solve('bvwbjplbgvbhsrlpgdmjqwftvncz')
  23
  >>> solve('nppdvjthqldpwncqszvftbrmjlhg')
  23
  >>> solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
  29
  >>> solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
  26
  """
  log_in_test(line)
  for i in range(len(line)):
      slice = line[i-13:i+1]
      log_in_test(f"{slice}, {set(slice)}, {len(set(slice))}, {i}")
      if len(set(slice)) == 14:
        return i + 1
  raise RuntimeError("no message!")


def main():
  print(solve(sys.stdin.readline().strip()))
  

if __name__ == "__main__":
  main()


