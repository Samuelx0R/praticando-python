# inteiro para float
print("numero inteiro: ")
num = 10                  
print(num)                            # preco inteiro

print("numero convertido: utilizando float(var) ")
num01 = 10                                   
num01 = float(num01)                  # utilizando um construtor float
print(num01)            

print("numero convertido: utilizando divisao")
num02 = 10 / 2                        # divisao
print(num02)

# float para inteiro
print("\n")

print("numero float ")
num03 = 10.2
print(num03)

print("numero convertido: utilizando int(var) ")
num03 = int(num03)                      # utilizando um construtor int
print(num03)

print("numero convertido: utilizando divisao (//)")
num02 = 10 // 2                         # divisao
print(num02)

# numérico para string
print("\n")

idade = 21
texto = f"idade {idade}"    #Dá pra atribuir uma string para uma variável e com { } concatenar numérico na string
print(texto)

# string para numérico

idade_string = "21"
print(int(idade))           # Dá pra transformar direto ou atribuir