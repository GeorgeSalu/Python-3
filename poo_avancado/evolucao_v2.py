class Humano:
    # atributo da classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'

    @staticmethod
    def especies():
        adjetivos = ('Habilitis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopitecos',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('jose')
    gronk = Neanderthal('gronck')

    print(
        f'Evolução (a partir da classe ): {", ".join(HomoSapiens.especies())}')
