import ply.lex as lex
import sys

tokens = (
    'VAR',
    'SELECT',
    'WHERE',
    'CA',
    'CF',
    'POINT',
    'QUOTES',
    'LANG',
    'TYPE',
    'PROPERTY',
    'LIMIT',
    'NUM'
)

t_VAR = r"(\?\w+)"
t_SELECT = r"select"
t_WHERE = r"where"
t_CA = r"{"
t_CF = r"}"
t_POINT = r"\."
t_QUOTES = r'\".+\"'
t_LANG = r'@\w+'
t_TYPE = r'\b\w\b'
t_PROPERTY = r'\w+:\w+'
t_LIMIT = r"LIMIT"
t_NUM = r'\d+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)    
