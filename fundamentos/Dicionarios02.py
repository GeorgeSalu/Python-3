pessoa = {'nome': 'Prof Alberto', 'idade': 43, 'cursos': ['react', 'python']}
pessoa['idade'] = 44
pessoa['cursos'].append('angular')

print(pessoa)
print(pessoa.pop('idade'))
print(pessoa)

pessoa.update({'idade': 40, 'sexo': 'M'})

print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)
