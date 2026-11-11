# Permitem desvio de fluxo de controle quando determinadas expressões lógicas são atendidas.

# Se (if) - verifica SE x condições atendem os requisitos.
# Então (else) - Caso não atendam o requisito, então y acontece
# Se, Então (elif) - Estende o bloco de controle

# Somente o primeiro bloco cuja condição for verdadeira será executado

x = int(input("Informe um valor para x: "))
y = int(input("Informe um valor para y: "))

if y > x:
    print(f"{y} é maior que {x}")
elif x == y:
    print("Ambos os valores são iguais")
else:
    print(f"{y} não é maior que {x}")

# aninhamento de estruturas condicionais 
# É uma estrutura condicional dentro de outra estrutura condicional

# if ternário - é uma verificação inline, onde verifica uma condição e realiza uma operação dependendo do resultado

saldo = 500
saque = 250
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")