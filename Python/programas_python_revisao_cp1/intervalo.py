soma = 0

#Pede 10 valores
for i in range(1,11):
    num = int(input(f'Digite o {i}° valor'))

    #Verifica se o valor está entre 10 e 20
    if num >= 10 and num <= 20:
        soma += 1

print(f'Dos valores que você digitou, {soma} estão entre 10 e 20')
