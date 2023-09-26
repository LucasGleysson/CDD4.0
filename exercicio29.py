print('-'*35)
lista_compras = ['banana', 'laranja', 'maça']
for i in lista_compras:
    print(i)

print('-'*35)
lista_compras.append('carro')
for i in lista_compras:
    print(i)

print('-'*35)
lista_compras.insert(1, 'carro')
for i in lista_compras:
    print(i)

print('-'*35)
del lista_compras[3]
for n in lista_compras:
    print(n)

print('-'*35)
item = lista_compras.pop(-1)
print(item)
