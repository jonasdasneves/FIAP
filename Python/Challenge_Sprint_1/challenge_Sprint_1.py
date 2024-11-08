    
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
    
    if idioma == 'pt-br':
        funcao = int(input('\nVocê está na estação Santo Amaro! Como posso te ajudar hoje? \n 1 - Traçar Rotas \n 2 - Pontos de interesse \n 3 - Tire dúvidas com o Tótis \n 4 - Encerrar programa'))

        match funcao:
            case 1:
                
                print('\nA qual estacao da linha 9 esmeralda você quer ir?\n')
                lista = list(estacoes_linha_9.items())
                destino = 1
                for estacoes in range(len(lista)-1):
                    print(lista[estacoes])

                destino = int(input(lista[19]))
                estacao(destino,idioma)

            case 2:
                print('\nO totem perguntará que tipo der serviço o cliente procura (mercados, farmacias, etc) e traçará uma rota para lá\n')

            case 3:
                print('\nO cliente poderá conversar com o chatbot Tótis, que pode responder perguntas, recomendar pontos turísticos, aceitar sugestões, etc.')

            case 4:
                termino_e_avaliacao(idioma)

            case _:

                intencao(idioma)
    else:  
        funcao = int(input('\nYou are at Santo Amaro station! How can I help you today? \n 1 - Trace routes \n 2 - Interest points \n 3 - Chat with Tótis!\n 4 - End program\n'))
                     
        match funcao:
            case 1:
                
                print('\nWhich line 9 emerald station are you going to?\n')
                lista = list(estacoes_linha_9.items())
                destino = 1
                for estacoes in range(len(lista)-1):
                    print(lista[estacoes])

                destino = int(input(lista[19]))
                estacao(destino,idioma)

            case 2:
                print('\nThe totem will ask what type of service the customer is looking for (markets, pharmacies, etc.) and trace a route there\n')

            case 3:
                print('\nThe customer will be able to talk to the Tótis chatbot, which can answer questions, recommend tourist attractions, accept suggestions, etc')

            case 4:
                termino_e_avaliacao(idioma)

            case _:

                intencao(idioma)

def estacao(destino, idioma):

    if destino > 14 and destino <= 20:
        sentido = estacoes_linha_9[20]
        trajeto = destino - 14

        if idioma == 'pt-br':
            print(f'\nPara chegar à estação {estacoes_linha_9[destino]}, você deve pegar o trem no sentido {sentido} e viajar por {trajeto} estações!\n')

        else:
            print(f'\nIn order to get to the {estacoes_linha_9[destino]} station, you need to get the train going to the {sentido} station and travel for {trajeto} stations!\n')
        
    elif destino > 0 and destino < 14:
        sentido = estacoes_linha_9[1]
        trajeto = 14 - destino

        if idioma == 'pt-br':
            print(f'\nPara chegar à estação {estacoes_linha_9[destino]}, você deve pegar o trem no sentido {sentido} e viajar por {trajeto} estações!\n')

        else:
            print(f'\nIn order to get to the {estacoes_linha_9[destino]} station, you need to get the train going to the {sentido} station and travel for {trajeto} stations!\n')


    elif destino == 14:
        if idioma == 'pt-br':
            print('\nVocê já está na estação Santo Amaro!\n')
            intencao(idioma)
        else:
            print('\nYou are at Santo Amaro station already\n')

    else:
        if idioma == 'pt-br':
            print('\ndigite um valor válido\n')
            intencao(idioma)
        else:
            print('\nTipe a valid valuey\n')

def termino_e_avaliacao(idioma):
    if idioma == 'pt-br':
        menu = int(input("Gostaria de deixar uma avaliação do serviço?\n0-Não\n1-Sim"))
        nota = 0
        match menu:
            case 0:
                pass
            case 1:
                while nota < 1 or nota > 5:
                    nota = int(input("Digite sua nota de 1 a 5 estrelas!"))
                    if nota > 0 and nota < 6:
                        print("Muito obrigado pela sua avaliação! Sua opinião é importante para nós!")
                    else:
                        print("Digite uma nota válida")
            case _:
                print("Digite uma opção válida")
                termino_e_avaliacao()

        print('\nObrigado por usar o Totem da Via mobilidade! Encerrando atendimento\n')
        return nota

    else:
        menu = int(input("Would you like to rate our service??\n0-No\n1-Yes"))
        nota = 0
        
        match menu:
            case 0:
                pass
            case 1:
                while nota < 1 or nota > 5:
                    nota = int(input("Type your rating from 1 to 5 stars!"))
                    if nota > 0 and nota < 6:
                        print("Thank you vert much for your rating! Your opinion is very important for us!")
                    else:
                        print("Type a valid rating")
            case _:
                print("Digite uma opção válida")
                termino_e_avaliacao()
        print('\nThank you for using the Totem Via Mobilidade! finalizing service\n')
        return nota

def main():
    #Função principal com loop
    while True:
        #Menu para totem - Dá uma explicação rápida do funcionamento para o usuário
        print('CCR Totem\n Para navegar, digite valores correspondentes à sua resposta \n To navigate, tipe values according to your answer\n')

        #Inicia perguntando o idioma a ser utilizado
        idioma = selecao_idioma()

        #Chama a função intenção
        intencao(idioma)

#Inicia função principal e loop
main()




    







    

            
            

            



