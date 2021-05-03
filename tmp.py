import re

def check_comment(line,cnt):
    pattern = re.compile(r'\s*#\s?.*')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(f'<"{match[0][:-1]}", COMMENT, {cnt}>')

    return ok

def check_print(line, cnt):
    # print('');
    pattern = re.compile(r'\s*print\(\'.*\'\);')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(f'<"print", KEYWORD, {cnt}>')
        print(f'<"(", LBRACKETS, {cnt}>')
        print(f'<"\'", APOSTROPHE, {cnt}>')
        print(f'<"{match[0][7:-3]}", STRING, {cnt}>')
        print(f'<"\'", APOSTROPHE, {cnt}>')
        print(f'<")", RBRACKETS, {cnt}>')
        print(f'<";", COMMA, {cnt}>')
    if (ok):
        return ok
    # print '';
    pattern = re.compile(r'\s*print\s\'.*\';')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(f'<"print", KEYWORD, {cnt}>')
        print(f'<"\'", APOSTROPHE, {cnt}>')
        print(f'<"{match[0][7:-3]}", STRING, {cnt}>')
        print(f'<"\'", APOSTROPHE, {cnt}>')
        print(f'<";", COMMA, {cnt}>')
    if (ok):
        return ok
    # print("");
    pattern = re.compile(r'\s*print\(\".*\"\);')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(f'<"print", KEYWORD, {cnt}>')
        print(f'<"(", LBRACKETS, {cnt}>')
        print(f'<"\"", DOUBLE APOSTROPHE, {cnt}>')

        substr = match[0][7:-3]
        pattern = re.compile(r'\$[a-zA-Z][a-zA-Z0-9]*')
        matches = pattern.finditer(substr)
        start = 0
        for match in matches:
            finish = match.start()
            if (start < finish):
                print(f'<"{substr[start:finish]}",STRING, {cnt}>')    
            print(f'<"{substr[match.start():match.end()]}",VARIABLE, {cnt}>')
            start = match.end()
        if (start < len(substr) - 1):
                print(f'<"{substr[start:]}",STRING, {cnt}>')    

        print(f'<"\"", DOUBLE APOSTROPHE, {cnt}>')
        print(f'<")", RBRACKETS, {cnt}>')
        print(f'<";", COMMA, {cnt}>')
    if (ok):
        return ok 
    # print "";
    pattern = re.compile(r'\s*print\s\".*\";')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        ok = 1
        print(f'<"print", KEYWORD, {cnt}>')
        print(f'<"\"", DOUBLE APOSTROPHE, {cnt}>')

        substr = match[0][7:-3]
        pattern = re.compile(r'\$[a-zA-Z][a-zA-Z0-9]*')
        matches = pattern.finditer(substr)
        start = 0
        for match in matches:
            finish = match.start()
            if (start < finish):
                print(f'<"{substr[start:finish]}",STRING, {cnt}>')    
            print(f'<"{substr[match.start():match.end()]}",VARIABLE, {cnt}>')
            start = match.end()
        if (start < len(substr) - 1):
                print(f'<"{substr[start:]}",STRING, {cnt}>')    

        print(f'<"\"", DOUBLE APOSTROPHE, {cnt}>')
        print(f'<";", COMMA, {cnt}>')
    if (ok):
        return ok 

    return ok

def check_assign(line, cnt):
    pattern = re.compile(r'\s*\$[a-zA-Z][a-zA-Z0-9]*\s*(\=|\+\=|\-\=|\*\=|\/\=)\s*.+;')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        print(match)
    
    return ok