
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<VAR>(\?\w+))|(?P<SELECT>select)|(?P<WHERE>where)|(?P<CA>{)|(?P<CF>})|(?P<POINT>\.)|(?P<QUOTES>\".+\")|(?P<LANG>@\w+)|(?P<TYPE>\b\w\b)|(?P<PROPERTY>\w+:\w+)|(?P<LIMIT>LIMIT)|(?P<NUM>\d+)|(?P<SKIP>[ \t])|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())

        elif dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())
    
        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['CA']:
            t = ("CA", dic['CA'], linha, m.span())
    
        elif dic['CF']:
            t = ("CF", dic['CF'], linha, m.span())
    
        elif dic['POINT']:
            t = ("POINT", dic['POINT'], linha, m.span())
    
        elif dic['QUOTES']:
            t = ("QUOTES", dic['QUOTES'], linha, m.span())
    
        elif dic['LANG']:
            t = ("LANG", dic['LANG'], linha, m.span())
    
        elif dic['TYPE']:
            t = ("TYPE", dic['TYPE'], linha, m.span())
    
        elif dic['PROPERTY']:
            t = ("PROPERTY", dic['PROPERTY'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['NUM']:
            t = ("NUM", dic['NUM'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("ERRO", m.group(), linha, m.span())
        if not dic['SKIP']: reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)    
