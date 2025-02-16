# TPC2 - Dataset de obras musicais
## 2025-02-16
### Inês Silva Marques - A104263
![A minha foto](../foto.jpg)

Para este TPC deveríamos implementar um programa que, dado o dataset [obras.csv](obras.csv), devolvesse uma lista ordenada dos compositores, os períodos e número de obras de cada um, e um dicionário que, para cada período contém os títulos das obras deste, ordenadas alfabeticamente.
Para isto, foi preciso retirar as ocorrências de ";" na descrição das músicas, para depois conseguir separar os campos pelo ponto e vírgula.
De seguida, implementei o programa [obras_musicais.py](obras_musicais.py), que separa o ficheiro nas várias obras da seguinte forma:
```
re.findall(r"(?:[^;]+;){6}[^;\n]+", string)
```

Assim obtendo uma lista de strings separadas de acordo com a expressão regular, que identifica 6 vezes (campos exceto _id) um conjunto de qualquer caracter exceto ';' seguido de um ';', e de seguida um conjunto de qualquer caracter exceto ';' ou '\n', para reconhecer o campo _id.
De seguida, cada uma das obras é separada no ';', e os seus campos adicionados à lista ou dicionário pretendido.

Utilização:
Executar o ficheiro [obras_musicais.py](obras_musicais.py).
```
$ py obras_musicais.py
```