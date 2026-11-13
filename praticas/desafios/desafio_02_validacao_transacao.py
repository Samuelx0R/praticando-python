# Desafio 02 - Validação de Transação Bancária
# Verifica se (valor - taxa) cobre o pagamento mínimo exigido.

# --- Entrada de dados ---
entrada = input()
valor_transacao, taxa_servico, pagamento_minimo = map(float, entrada.split())

# --- Cálculo do valor final ---
valor_final = valor_transacao - taxa_servico

# --- Validação ---
if valor_final >= pagamento_minimo:
    print("Aprovada")
else:
    print("Recusada")
