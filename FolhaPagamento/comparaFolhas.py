#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import csv
import string

# Campos do CSV: matricula, nome, remuneração bruta, indenizações, redutor,
# descontos legais, remuneração líquida

def Salario(pessoa):
    return float(pessoa[2]) + float(pessoa[3]) - float(pessoa[4])


def Compara(inicio, fim):
    sairam = 0
    entraram = 0
    movimentos = {}
    for pessoa in inicio.keys():
        if pessoa not in fim:
            sairam += 1
        else:
            si = Salario(inicio[pessoa])
            sf = Salario(fim[pessoa])
            porcentagem = int((sf / si - 1.0) * 100)
            [quantidade, valor] = movimentos.get(porcentagem, (0, 0.0))
            movimentos[porcentagem] =  [quantidade + 1, valor + sf - si]

    for pessoa in fim.keys():
        if pessoa not in inicio:
            entraram += 1

    resposta = [['Entraram', entraram], ['Sairam', sairam], ['Movimentos']]
    mov = movimentos.keys()
    mov.sort()
    for i in mov:
        linha = [i, movimentos[i][0], round(movimentos[i][1], 2)]
        resposta.append(linha)

    return resposta

def GeraDicionario(lista):
    resposta = {}
    for linha in lista:
        resposta[linha[0]] = linha

    return resposta

if (len(sys.argv) > 2):
    ordem = sys.argv[1:]
    folhas = {}

    for arquivo in sys.argv[1:]:
        print 'Lendo folha', arquivo, '->',
        folhas[arquivo] = GeraDicionario(list(csv.reader(open(arquivo))))
        print len(folhas[arquivo]), 'registros lidos'

    for f in range(0, len(ordem) - 1):
        print '****', ordem[f], 'vs', ordem[f+1]
        resultado = Compara(folhas[ordem[f]], folhas[ordem[f + 1]])
        saida = csv.writer(open('comparacao-' + string.replace(ordem[f], '.csv', '') + '-' + ordem[f+1], 'wt'))
        saida.writerows(resultado)
