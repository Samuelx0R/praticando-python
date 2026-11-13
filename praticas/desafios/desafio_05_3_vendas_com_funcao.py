# Desafio 05-3 - Vendas com Função
# Usa função para calcular o faturamento individual e total.

vendas = []

# --- Função: cálculo de faturamento ---
def calcular_faturamento(vendas):
    faturamento_total = 0

    for venda in vendas:
        faturamento_individual = venda["qtd_vendida"] * venda["preco_un"]
        venda["faturamento_individual"] = faturamento_individual
        faturamento_total += faturamento_individual

    return faturamento_total


# --- Início do programa ---
qtd_produto = int(input("Informe a quantidade de produtos: "))

# --- Cadastro de produtos ---
for i in range(qtd_produto):
    venda = {}
    print(f"\n{i+1}º produto: ")
    venda["produto"] = input(f"\nNome: ")
    venda["qtd_vendida"] = int(input("Quantidade: "))
    venda["preco_un"] = float(input("preço unitário: "))

    vendas.append(venda)

# --- Chamada da função ---
faturamento_final = calcular_faturamento(vendas)

# --- Relatório individual ---
print(" RELATÓRIO ".center(50, "="))

for i, venda in enumerate(vendas, start=1):
    print(f"\n{i} - {venda['produto']}")
    print(f"quantidade: {venda['qtd_vendida']}")
    print(f"preço unitário: R$ {venda['preco_un']:.2f}")
    print(f"Faturamento: R$ {venda['faturamento_individual']:.2f}")

print("=".center(50, "="))

# --- Faturamento total ---
print(f"\nFaturamento total: R$ {faturamento_final:.2f}")
