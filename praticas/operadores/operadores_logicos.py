# utilizados em conjunto com operadores de comparação para montar uma expressão lógicas, retorna um bool (true/false)

# operador E (and): ambas as condições precisam ser verdadeira para retornar verdadeiro, para ser falso, basta um falso

num1, num2, num3 = 2, 4, 8

print(f"{num1} é menor que (<) {num2} E {num3} é maior que (>) {num2}?")
print(num1 < num2 and num3 > num2)

# operador OU (or): é verdadeiro se uma ou mais condições são verdadeiras, e é falso se todas forem falsas

print(f"\n{num1} é maior que (>) {num3} OU {num3} é igual (==) {num3} ")
print(num1 > num3 or num3 == num3)

# operador NÃO (not): é responsável por negar a afirmação, ou seja, not true = false
print("\nNão é verdade: not true")
print(not True)

print("\nÉ verdade: not false")
print(not False)

# A precêdencia é:
# 1. E - and
# 2. Ou - or
# 3. Não - not
# parênteses alteram a ordem de precêdencia

# é possível armazenar o resultado de operações lógicas em variáveis