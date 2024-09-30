#Pergunta um número
num = int(input('Digite um número inteiro'))

#printa a sequencia
for n in range(1,num+1):
    print(n,'/',(n*2)-1)