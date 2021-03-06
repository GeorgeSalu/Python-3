from math import pi
import sys


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
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do circulo ', area)
