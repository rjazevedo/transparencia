#!/usr/bin/python
# -*- coding: utf-8 -*-

import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
import csv
import codecs
import sys
import os
import pickle

def CreateBrowser():

    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
#    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Want debugging messages?
#    br.set_debug_http(True)
#    br.set_debug_redirects(True)
#    br.set_debug_responses(True)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    return br

def BuscaDados(br, matricula):

    print matricula,
    br.open('http://www.siarh.unicamp.br/consultaFuncionario/action/ConsultaFuncionario?nome=&local=&matricula=' + matricula)
    soup = BeautifulSoup(br.response().read(),convertEntities=BeautifulSoup.HTML_ENTITIES)
    table = soup.fetch(name="table")
    tr = table[3].fetch(name="tr")
    td = tr[1].fetch(name='td')

    nome = td[0].text
    matr = td[1].text
    ramal = td[2].text
    local = td[3].text

    print nome
    return [nome, matr, ramal, local]


br = CreateBrowser()
matriculas = list(csv.reader(open('matriculas.csv')))
processados = {}
multiplo = 0

if (os.path.isfile('completo.pickle')):
    processados = pickle.load(open('completo.pickle', 'rb'))
    pickle.dump(processados, open('completo.pickle.old', 'wb'))

for funcionario in matriculas:
    if (funcionario[0] in processados):
        funcionario = processados[funcionario[0]]
        print funcionario[0]
    else:
        dados = ['', '', '', '']
        try:
            dados = BuscaDados(br, funcionario[0])
        except IndexError:
            print 'Falhou...'
        else:
            funcionario.extend(dados)
            processados[funcionario[0]] = funcionario
            multiplo += 1
            if (multiplo == 10):
                pickle.dump(processados, open('completo.pickle', 'wb'))
                multiplo = 0



