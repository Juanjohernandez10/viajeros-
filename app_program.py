list_viajero=[]

import os

def fnt_limpiar ():
    os.system('cls')
    print('AUTOR: juan jose hernandez ')

def fnt_agente (opcion):
    fnt_limpiar()
    global sw 
    if opcion =='1':
        fnt_limpiar()
        print('agregar viajero \n->')
        viajero = ' '
        nombre = input('Nombre-> ')
        apellido = input('apellido-> ')
        edad = input('edad-> ')
        if (int(edad)) >= 0 and (int(edad) <= 25):
            viajero = nombre + ' ' + apellido + ' ' + edad + ''
            list_viajero.append(viajero)
            print('viajero agregado correctamente \n')
            enter = input('enter para continuar <ENTER>')
        else:
            print('no cuentas con la edad suficiente \n')
            enter = input('enter para continuar <ENTER>')
    
    elif opcion == '2':
        print (' mostrar viajeros ')
        if len(list_viajero) == 0:
            print('no hay viajeros registrados ')
            input ( 'presiones enter para continuar <ENTER>')   
        else:
            for viajero in list_viajero:
                print( viajero )
            input ( 'presione enter para continuar <ENTER>')
    elif opcion == '3':
        sw = False
    
sw = True

while sw == True:
    fnt_limpiar ()
    opcion = input(' menu principal \n1. agregar \n2. mostrar \n3.salir \n -> ')
    fnt_agente(opcion)
        
    