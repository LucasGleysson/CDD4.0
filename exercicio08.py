time1 = input('Digite o nome do time: ')
gols1 = int(input('Digite a quantidade de gols desse time: '))

time2 = input('Digite o nome do outro time: ')
gols2 = int(input('Digite a quantidade de gols desse time: '))

vencedor = 0
if gols1 == gols2:
    print('Houve um EMPATE')
else:
    if gols1 > gols2:
        vencedor = time1
    else:
        vencedor = time2
    print(vencedor, 'é o VENCEDOR!')


