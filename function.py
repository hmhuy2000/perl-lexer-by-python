import re
import source

def check_comment(line,cnt):
    pattern = re.compile(r'\s*#\s?.*\n')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(f'<"{match[0][:-1]}", comment, {cnt}>')

    return ok

def check_print(line, cnt):
    pattern = re.compile(r'\s*print(\s+".*"|\(".*"\));')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(match,cnt)
    
    return ok

def check_float(line, cnt):
    pattern = re.compile(r'\d+[.]\d+')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(match, cnt)

    return ok

def check_int(line, cnt):
    pattern = re.compile(r'\d')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(match, cnt)

    return ok


