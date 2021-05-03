import re
from function import *

file = open('sample.pl','r')
def main():
    cur = 0
    for line in file:
        if (line[-1] == '\n'):
            line = line[:-1]
        extract(line, cur)
        cur += 1
    file.close()


if __name__ == "__main__":
    main()