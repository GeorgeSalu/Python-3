from math import pi
import sys
import errno

ERRO = '\033[91m'
NORMAL = '\033[0m'


def help():
    print("""
        E necessario informar o raio do circulo
        Sintaxe: {} <raio>
        """.format(sys.argv[0]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)

    if not sys.argv[1].isnumeric():
        help()
        print(ERRO, 'O raio deve ser um valor numerico', NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo ', area)
