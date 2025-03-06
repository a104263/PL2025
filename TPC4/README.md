# TPC4 - Analisador Léxico
## 2025-03-06
### Inês Silva Marques - A104263
![A minha foto](../foto.jpg)

Para este TPC, tivemos de implementar um analisador léxico. Para isso, analisei o exemplo dado, e identifiquei os seguintes tokens:
- VAR: Variáveis, correspondem a palavras começadas por **?**
- SELECT: A expressão **select**
- WHERE: A expressão **where**
- CA: Abrir chavetas **{**
- CF: Fechar chavetas **}**
- POINT: Caracter **.**
- QUOTES: Aspas **"**
- LANG: Linguagem, por exemplo **@en**
- TYPE: Tipo, só um caractér, no exemplo **a**
- PROPERTY: Propriedade, por exemplo **dbo:MusicalArtist**
- LIMIT: expressão **LIMIT**
- NUM: Um número inteiro, por exemplo **1000**


Para a versão [tokenizer.py](tokenizer.py), coloquei os tokens e expressões correspondentes no [tokens.json](tokens.json), e utilizei o ficheiro [gen_tokenizer.py](gen_tokenizer.py) disponibilizado na aula.
Para o [tokenizer_lex.py](tokenizer_lex.py) utilizei a biblioteca **ply.lex** para definir os tokens e o que fazer em caso de erro.

Utilização:
Executar o ficheiro [tokenizer.py](tokenizer.py) ou o [tokenizer_lex.py](tokenizer_lex.py).
```
$ py tokenizer.py
```
ou
```
$ py tokenizer_lex.py
```
De seguida deve inserir as linhas a analisar, e o programa irá imprimir no ecrã os tokens organizados.
