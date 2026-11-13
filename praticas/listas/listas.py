produtos = []                    # cria uma lista vazia
produtos.append("Teclado")
produtos.append("Mouse")
produtos.append("Monitor")       # insere elementos ao final da lista
print(produtos[1])               # acessa os elementos através de indices
print(len(produtos))             # informa o tamanho da lista, len() retorna a quantidade de elementos

for produto in produtos:         # percorre e exibe os elementos da lista
    print(produto)