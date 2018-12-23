palavra = 'paralelepipedo'

for letra in palavra:
    print(letra)


aprovados = ['rafaela', 'pedro', 'renato', 'maria']
for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    print('{} {}'.format(posicao, nome))

dias_da_semana = ('Domingo', 'Segunda', 'Terca',
                  'Quarta', 'Quinta', 'Sexta', 'Sabado')

for dia in dias_da_semana:
    print('Hoje e {}'.format(dia))
