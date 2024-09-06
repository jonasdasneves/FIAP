#Pede a altura da pessoa
altura = float(input('Qual é a sua altura?'))

#Pede o peso da pessoa
peso = float(input('Quanto você pesa?'))

#Calcula e mostra o IMC
print(f'Seu IMC(Índice de massa corporal) é {peso//(altura**2)}')