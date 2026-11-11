# utilizado para comparar algumas situações, retorna verdadeiro ou falso (bool)

# 1. verificar igualdade -> ==
# 2. verificar diferença -> !=
# 3. verificar maior que -> >
# 4. verificar maior igual que -> >=
# 5. verificar menor que -> <
# 6. verificar menor igual que -> <=

num1 = 10
num2 = 5

print(f"{num1} é igual a {num2}?")
print(num1 == num2)

print(f"\n{num1} é diferente de {num2}?")
print(num1 != num2)

print(f"\n{num1} é maior que {num2}?")
print(num1 > num2)

print(f"\n{num2} é maior que {num1}?")
print(num2 > num1)

print(f"\n{num1} é maior ou igual que {num2}?")
print(num1 > num2)

print(f"\n{num2} é maior ou igual que {num1}?")
print(num2 > num1)

print(f"\n{num1} é menor que {num2}?")
print(num1 < num2)

print(f"\n{num2} é menor que {num1}?")
print(num2 < num1)

print(f"\n{num1} é menor ou igual que {num2}?")
print(num1 <= num2)

print(f"\n{num2} é menor ou igual que {num1}?")
print(num2 <= num1)
