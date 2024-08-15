import requests
import json
import matplotlib.pyplot as plt

## API COTAÇÃO MOEDAS

# cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')  #acessar api através do link
# cotacao_dict = cotacao.json()  #converter em dicionário 
# print(cotacao_dict)


# acessar informações do dicionario
# print('Dolar = {}'.format(cotacao_dict['USDBRL']['bid']))
# print('Euro = {}'.format(cotacao_dict['EURBRL']['bid']))
# print('Bitcoin = {}'.format(cotacao_dict['BTCBRL']['bid']))


# retornar histórico dos ultimos x dias da cotação do dólar
# cotação30 = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
# dict30 = cotação30.json()

# for i, bids in enumerate(dict30):  #por loop for
#     print('Dia {} = {}'.format(i,dict30[i]['bid']))

# lista = [float(bids['bid']) for bids in dict30]  #por list comprehension
# print(lista)


# retornar histórico da cotação entre datas específicas
# cotação_date = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/50?start_date=20230101&end_date=20240101')
# dict_date = cotação_date.json()
# lista = [bids['bid'] for bids in dict_date]
# lista.reverse()
# print(lista)

# plt.figure(figsize=(15,5))
# plt.plot(lista)
# plt.show()


## API ENVIO SMS - TWILIO
# from twilio.rest import Client

# sid = 'AC33b2c2b0cfb51c52514566b9c18968b5'
# token = '5f3fbe9bbcf6530c3c5d517eb61d1e50'

# login = Client(sid,token)

# remetente = '+14158309518'
# destino = '+5521973679134'

# message = login.messages.create(
#     to=destino,
#     from_=remetente,
#     body='Fala, marreco'
# )

# print('check')