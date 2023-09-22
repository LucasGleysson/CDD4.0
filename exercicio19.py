print('Digite a quantidade de tempo que pretende ser passada: ')
hora01 = int(input('Horas: '))
minutos01 = int(input('Minutos: '))

print('Digite o horario de entrada: ')
hora02 = int(input('Horas: '))
minutos02 = int(input('Minutos: '))

hora_final = hora01 + hora02
minuto_final = minutos01 + minutos02

if minuto_final >= 60:
    hora_final += 1
    minuto_final -= 60

if hora_final > 24:
    hora_final -= 24

formato = 'AM'
if hora_final >= 12:
    formato = 'PM'

if hora_final >= 13:
    hora_final -= 12



print(f'Tempo de saida: {hora_final}:{minuto_final:02}{formato}')
