#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import string
import os

def RemoveRodape(lista):
    for i in range(0, len(lista)):
        if 'IMPRENSA OFICIAL DO ESTADO SA' in lista[i]:
            return lista[:i-1]
    return lista

def RemoveCabecalho(lista):
    if len(lista) > 10:
        for i in range(0, 10):
            if 'www.imprensaoficial.com.br' in lista[i]:
                return lista[i+1:]
        for i in range(0, 10):
            if 'rio Oficial' in lista[i]:
                return lista[i+1:]
    return lista

def ConvertePDF2TXT(pdf):
    txt = string.replace(pdf, '.pdf', '.txt')

    # Converte o PDF em txt, provavelmente multicolunas
    os.system('pdftotext -layout ' + pdf)

    # Lê o arquivo sem os cabeçalhos e sem o fim de linha
    conteudo = map(lambda x: x[:-1], RemoveRodape(RemoveCabecalho(list(open(txt).readlines()))))

    maximo = max(map(lambda x: len(x), conteudo))
    espacos = [0] * maximo

    # Conta os espaços verticalmente, para descobrir as divisões de colunas
    for linha in conteudo:
        for i in range(0, maximo):
            if i < len(linha):
                espacos[i] += 1 if linha[i] == ' ' else 0
            else:
                espacos[i] += 1

    # Localiza as divisões de colunas e delimita cada uma delas
    separador = len(conteudo)
    colunas = []
    anterior = 0
    for i in range(0, len(espacos)):
        if espacos[i] >= separador - 3:
            if anterior < i - 1:
                colunas.append((anterior, i))
            anterior = i + 1
    if anterior < len(espacos):
        colunas.append((anterior, len(espacos)))

    # Extrai o texto de cada coluna, removendo colunas em branco
    saida = []
    for (inicio, fim) in colunas:
        ultima = ''
        for linha in conteudo:
            atual = linha[inicio:fim].rstrip()
            if len(atual) != 0:
                saida.append(atual)

    arquivoSaida = open(txt, 'wt')
    for linha in saida:
        arquivoSaida.write(linha + '\n')
    arquivoSaida.close()

if len(sys.argv) > 1:
    for arquivo in sys.argv[1:]:
        print 'Convertendo', arquivo, '...'
        ConvertePDF2TXT(arquivo)
