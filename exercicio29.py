# Lista de frutas
print('-'*35)
lista_compras = ['banana', 'laranja', 'maça']
for i in lista_compras:
    print(i)

# Inserindo novo elemento no final
print('-'*35)
lista_compras.append('carro')
for i in lista_compras:
    print(i)

# Inserindo novo elemento em posição específica
print('-'*35)
lista_compras.insert(1, 'carro')
for i in lista_compras:
    print(i)

# Deletando um item pela posição
print('-'*35)
del lista_compras[3]
for n in lista_compras:
    print(n)

# Selecionando um item pela sua posição
print('-'*35)
item = lista_compras.pop(-1)
print(item)
