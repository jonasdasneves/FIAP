#Define o preço de cada material
caneta = 2.00
lapis = 1.50
caderno = 5.00

#pergunta quantos itens foram comprados
qtd_caneta = int(input('Quantas canetas você comprou?'))
qtd_lapis = int(input('Quantos lápis você comprou?'))
qtd_caderno = int(input('Quantos cadernos você comprou?'))

#Aplica desconto e soma os valores
print(f'O valor total da sua compra é de R${(((caneta*qtd_caneta)*0.95)+((caderno*qtd_caderno)*0.8)+(qtd_lapis*lapis)):.2f}')