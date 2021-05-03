import re
import numpy as np
keywords = ['if','then','function'] # fix danh sách này cho đúng giúp tui

def check(line, cur):
    if (is_comment(line)):
        print(f'<{line}, COMMENT, {cur}>')
        return True
    if (is_keyword(line)):
        print(f'<{line}, KEYWORD, {cur}>')
        return True
    if (is_ID(line)):
        print(f'<{line}, ID, {cur}>')
        return True
    
    return False

def extract(line, cur):
    if (len(line) == 0):
        return
    while(line[0] == ' '):
        line = line[1:]
    while(line[-1] == ' '):
        line = line[:-1]
    Lrange = np.arange(1,len(line)+1)
    Lrange = Lrange[::-1]
    for Length in Lrange:
        if (check(line[:Length],cur)):
            extract(line[Length:],cur)
            return 

def is_comment(line):
    pattern = re.compile(r'#\.*')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        return ok

    return ok

def is_keyword(line):
    global keywords
    return (line in keywords)

def is_ID(line):
    global keywords
    pattern = re.compile(r'[\$\@][a-zA-Z][a-zA-Z0-9]*')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line)):
            ok = 1
            return ok
    
    pattern = re.compile(r'[a-zA-Z][a-zA-Z0-9]*')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line) and line not in keywords):
            ok = 1
            return ok
    return ok