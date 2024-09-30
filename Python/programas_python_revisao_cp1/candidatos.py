import random

n_eleitores = int(input('Há quantos eleitores nessa cidade?'))
candidato1 = 0
candidato2 = 0
candidato3 = 0

#Pergunta o número total de eleitores
for i in range(n_eleitores):
    voto = random.randrange(1,4)
    match voto:
        case 1:
            candidato1 += 1
        case 2:
            candidato2 += 1
        case 3:
            candidato3 += 1

print(f'{candidato1} pessoas votaram no candidato 1, {candidato2} votaram no candidato 2 e {candidato3} votaram no candidato 3!')