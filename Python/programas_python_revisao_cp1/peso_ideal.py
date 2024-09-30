#Solicita o sexo e peso da pessoa e verifica se a resposta é valida
sexo = input("Qual é o seu sexo(M/F)")
while sexo != 'M' and sexo != 'F':
    print('Digite um sexo válido')
    sexo = input("Qual é o seu sexo(M/F)")

altura = float(input('Qual é a sua altura?'))

if sexo == 'M':
    print(f'Seu peso ideal é de {((72.7*altura)-58):.2f}kg')

else:
    print(f'Seu peso ideal é de {((62.1*altura)-44.7):.2f}kg')

