#Programa para calcular a média de 3 notas digitadas pelo usuário

checkpoint1 = float(input('Digite a npota do checkpoint 1: '))
checkpoint2 = float(input('Digite a npota do checkpoint 2: '))
checkpoint3 = float(input('Digite a npota do checkpoint 3: '))

media = (checkpoint1+checkpoint2+checkpoint3)/3
print(f'A média do aluno é {media:.2f}')