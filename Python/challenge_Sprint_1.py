#Menu para totem - Dá uma explicação rápida do funcionamento para o usuário
print('CCR Totem\n Para navegar, digite valores correspondentes à sua resposta \n To navigate, tipe values according to your answer\n')
    
#Definição de dicionários para expor opções:

#Este programa é um protótipo com escala reduzida para demonstração - considerando apenas o escopo da linha 9 esmeralda e suas estações
estacoes_linha_9 = {
    1 : "Osasco",
    2 : "Presidente Altino",
    3 : "Ceasa",
    4 : "Villa Lobos-Jaguaré",
    5 : "Cidade Universitária",
    6 : "Pinheiros",
    7 : "Hebraica - Rebouças",
    8 : "Cidade Jardim",
    9 : "Vila Olímpia",
    10 : "Berrini",
    11 : "Morumbi - Claro",
    12 : "Granja Julieta",
    13 : "João dias",
    14 : "Santo Amaro",
    15 : "Socorro",
    16 : "Jurubatuba",
    17 : "Autódromo",
    18 : "Primavera - Interlagos",
    19 : "Grajaú",
    20 : "Bruno Covas - Mendes - Vila Natal",

}

# dicionários contendo alguns pontos de interesse gerais em português 
servicos = {
    1 : 'Atendimento Médico',
    2 : 'restaurante',
    3 : 'farmácia',
    4 : 'Mercado',
    5 : 'Shopping',
    6 : 'Me recomende um ponto turístico'
}

# dicionários contendo alguns pontos de interesse gerais em inglês 
services = {
    1 : 'Atendimento Médico',
    2 : 'restaurante',
    3 : 'farmácia',
    4 : 'Market',
    5 : 'Mall',
    6 : 'Recommend me a touristical point'
}

#Definição de funções:

#Definição de idioma
def selecao_idioma():
    #Inicia perguntando o idioma a ser utilizado
    idioma = int(input('\nPrimeiro, escolha seu idioma! \nFirst, choose your language! \n 1 - Português \n 2 - English\n'))

    #Verifica se o valor é valido e evita erros
    match idioma:
        case 1:
            idioma = 'pt-br'
            return idioma

        case 2:
            idioma = 'en'
            return idioma

        case _:
            print('insira um valor válido')
            selecao_idioma()

#Função onde o usuário escolherá o que precisa
def intencao(idioma):
    funcao = int(input('\nVocê está na estação Santo Amaro! Como posso te ajudar hoje? \n 1 - Traçar Rotas \n 2 - Pontos de interesse \n 3 - Tire dúvidas com o Tótis'))

    
    
    match funcao:
        case 1:
            
            print('\nA qual estacao da linha 9 esmeralda você quer ir?\n')
            lista = list(estacoes_linha_9.items())
            destino = 1
            for estacoes in range(len(lista)-1):
                print(lista[estacoes])

            destino = int(input(lista[19]))
            estacao(destino,idioma)

        case _:

            funcao = int(input('\nVocê está na estação Santo Amaro! Como posso te ajudar hoje? \n 1 - Traçar Rotas \n 2 - Pontos de interesse \n 3 - Converse com o Tótis!\n'))

def estacao(destino, idioma):

    if destino > 14 and destino <= 20:
        sentido = estacoes_linha_9[20]
        trajeto = destino - 14

        if idioma == 'pt-br':
            print(f'\nPara chegar à estação {estacoes_linha_9[destino]}, você deve pegar o trem no sentido {sentido} e viajar por {trajeto} estações!\n')
        
    elif destino > 0 and destino < 14:
        sentido = estacoes_linha_9[1]
        trajeto = 14 - destino

        if idioma == 'pt-br':
            print(f'\nPara chegar à estação {estacoes_linha_9[destino]}, você deve pegar o trem no sentido {sentido} e viajar por {trajeto} estações!\n')


    elif destino == 14:
        print('\nVocê já está na estação Santo Amaro!\n')
        intencao(idioma)

    else:
        print('\ndigite um valor válido\n')
        intencao(idioma)

def pontos_interesse(idioma):
    interesse = int(input('\nQue tipo de serviço você procura?\n'))


#Inicia perguntando o idioma a ser utilizado
idioma = selecao_idioma()

#Chama a função intenção
intencao(idioma)







    

            
            

            



