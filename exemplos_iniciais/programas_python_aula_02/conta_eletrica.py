#Solicita consumo elétrico em KWH
kwh = float(input('Qual é o seu consumo elétrico mensal em kw/h?'))

#Calcula conta de luz
print(f'Sua conta de luz é de R${(kwh*0.2):.2f}')