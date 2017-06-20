# Conjunto de ferramentas para trabalhar com Transparência de Dados

O foco original deste projeto é trabalhar com os dados da Unicamp que já estão disponíveis publicamente de alguma forma. Em particular, começamos com 3 fontes de dados:

* **Diário Oficial do Estado de São Paulo**: Contém os relatos, em PDF, dos atos emitidos por todos os órgãos paulistas, incluindo a Unicamp. No momento temos um crawler básico das edições em PDF e um conversor de PDF para txt.

* **Folha de Pagamento**: Contém um conversor do relatório de folha de pagamento fornecido pela Unicamp em PDF na página https://www.unicamp.br/unicamp/informacao/remuneracao-unicamp para CSV. Contém uma versão preliminar de análise do fluxo de pessoas entrando e saindo da folha de pagamento entre dois meses.

* **SIAFEM**: É o sistema integrado de prestações de contas do Estado de São Paulo, acessível via webservices. Esta pasta está sem código no momento mas terá uma documentação de exemplo do uso do webservice e ferramentas para analisar os dados. 

# Pacotes de Python que podem ser úteis

- Natural Language Toolkit: <http://www.nltk.org>

- Python Data Analysis Library: <http://pandas.pydata.org>

- Altair declarative statistical visualization: <https://github.com/altair-viz/altair>

- SOAP/WSDL client: <http://www.diveintopython.net/soap_web_services/index.html>

- Python e PDF: <https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167> e <https://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text>
