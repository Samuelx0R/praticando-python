# Desafio 04 - Lista de Produtos
# Cadastra produtos informados pelo usuário e exibe com numeração.

produtos = []

# --- Entrada da quantidade ---
qtd_produtos = int(input("Quantidade de produtos: "))

# --- Cadastro dos itens ---
for _ in range(qtd_produtos):
    nome = input("Nome do produto: ")
    produtos.append(nome)

# --- Exibição numerada ---
for i, produto in enumerate(produtos, start=1):
    print(f"{i} - {produto}")
