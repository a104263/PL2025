import re

ficheiro = open("obras.csv", "r", encoding="utf8")

compositores = list()
n_obras_periodo = dict()
obras_periodo = dict()

string = ficheiro.read()

for linha in re.findall(r"(?:[^;]+;){6}[^;\n]+", string):
    if linha!='nome;desc;anoCriacao;periodo;compositor;duracao;_id':
        obra = re.split(r";", linha, 0)
        if(obra[4] not in compositores):
            compositores.append(obra[4])
        if(obra[3] not in n_obras_periodo.keys()):
            n_obras_periodo[obra[3]] = 1
            obras_periodo[obra[3]] = list()
            obras_periodo[obra[3]].append(re.sub("\n", "", obra[0], 0))
        else:
            n_obras_periodo[obra[3]] += 1
            obras_periodo[obra[3]].append(re.sub("\n", "", obra[0], 0))

compositores.sort()
for periodo in obras_periodo.keys():
    obras_periodo[periodo].sort()

print(compositores)
print(n_obras_periodo)
print(obras_periodo)

ficheiro.close()