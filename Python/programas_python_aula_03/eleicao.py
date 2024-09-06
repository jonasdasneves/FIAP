#Votos em branco
branco = int(input('Quantos votos em branco foram contados?'))
#Votos nulos
nulo = int(input('Quantos votos nulos foram contados?'))
#Votos válidos
validos = int(input('Quantos votos válidos foram contados?'))

#Calcula e exibe a porcentagem de votos
pessoas = branco+nulo+validos
print(f'{((branco/pessoas)*100):.2f}% das pessoas votaram em branco')
print(f'{((nulo/pessoas)*100):.2f}% das pessoas votaram nulo')
print(f'{((validos/pessoas)*100):.2f}% das pessoas votaram em algum candidato')