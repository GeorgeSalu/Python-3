# Desafio Operadores Logicos

# Os Trabalhadores
trabalho_terca = True
trabalho_quinta = False

"""
- Confirmando os 2 : Tv 50' + sorvete
- Confirmando apenas 1 : Tv 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudavel={}".format(
    tv_50, tv_32, sorvete, mais_saudavel))
