#Módulos importados
import requests
import json
from datetime import date, timedelta

#Variáveis para parâmetros GET
acao = ['bbas3', 'itsa4', 'ggbr4', 'mglu3', 'petr4']
url = 'https://www.alphavantage.co/query?'
func = 'TIME_SERIES_DAILY'
key = #'insira sua key aqui'

#Para cada item na lista 'Ação', vai repetir este loop.
for a in acao:
    print(a.upper())
    #Passa as variáveis GET.
    r = requests.get(f'{url}function={func}&symbol={a}.SA&apikey={key}')
    #Conta entre dois números, pulando de 28 em 28.
    for n in range(4,160,28):
        #Diminui o 'n' do dia de hoje, para pegar dados históricos.
        data = date.today() - timedelta(days = n)
        #Verifica se a data é sabado ou domingo, e diminui dias para que caiam na sexta-feira anterior
        if data.weekday() == 5:
            data = data - timedelta(days = 1)
        elif data.weekday() == 6:
            data = data - timedelta(days = 2)
        #Busca no arquivo JSON, a data e o valor de fechamento, quardando em 'Cotação'.
        cotacao = r.json()['Time Series (Daily)'][str(data)]['4. close']
        #Transforma a STR do JSON, para FLOAT.
        valor = float(cotacao)
        print(f'{data} -- R${valor:.2f}', end = '')
        print()
print("Fim")
