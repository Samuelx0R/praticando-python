# identação: forma de manter o código mais legível e manutenível.
# Além de que no python, serve para delimitar o final do bloco de comando
# : - inicia um bloco, ' ' termina um bloco

def sacar(valor, saldo):
    
        if saldo >= valor:
            print(f"\nvalor sacado: {valor}")
            saldo -= valor
            return saldo
        
        print("saldo insuficiente!")
        return saldo 
        
saldo = 500
print(f"saldo atual: {saldo}")

valor = int(input("Escolha um valor: "))
saldo_final = sacar(valor, saldo)

print(f"saldo atual: {saldo_final}")