# Desafio 01 - Promoções da Loja
# Regras:
# - Menor que 50: agradecimento
# - 50 a 99: brinde
# - 100 a 199: R$ 10 de desconto
# - 200 ou mais: R$ 25 de desconto

# --- Entrada de dados ---
print("Insira o valor da compra: ")
valor_compra = float(input())

# --- Verificação do benefício ---
if valor_compra < 50.0:
    print("Obrigado por comprar conosco!")
elif valor_compra >= 50.0 and valor_compra <= 99.0:
    print("Parabens! Voce ganhou um brinde!")
elif valor_compra >= 100.0 and valor_compra <= 199.0:
    print("Desconto de 10 reais aplicado!")
else:
    print("Desconto de 25 reais aplicado!")
