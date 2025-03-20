# TPC6 - Cálculo de Expressões
## 2025-03-20
### Inês Silva Marques - A104263
![A minha foto](../foto.jpg)

Para este TPC, tivemos de implementar um analisador sintático para expressões do tipo **1 + 2 * 3 - 4** por exemplo, ou seja, uma expressão que pode conter números, sinais de **+**, de **-** e de **\***.
Para isso, comecei por fazer o analisador léxico, que corresponde ao ficheiro [expressoes_analex.py](expressoes_analex.py), adaptado do ficheiro ``listas_analex`` fornecido. O analisador léxico reconhece os seguintes tokens:
- **NUM**: corresponde aos números, e é reconhecido com a expressão ``r'\d+'``;
- **OP**: corresponde às operações possíveis, reconhecidas com ``r'(\+|\-|\*)'``.

Separada a expressão em tokens, estes são passados para o analisador sintático [expressoes_anasin.py](expressoes_anasin.py) que reconhece as frases de acordo com a seguinte gramática:
- T = {op, num}
- S = Exp
- N = {Exp, ExpCont}
- P = {Exp -> num ExpCont, ExpCont -> (Vazio) | op Exp}

De seguida, guardamos as expressões reconhecidas numa estrutura, definida no ficheiro [expressoes_ast.py](expressoes_ast.py), e, no final, calculamos o valor da expressão, percorrendo a estrutura de forma a calcular as multiplicações primeiro, e de seguida as somas e subtrações pela ordem correta.

## Utilização:
Executar o ficheiro [prog.py](prog.py).
```
$ py prog.py
```