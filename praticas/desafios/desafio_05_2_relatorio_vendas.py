# Desafio 05-2 - Relatório Detalhado de Vendas
# Cadastra produtos, calcula o faturamento e exibe o relatório individual e total.

vendas = []
faturamento = 0

# --- Entrada da quantidade ---
qtd_produto = int(input("Informe a quantidade de produtos: "))

# --- Cadastro das vendas ---
for i in range(qtd_produto):
    venda = {}
    print(f"\n{i+1}º produto: ")
    venda["produto"] = input(f"\nNome: ")
    venda["qtd_vendida"] = int(input("Quantidade: "))
    venda["preco_un"] = float(input("preço unitário: "))

    vendas.append(venda)

# --- Cálculo do faturamento ---
for venda in vendas:
    faturamento += venda["qtd_vendida"] * venda["preco_un"]

# --- Relatório individual ---
print(" RELATÓRIO ".center(50, "="))

for i, venda in enumerate(vendas, start=1):
    print(f"\n{i} - {venda['produto']}")
    print(f"quantidade: {venda['qtd_vendida']}")
    print(f"preço unitário: R$ {venda['preco_un']:.2f}")
    print(f"Faturamento: R$ {venda['qtd_vendida'] * venda['preco_un']:.2f}")

print("=".center(50, "="))

# --- Faturamento total ---
print(f"\nFaturamento total: R$ {faturamento:.2f}")
