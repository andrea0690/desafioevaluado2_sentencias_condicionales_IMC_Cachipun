import random

jugador_1 = input('Ingrese la opcion "PIEDRA, PAPEL ó TIJERA": ')
jugador_1 = jugador_1.lower()

if jugador_1 != 'piedra' and jugador_1 != 'papel' and jugador_1 != 'tijera':
    print('Argumento invalido: debe ser piedra, papel o tijera')
else:
    computador = random.choice(['piedra', 'papel','tijera'])
    
    print(f'Tu jugaste {jugador_1}')
    print(f'Computador jugó {computador}')
    
    if jugador_1 == computador:
        print("Empate!!")
    elif (jugador_1 == 'piedra' and computador == 'tijera') or (jugador_1 == 'papel' and computador == 'piedra') or (jugador_1 == 'tijera' and computador == 'papel'):
        print("Ganaste!!")
    else:
        print("Perdiste!!")

    
        



