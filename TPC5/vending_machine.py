import ply.lex as lex
import re
import sys
import math
import datetime
import json
import os

saldo = 0.00
produto = ""

def open_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data 

tokens = ["MOEDAEURO", "MOEDACENTIMO", "VIRGULA", "PRODUTO", "PONTO", "MOEDA", "LISTAR", "SELECIONAR", "IGNORAR", "NEWLINE"]
states = [("MOEDA", "exclusive"), ("LISTAR", "exclusive"), ("SELECIONAR", "exclusive")]

def t_MOEDA(t):
    r'MOEDA'
    t.lexer.begin("MOEDA")
    return t

def t_LISTAR(t):
    r'LISTAR'
    print(" ---------------------------------------------------")
    print("|  cod  |         nome         | quantidade | preço |")
    print(" ---------------------------------------------------")
    for produtoS in t.lexer.stock:
        print(f"| {produtoS['cod']:<5} | {produtoS['nome']:<20} | {str(produtoS['quant']):<10} | {str(produtoS['preco']):<5} |")
    print(" ---------------------------------------------------")
    t.lexer.begin("LISTAR")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    t.lexer.begin("SELECIONAR")
    return t

def t_SAIR(t):
    r'SAIR'
    t.lexer.begin("SAIR")
    return t

def t_NEWLINE(t):
    r'\n'
    pass

def t_MOEDA_MOEDAEURO(t):
    r'\de'
    global saldo
    saldo+=float(t.value[0])
    print(saldo)
    return t

def t_MOEDA_MOEDACENTIMO(t):
    r'\d\dc'
    global saldo
    saldo+=(float(re.split(r'c', t.value)[0]))/100
    print(saldo)
    return t

def t_MOEDA_VIRGULA(t):
    r','
    pass

def t_MOEDA_PONTO(t):
    r'\.'
    global saldo 
    saldostr  = re.split(r'\.', "{:.2f}".format(saldo))
    print("Saldo = " + saldostr[0] + "e" + saldostr[1] + "c")
    t.lexer.begin("INITIAL")
    return t

def t_LISTAR_NEWLINE(t):
    r'\n'
    t.lexer.begin("INITIAL")
    return t

def t_SAIR_NEWLINE(t):
    r'\n'
    t.lexer.begin("INITIAL")
    return t

def t_SELECIONAR_PRODUTO(t):
    r'A\d+'
    global produto
    produto = t.value
    global saldo 
    for produtoS in t.lexer.stock:
        if produtoS['cod'] == produto:
            if produtoS['quant'] == 0:
                print("Produto sem stock")
                return t
            else:
                if produtoS['preco'] <= saldo:
                    produtoS['quant'] -= 1
                    print("Pode retirar o produto dispensado: "+ produtoS['nome'])
                    saldo-= produtoS['preco']
                    saldostr  = re.split(r'\.', "{:.2f}".format(saldo))
                    print("Saldo = " + saldostr[0] + "e" + saldostr[1] + "c")
                    return t
                else:
                    print("Saldo insufuciente para satisfazer o seu pedido")
                    saldostr  = re.split(r'\.', "{:.2f}".format(saldo))
                    precostr = re.split(r'\.', "{:.2f}".format(produtoS['preco']))
                    print("Saldo = "+ saldostr[0] + "e" + saldostr[1] + "c"+"; Pedido = "+ precostr[0] + "e" + precostr[1] + "c")
                    return t
    print("Produto indisponível")
    return t

def t_SELECIONAR_NEWLINE(t):
    r'\n'
    t.lexer.begin("INITIAL")
    return t

def t_ANY_IGNORAR(t):
    r'[^\n\S]'
    pass

def t_ANY_error(t):
    print(f"Erro {t.value[0]}")
    t.lexer.skip(1)

def calcula_troco(saldo):
    res = ""
    moedasEuro = [2,1]
    moedasCent = [0.5,0.2,0.1,0.05,0.02,0.01]
    for value in moedasEuro:
        num = 0
        while saldo>=value:
            num+=1
            saldo-=value
        if num>0:
            res+=f"{num}x {value}e, "
    for value in moedasCent:
        num = 0
        while saldo>=value:
            num+=1
            saldo-=value
        if num>0:
            res+=f"{num}x {int(value*100)}c, "
    return res

lexer = lex.lex()
json_obj = open_json('stock.json')
stock_load = json_obj['stock']
print(str(datetime.date.today()) + ", Stock carregado, Estado atualizado.")
lexer.stock = stock_load
print("Bom dia. Estou disponível para atender o seu pedido.")
for linha in sys.stdin:
    if linha=="SAIR\n":
        troco = calcula_troco(saldo)
        print("Pode retirar o troco: "+troco)
        print("Até à próxima")
        with open('stock.json','w', encoding='utf-8') as file:
            json.dump(json_obj,file, indent=2, ensure_ascii=False)
        break
    else:
        lexer.input(linha)
        for tok in lexer:
            continue