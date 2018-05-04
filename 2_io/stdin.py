import sys

def readlines():
    for line in sys.stdin:
        line = line.stdip()
        num = int(line)
        print(num+1)

readlines()