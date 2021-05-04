import re
import numpy as np
keywords = ['DATA','END','FILE','STDIN','LINE','PACKAGE','and','cmp','continue','CORE','do',\
            'else','elsif','eq','exp','for','foreach','ge','gt','if','le','lock','lt',\
            'm','ne','no','or','package','q','qq','qr','qw','qx','s','sub','tr',\
            'unless','until','while','xor','y', 'use','my','return','print','die'] # fix danh sách này cho đúng giúp tui

def check(line, cur):
    if (is_comment(line)):
        print(f'(< {line} >, COMMENT, {cur})')
        return True
    if (is_RE(line)):
        print(f'(< {line} >, RE, {cur})')
        return True
    if (is_NAMESPACE(line)):
        print(f'(< {line} >, NAMESPACE, {cur})')
        return True
    if (is_keyword(line)):
        print(f'(< {line} >, KEYWORD, {cur})')
        return True
    if (is_NUM8(line)):
        print(f'(< {line} >, BASE08NUM, {cur})')
        return True
    if (is_NUM16(line)):
        print(f'(< {line} >, BASE16NUM, {cur})')
        return True
    if (is_ID(line)):
        print(f'(< {line} >, ID, {cur})')
        return True
    if (is_SEMICOLON(line)):
        print(f'(< {line} >, SEMICOLON, {cur})')
        return True
    if (is_COMMA(line)):
        print(f'(< {line} >, COMMA, {cur})')
        return True
    if (is_LPAREN(line)):
        print(f'(< {line} >, LPAREN, {cur})')
        return True
    if (is_RPAREN(line)):
        print(f'(< {line} >, RPAREN, {cur})')
        return True
    if (is_ASSIGN(line)):
        print(f'(< {line} >, ASSIGN, {cur})')
        return True
    if (is_LBRAC(line)):
        print(f'(< {line} >, LBRAC, {cur})')
        return True
    if (is_RBRAC(line)):
        print(f'(< {line} >, RBRAC, {cur})')
        return True
    if (is_LESS(line)):
        print(f'(< {line} >, LESS, {cur})')
        return True
    if (is_GREATER(line)):
        print(f'(< {line} >, GREATER, {cur})')
        return True
    if (is_GTEQ(line)):
        print(f'(< {line} >, GTEQ, {cur})')
        return True
    if (is_LTEQ(line)):
        print(f'(< {line} >, LTEQ, {cur})')
        return True
    if (is_EQUAL(line)):
        print(f'(< {line} >, EQUAL, {cur})')
        return True
    if (is_NEQUAL(line)):
        print(f'(< {line} >, NEQUAL, {cur})')
        return True
    if (is_Comparison(line)):
        print(f'(< {line} >, COMPARISION, {cur})')
        return True
    if (is_NUM(line)):
        print(f'(< {line} >, NUM, {cur})')
        return True
    if (is_REALNUM(line)):
        print(f'(< {line} >, REALNUM, {cur})')
        return True
    if (is_STRING(line)):
        print(f'(< {line} >, STRING, {cur})')
        return True 
    if(is_plus(line)):
        print(f'(< {line} >, PLUS, {cur})')
        return True
    if(is_plusEQ(line)):
        print(f'(< {line} >, PLUSEQ, {cur})')
        return True
    if(is_minus(line)):
        print(f'(< {line} >, MINUS, {cur})')
        return True
    if(is_minusEQ(line)):
        print(f'(< {line} >, MINUSEQ, {cur})')
        return True
    if(is_mul(line)):
        print(f'(< {line} >, MUL, {cur})')
        return True
    if(is_mulEQ(line)):
        print(f'(< {line} >, MULEQ, {cur})')
        return True
    if(is_div(line)):
        print(f'(< {line} >, DIV, {cur})')
        return True
    if(is_divEQ(line)):
        print(f'(< {line} >, DIVEQ, {cur})')
        return True
    if(is_remain(line)):
        print(f'(< {line} >, REMAIN, {cur})')
        return True
    if(is_remainEQ(line)):
        print(f'(< {line} >, REMAINEQ, {cur})')
        return True
    if (is_POW(line)):     
        print(f'(< {line} >, POWER, {cur})')
        return True
    if (is_and(line)):     
        print(f'(< {line} >, AND, {cur})')
        return True
    if (is_or(line)):     
        print(f'(< {line} >, OR, {cur})')
        return True
    if (is_XOR(line)):     
        print(f'(< {line} >, XOR, {cur})')
        return True
    if (is_LShift(line)):     
        print(f'(< {line} >, LSHIFT, {cur})')
        return True
    if (is_RShift(line)):     
        print(f'(< {line} >, RSHIFT, {cur})')
        return True
    if (is_Dor(line)):     
        print(f'(< {line} >, DOR, {cur})')
        return True
    if (is_Dand(line)):     
        print(f'(< {line} >, DAND, {cur})')
        return True    
    if (is_PLUSPLUS(line)):
        print(f'(< {line} >, INC, {cur})')
        return True
    if (is_MINUSMINUS(line)):
        print(f'(< {line} >, DEC, {cur})')
        return True
    if (is_RBraces(line)):
        print(f'(< {line} >, RBRACES, {cur})')
        return True
    if (is_LBraces(line)):
        print(f'(< {line} >, LBRACES, {cur})')
        return True
    if (is_HASHASSIGN(line)):
        print(f'(< {line} >, HASH ASSIGN, {cur})')
        return True
    if (is_RETEST(line)):
        print(f'(< {line} >, RE TEST, {cur})')
        return True


    return False

def extract(line, cur):
    if (len(line) == 0):
        return
    while(line[0] == ' '):
        line = line[1:]
    while(line[-1] == ' '):
        line = line[:-1]
    while(line[0] == '\t'):
        line = line[1:]
    while(line[-1] == '\t'):
        line = line[:-1]
    Lrange = np.arange(1,len(line)+1)
    Lrange = Lrange[::-1]
    for Length in Lrange:
        if (check(line[:Length],cur)):
            extract(line[Length:],cur)
            return 

def is_comment(line):
    pattern = re.compile(r'\#.*')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line)):
            ok = 1
            return ok

    return ok



def is_keyword(line):
    global keywords
    return (line in keywords)

def is_ID(line):
    global keywords
    pattern = re.compile(r'[\$\@\%\&][\_a-zA-Z][\_a-zA-Z0-9]*')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line)):
            ok = 1
            return ok
    
    pattern = re.compile(r'[\_a-zA-Z][\_a-zA-Z0-9]*')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line) and line not in keywords):
            ok = 1
            return ok
    return ok

def is_NUM(line):
    pattern = re.compile(r'\d+')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line) and line not in keywords):
            ok = 1
            return ok
    return ok

def is_RE(line):
    pattern = re.compile(r'(/.+?/|\|.+?\|)')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line) and line not in keywords):
            ok = 1
            return ok
        break
            
            
    return ok

def is_REALNUM(line):
    pattern = re.compile(r'\d+\.\d+')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line) and line not in keywords):
            ok = 1
            return ok
    return ok

def is_STRING(line):
    pattern = re.compile(r'(\".*?[^\\]\"|\'.*?[^\\]\')')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line) and line not in keywords):
            ok = 1
            return ok
    return ok

def is_NUM8(line):
    pattern = re.compile(r'[0-9]+x08')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line) and line not in keywords):
            ok = 1
            return ok
    return ok

def is_NUM16(line):
    pattern = re.compile(r'[0-9A-F]+x16')
    matches = pattern.finditer(line)
    ok = 0
    for match in matches:
        if (match.start() == 0 and match.end() == len(line) and line not in keywords):
            ok = 1
            return ok
    return ok

def is_RETEST(line):
    return line == '=~'

def is_NAMESPACE(line):
    return line == '::'

def is_SEMICOLON(line):
    return line == ';'

def is_COMMA(line):
    return line == ','

def is_RPAREN(line):
    return line == ')'

def is_LPAREN(line):
    return line == '('

def is_ASSIGN(line):
    return line == '='

def is_LBRAC(line):
    return line == '['

def is_RBRAC(line):
    return line == ']'

def is_LESS(line):
    return line == '<'

def is_GREATER(line):
    return line == '>'

def is_GTEQ(line):
    return line == '>='

def is_LTEQ(line):
    return line == '<='

def is_EQUAL(line):
    return line == '=='

def is_NEQUAL(line):
    return line == '!='

def is_Comparison(line):
    return line == '<=>'

def is_plus(line):
    return line == '+'

def is_minus(line):
    return line == '-'

def is_mul(line):
    return line == '*'

def is_div(line):
    return line == '/'

def is_remain(line):
    return line =='%'

def is_plusEQ(line):
    return line == '+='

def is_minusEQ(line):
    return line == '-='

def is_mulEQ(line):
    return line == '*='

def is_divEQ(line):
    return line == '/='

def is_remainEQ(line):
    return line =='%='

def is_POW(line):
    return line == '**'

def is_and(line):
    return line == '&'

def is_or(line):
    return line == '|'

def is_XOR(line):
    return line == '^'

def is_NOT(line):
    return line == '~'

def is_LShift(line):
    return line == '<<'

def is_RShift(line):
    return line == '>>'

def is_Dand(line):
    return line == '&&'

def is_Dor(line):
    return line == '||'

def is_PLUSPLUS(line):
    return line == '++'

def is_MINUSMINUS(line):
    return line == '--'

def is_LBraces(line):
    return line == '{'

def is_RBraces(line):
    return line == '}'

def is_HASHASSIGN(line):
    return line == '=>'