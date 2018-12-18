tupla = tuple()
tupla = ()

print(type(tupla))

tupla = ('um',)
print(type(tupla))
print(tupla[0])

#
cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))
