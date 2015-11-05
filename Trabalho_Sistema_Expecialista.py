from pyswip import Prolog, Query, Variable, Functor
import os
import sys

class Trabalho_Sistema_Expecialista():

    def __init__(self):
        self.prolog = Prolog()
        self.X = Variable()
        self.resultado = ['corinthians', 'atletico_mg', 'gremio', 'santos', 'sao_paulo', 'palmeiras', 'flamengo', 'internacional', 'ponte_preta', 'sport', 'fluminense', 'atletico_pr', 'cruzeiro', 'chapecoense', 'figueirense', 'avai', 'coritiba', 'goias', 'vasco', 'joinville', 'botafogo']

        arquivo_pl = open('jogos.pl')
        for linha in arquivo_pl.readlines():
            if linha[len(linha) - 1] == '\n':
                linha = linha.replace("\n", "")
            self.prolog.assertz(linha)

    def Imprimir_Resultados(self):
        os.system('clear')
        if len(self.resultado) == 1:
            print("O esporte que você está pensando é :\n")
            for resultado in self.resultado:
                print(resultado, '\n')
            sys.exit(0)
        # else:
        #     print('''
        #         Não consegui achar o esporte mas acho 
        #         que ele está nessa lista. Não está?
        #         ''')
        #     for resultado in self.resultado:
        #         print(resultado)

    def Imprimir(self, lista):
        for esporte in lista:
            print(esporte)

    def Tamanho(self):
        print(len(self.resultado))

    def Query(self, parametro):
        lista = []
        parametro = Functor(parametro)
        query = Query(parametro(self.X))
        while query.nextSolution():
            lista.append(str(self.X.get_value()))
        query.closeQuery()

        return lista

    def Intersection(self, lista1):
        if set(lista1).intersection(self.resultado) == set():
            self.resultado = lista1
        else:
            self.resultado = set(lista1).intersection(self.resultado)
                
    def Difference(self, lista1):
        Times = set(self.resultado)
        if Times.difference(lista1) == set():
            self.resultado = lista1
        else:
            self.resultado = Times.difference(lista1)

    def Pergunta(self, pergunta, caracteristica):
        resp = input(pergunta + '\n')
        Times = self.Query(caracteristica)
        if (resp == 's' or resp == 'S'):
            self.Intersection(Times)
            return True
        else:
            self.Difference(Times)
            return False