class Humano:
    # atributo da classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

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
    jose.idade = 40

    print(f'Nome : {jose.nome} idade: {jose.idade}')
