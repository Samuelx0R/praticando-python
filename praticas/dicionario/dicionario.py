# parecido com uso de structs em C, é possível associar informações por meio de chaves.
# um dicionário armazena informações em pares de chave e valor (key-value)

venda = {                           # declarando e preenchendo um dicionario
    "produto": "teclado",
    "quantidade": 3,
    "preco": 80.00
}

print(venda["produto"])             # acessando as informações de um dicionario
print(venda["quantidade"])
print(venda["preco"])

venda["quantidade"] = 5             # alterando valor de uma informação no dicionário
venda["categoria"] = "periférico"   # adicionando novas informações