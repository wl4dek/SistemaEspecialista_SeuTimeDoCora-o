from Trabalho_Sistema_Expecialista import Trabalho_Sistema_Expecialista

print('''
    Vou tentar adivinhar qual o time que você torce. Mas para isso, 
    preciso que você me responda algumas perguntas que devem ser 
    respondidas com s(Sim) ou n(Não). Vamos lá? 
    ''')

TSE = Trabalho_Sistema_Expecialista()

if TSE.Pergunta('O seu time de coração é do SUL?', 'sul'):

    TSE.Pergunta('O time e de Santa Catarina?', 'sc')
    TSE.Imprimir_Resultados()
    
    TSE.Pergunta('Então o time possui a cor AZUL?', 'azul')
    TSE.Imprimir_Resultados()
    
else:
    
    if TSE.Pergunta('O seu time de coração é do SUDESTE?', 'sudeste'):
        if TSE.Pergunta('Seu time é PAULISTA?', 'sp'):

            if TSE.Pergunta('O time possue SOMENTE as cores PRETO e BRANCO no uniforme?', 'pretobranco'):
                TSE.Pergunta('Ex time do jogador Neymar?', 'neymar')
                TSE.Imprimir_Resultados()

                TSE.Pergunta('Possue uma das maiores torcidas dos Brasil?', 'maiortorcida')
                TSE.Imprimir_Resultados()
            else:
                TSE.Pergunta('O uniforme do time possui a cor VERDE?', 'verde')
                TSE.Imprimir_Resultados()
        else:
            if TSE.Pergunta('O time possue SOMENTE as cores PRETO e BRANCO no uniforme?', 'pretobranco'):
                TSE.Pergunta('O GARRINCHA jogou nesse time?', 'garrincha')
                TSE.Imprimir_Resultados()

            TSE.Pergunta('O time é Mineiro?', 'mg')
            TSE.Imprimir_Resultados()

TSE.Pergunta('O uniforme do time possui as cores VERMELHO e PRETO?', 'vermelhopreto')
TSE.Imprimir_Resultados()

TSE.Pergunta('O uniforme do time possui a cor VERDE?', 'verde')
TSE.Imprimir_Resultados()