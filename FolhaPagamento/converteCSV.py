#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import string
import os

def SeparaCampos(s):
    # Os campos estão separados por muitos espaços. Precisamos trocar estas
    # cadeias de espaços por uma vírgula. As linhas já terminam com \n

    resposta = ''
    estado = 0
    for letra in s:
        if estado == 0:
            if letra != ' ': # está no meio de uma string
                resposta += letra
            elif letra == ' ': # não sei se é separador de palavras ou não
                estado = 1
        elif estado == 1:
            if letra != ' ': # foi espaço separador de palavras
                resposta += ' ' + letra
                estado = 0
            elif letra == ' ': # sequencia de espaços
                resposta += ','
                estado = 2
        elif estado == 2:
            if letra != ' ': # terminou a sequencia de espaços
                resposta += letra
                estado = 0
    return resposta


def ConvertePDF2CSV(pdf):
    # Só precisamos processar as linhas que comecem com 1 espaço

    txt = string.replace(pdf, '.pdf', '.txt')
    csv = string.replace(pdf, '.pdf', '.csv')
    os.system('pdftotext -layout ' + pdf)
    entrada = open(txt).readlines()
    saida = open(csv, 'wt')

    dados = filter(lambda x: (x[0] == ' ') and (x[1] != ' '), entrada)
    resultado = []
    for linha in dados:
        resultado.append(SeparaCampos(string.replace(linha[1:], ',', '.')))

    saida.writelines(resultado)
    return

if len(sys.argv) == 2:
    ConvertePDF2CSV(sys.argv[1])
