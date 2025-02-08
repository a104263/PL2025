import sys 

def somador(linha):
    res = 0 #valor da soma total
    i = 0
    on = True
    while(i<len(linha)):
        if on:
            valor = 0 #valor atual da sequencia de digitos
            if linha[i] == '=': #imprime se encontrar um sinal =
                print(res)
                i+=1
            elif linha[i].lower() == 'o': #procura a palavra "off"
                if i+2<len(linha) and linha[i+1].lower() == 'f' and linha[i+2].lower() == 'f':
                    i+=3
                    on = False
                else:
                    i+=1
            elif linha[i] in "0123456789": #se encontrar um digito
                while linha[i] in "0123456789":
                    valor = valor * 10 + int(linha[i])
                    i +=1
                res+=valor
            else:
                i += 1
        else:
            if linha[i] == '=': #imprime se encontrar um sinal =
                print(res)
                i+=1
            elif linha[i].lower()=='o': #procura a palavra "on"
                    if i+1<len(linha) and linha[i+1].lower() == 'n':
                        i+=2
                        on = True
            else:
                i += 1
    return res

for linha in sys.stdin:
    soma = somador(linha)
    print(soma)
