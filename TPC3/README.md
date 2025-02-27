# TPC3 - Conversor de MarkDown para HTML
## 2025-02-27
### Inês Silva Marques - A104263
![A minha foto](../foto.jpg)

Para este TPC, para praticar a utilização de expressões regulares e grupos de captura, tivemos de implementar um conversor de MarkDown para HTML, que transforma a sintaxe mais básica de markdown para o HTML equivalente.
Estou a usar expressões regulares para substituir os títulos do markdown (linhas começadas por *) por headers HTML, as partes do texto rodeadas por ** por bold, as partes rodeadas por * por itálico, e as imagens, links e listas pela sua sintaxe correspondente.

Utilização:
Executar o ficheiro [markdown_converter.py](markdown_converter.py).
```
$ py markdown_converter.py
```
De seguida vai ser pedido o ficheiro a converter, e o texto convertido será guardado num ficheiro com o mesmo nome mas com a extensão `.html` em vez de `.md`.