produto = {'nome': 'Caneta chic', 'preco': 14.90,
           'importada': True, 'estoque': 889}

for chave in produto:
    print(chave)


for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)
