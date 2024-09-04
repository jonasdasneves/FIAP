#Pergunta a nota de três matérias
mat = float(input('Qual foi a sua nota em matemática?'))
por = float(input('Qual foi a sua nota em português?'))
his = float(input('Qual foi a sua nota em história?'))

#Calcula e exibe a média aritmética das disciplinas
print(f'Sua nota média foi {((mat+por+his)/3):.2f}')