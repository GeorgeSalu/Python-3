class Humano:
    # atributo da classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'


if __name__ == '__main__':
    jose = Humano('jose')
    grokn = Humano('Grock')
    grokn.das_cavernas()

    print(f'Humano.especie: {Humano.especie} ')
    print(f'Jose.especie: {jose.especie} ')
    print(f'Grock.especie: {grokn.especie} ')
