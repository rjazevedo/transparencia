#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import datetime
import bz2
import os
import time
import sys

#Para PDF, olhar http://www.unixuser.org/~euske/python/pdfminer/

class CrawlerDOSP:
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    cadernos = ['exec1'] #, 'exec2', 'legislativo']

    def __init__(self, inicio, final, espera = 0):
        self.inicio = inicio
        self.final = final
        self.espera = espera
        return

    def MontaURL(self, caderno, ano, mes, dia, pagina):
        return 'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/%d/%s/%02d/%s/pdf/pg_%04d.pdf' % (ano, self.meses[mes - 1], dia, caderno, pagina)

    def CriaDir(self, listaDiretorios):
        caminho = ''
        for diretorio in listaDiretorios:
            caminho = os.path.join(caminho, diretorio)
            if (not os.path.isdir(caminho)):
                os.mkdir(caminho)

    def MontaNome(self, caderno, ano, mes, dia, pagina):
        return 'content/%d/%s/%d/%s/pg_%04d.pdf.bz2' % (ano, mes, dia, caderno, pagina)

    def Download(self):
        passo = datetime.timedelta(1)
        data = self.inicio
        downloader = urllib.FancyURLopener()

        while (data <= self.final):
            print data
            sys.stdout.flush()

            for caderno in self.cadernos:
                print ' - %s ' % (caderno),
                self.CriaDir(['content', str(data.year), str(data.month), str(data.day), caderno])

                for pagina in range(1,9999):
                    url = self.MontaURL(caderno, data.year, data.month, data.day, pagina)
                    nomeArquivo = self.MontaNome(caderno, data.year, data.month, data.day, pagina)
                    funcionou = True
                    try:
                        if (os.path.isfile(nomeArquivo)):
                            continue

                        entrada = downloader.open(url)
                        dado = entrada.read()
                        if (dado[0:4] == '%PDF'):
                            saida = bz2.BZ2File(nomeArquivo, 'w')
                            saida.write(dado)
                            saida.close()
                            print '\b.',
                            sys.stdout.flush()
                        else:
                            print '-> %d páginas.' % (pagina - 1)
                            break

                    except IOError:
                        funcionou = False

                    if (not funcionou):
                        break

                    time.sleep(self.espera)

            data = data + passo

c = CrawlerDOSP(datetime.date(2017,6,1), datetime.date(2017,6,20))

c.Download()
