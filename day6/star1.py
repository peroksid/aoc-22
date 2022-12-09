import sys


def main():
  line = sys.stdin.readline()
  for i in range(len(line)):
    slice = line[i-3:i+1]
    if len(set(line[i-4:i])) == 4:
      print(i)
      return
    


if __name__ == "__main__":
  main()
