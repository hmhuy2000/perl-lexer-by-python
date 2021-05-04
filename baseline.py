import re
from function import *

file = open('sample.pl','r')
def main():
    cur = 0
    for line in file:
        cur += 1
        if (line[-1] == '\n'):
            line = line[:-1]
        # print(line)
        extract(line, cur)
    file.close()


if __name__ == "__main__":
    main()