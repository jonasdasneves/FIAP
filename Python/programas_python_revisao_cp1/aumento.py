#Pergunta o salário do funcionário
salario = float(input('Qual é o salário do funcionário?'))

#Define o aumento
if salario <= 280:
    aumento = 0.2
elif salario <= 700:
    aumento = 0.15
elif salario <= 1500:
    aumento = 0.1
else:
    aumento = 0.05

print(f'O aumento desse funcionário será de {aumento*100}%, totalizando R${salario+(salario*aumento)}')