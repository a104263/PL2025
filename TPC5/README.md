# TPC5 - Máquina de Vending
## 2025-03-13
### Inês Silva Marques - A104263
![A minha foto](../foto.jpg)

Para este TPC, teríamos de implementar um programa que se comportasse conforme o exemplo dado de uma máquina de vending. Para isso, usei o módulo **ply.lex** para organizer o input do utilizador da seguinte forma:

## Estados:
- MOEDA: Desde que o utilizador escreve a string **MOEDA** e até escrever **.** considero que está no estado onde irá reconhecer moedas, que serão organizadas com os tokens **MOEDAEURO**, **MOEDACENTIMO** e **VIRGULA**;
- LISTAR: Quando o utilizador pede para **LISTAR** os produtos na máquina e até mudar de linha, considero que está neste estado, onde vai sei imprimido o stock atual da máquina;
- SELECIONAR: Desde que o utilizador escreve **SELECIONAR** até mudar de linha está no estado em que pode selecionar um produto, reconhecido com o token **PRODUTO**.

## Tokens:
Além dos tokens que apenas causa a mudança para outro estado, e os correspondentes a caractéres que são ignorados, os tokens são os seguintes:
- MOEDAEURO: No estado **MOEDA**, este token corresponde a inserir uma moeda de 1€ ou 2€, que será adicionada ao saldo atual;
- MOEDACENTIMO: No estado **MOEDA**, corresponde a inserir uma moeda de menos de 1€, que é adicionada ao saldo;
- VIRGULA: No estado **MOEDA**, serve de separador entre as moedas;
- PRODUTO: No estado **SELECIONAR**, reconhece o identificador do produto a ser comprado, e, se o produto estiver no stock e existir saldo suficiente, é atualizado o stock e saldo conforme a compra (o ficheiro **stock.json** apenas é atualizado no fim do programa, quando o utilizador escrever **SAIR**).

Os dados do stock da máquina são então persistidos no ficheiro [stock.json](stock.json), que é carregado no início do programa, e atualizado no final.

## Utilização:
Executar o ficheiro [vending_machine.py](vending_machine.py).
```
$ py vending_machine.py
```

De seguida poderá interagir com o programa utilizando o mesmo formato do exemplo presente na BlackBoard.
