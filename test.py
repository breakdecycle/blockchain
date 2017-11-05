import requests
from flask import Flask, jsonify, request

regURL = 'http://localhost:5000/nodes/register'

chainURL = 'http://localhost:5000/chain'

balURL = 'http://localhost:5000/getbalance'

mineURL = 'http://localhost:5000/mine'

tranURL = 'http://localhost:5000/transactions/new'

conURL = 'http://6c7892c2.ngrok.io/nodes/resolve'

nodes = {"nodes": ['https://411d4537.ngrok.io/']}

transaction = {"sender":'1PSXQuHixWq9RL1xHDd23wKmBsWG3Fadmh', "pkey": '47e4453c900a8670ea540b2751775e13108466639585de6f09dcf2bc491318f3', "recipient":'16wzkTwnZHefubyQbWECnR8P3PeT42PngV', "amount" : 2}

tranR = requests.post(tranURL, json=transaction)
print(tranR.json())

# regR = requests.post(regURL,json=nodes)
# print(regR.json())

for i in range(5):
	r = requests.get(mineURL)
	print(r.content)

key = {'pkey': '1PSXQuHixWq9RL1xHDd23wKmBsWG3Fadmh'}
balR = requests.post(balURL, json = key)
# print(balR.json())
# chainR = requests.get(chainURL)

# print('length of chain is {}'.format(len(chainR.json()['chain'])))

# print(chainR.json()['chain'])

# conR = requests.get(conURL)

# print(conR.json())