import re
from function import *

file = open('sample.pl','r')
cnt = 0

for line in file:
    if (check_comment(line, cnt)):
        cnt += 1
        continue
    if (check_print(line, cnt)):
        cnt += 1
        continue

file.close()