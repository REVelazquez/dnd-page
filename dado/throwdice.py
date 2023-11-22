from dice import dice

def throw_dice():
    print('Seleccione el dado: ')
    print('1. Dado de 6 caras')
    print('2. Dado de 8 caras')
    print('3. Dado de 10 caras')
    print('4. Dado de 20 caras')
    print('5. Dado de 100 caras')

    opcion = int(input('Ingrese el número correspondiente al dado que desea lanzar: '))
    opcion_valores={1:6, 2:8, 3:10, 4:20, 5:100}

    if opcion in opcion_valores :
        return opcion_valores[opcion]
    else:
        print ("Opción invalida. Por favor seleccione un número del 1 al 5")
        return throw_dice()

tipo_dado= throw_dice()
resultado= dice(tipo_dado)
print('El resultado del dado es: ', resultado)