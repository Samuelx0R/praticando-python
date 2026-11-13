# serve para agrupar um conjunto de instruções reutilizáveis 
# def -> palavra reservada que indica criação de uma função
# em seguida vem o nome da função junto dos parenteses onde ficam os paramêtros, def nome(paramêtros)
# funções também seguem o mesmo padrão de iniciar com : e identenção
# os paramêtros funcionam como localizadores para as funções acessarem determinadas variáveis
# para utilizar uma função declarada, é necessário "invocá-la", chamando seu nome no código e passando as variáveis que seram utilizadas como paramêtros

def calcular_faturamento(qtd_vendida, preco): # declarando a função + parametros
    faturamento = qtd_vendida * preco
    print(faturamento)

calcular_faturamento(2, 10)                   # chamada da função + valores para os paramêtros

# print != return
# print -> o resultado da função é diretamente exibída
# return -> a função retorna um resultado para a atribuição, ela é armazenada numa variável
