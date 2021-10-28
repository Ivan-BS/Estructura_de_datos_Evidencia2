import csv
from collections import namedtuple
import datetime
import random
import pandas as pd
import os
SEPARADOR=('*'*50+'\n')

Ventas = {}
while os.path.exists('Ventas.csv') == True:
    valor=0
    leer_csv={}
    temp_dict={}
    temp_folio=[]
    temp_fecha=[]
    temp_descrip=[]
    temp_piezas=[]
    temp_precio=[]
    leer_csv = pd.read_csv('Ventas.csv', index_col=None).to_dict()
    #print(leer_csv)

    for key in leer_csv:
        if key == 'Folio':
            for key_dict in leer_csv[key]:
                temp_folio.append(leer_csv[key][key_dict])
        if key == 'Fecha':
            for key_dict in leer_csv[key]:
                temp_fecha.append(leer_csv[key][key_dict])
        if key == 'Descripcion':
            for key_dict in leer_csv[key]:
                temp_descrip.append(leer_csv[key][key_dict])
        if key == 'Piezas':
            for key_dict in leer_csv[key]:
                temp_piezas.append(leer_csv[key][key_dict])
        if key == 'PrecioVenta':
            for key_dict in leer_csv[key]:
                temp_precio.append(leer_csv[key][key_dict])

    zip_list=list(zip(temp_folio,temp_fecha,temp_descrip,temp_piezas,temp_precio))
    print(zip_list)
    key_actual=None
    lista_actual=[]
    for registro in zip_list:
        if registro[0] != key_actual:
            if len(lista_actual) > 0:
                Ventas[str(key_actual)]=lista_actual
            lista_actual=[]
            key_actual=registro[0]
            lista_actual.append(registro[1])
            articulo = namedtuple("articulo",("Descripcion","Piezas","Precioventa"))
            Venta=articulo(registro[2],registro[3],registro[4])
            lista_actual.append(Venta)
        else:
            articulo = namedtuple("articulo",("Descripcion","Piezas","Precioventa"))
            Venta=articulo(registro[2],registro[3],registro[4])
            lista_actual.append(Venta)

    Ventas[key_actual]=lista_actual
    print(Ventas)
    break


while True:
    print(SEPARADOR)
    print("MENÚ")
    print("1) Agregar datos")
    print("2) Consulta por folio")
    print("3) Consulta por fecha")
    print("4) Generar reporte de venta ")
    print("5) Salir")
    respuesta = int(input("Elija una opción: "))

    if respuesta == 1:
        articulo = namedtuple("articulo",("Descripcion","Piezas","Precioventa"))
        Articulos_venta = []
        print(SEPARADOR)
        clave = input('ingrese una clave:')
        print(clave)
        fecha= datetime.datetime.now()
        fecha=fecha.strftime('%d/%m/%Y')
        print(fecha)
        Articulos_venta.append(fecha)
        TOTAL=0
        while True:
            print(SEPARADOR)
            descripcion = input("Introduzca la descripcion del articulo:\n")

            print(SEPARADOR)
            cantidad = float(input("Ingrese la cantidad de piezas vendidas:\n"))

            print(SEPARADOR)
            precio = float(input("Ingrese el precio de venta:\n"))

            Venta=articulo(descripcion,cantidad,precio)
            TOTAL=TOTAL+precio*cantidad
            Articulos_venta.append(Venta)

            print(SEPARADOR)
            continuar = input ('Desea agregar otro(s) articulos?(S/N):')
            if continuar == 'N':

                print(f'Monto total {TOTAL}\n')
                IVA=TOTAL*16/100
                print(f'Iva del monto total {IVA}\n')
                PRECIOFIN=TOTAL+IVA
                print(f'Precio final de compra {PRECIOFIN}\n')

                Ventas[clave]=Articulos_venta

                print(Ventas)
                break

    if respuesta == 2:
        while True:
            valor=0
            TOTAL=0
            print(SEPARADOR)
            folio_consul = input('Ingrese el folio de la venta a consultar: \n')
            print('Venta consultada:')
            # print(Ventas[folio_consul])


            print(SEPARADOR)
            print(f'Venta: ')
            print(f'{"Descripción":<5} | {"Piezas vendidas":<10} | {"Precio Unitario":<15} | {"Fecha":<10} | {"Folio":<5}')
            for articulo in Ventas[folio_consul]:

                if valor != 0:
                    print(f"{articulo.Descripcion:<5} | {articulo.Piezas:<10} | {articulo.Precioventa:<15} | {Ventas[folio_consul][0]} | {folio_consul}")
                    TOTAL=TOTAL+articulo.Precioventa*articulo.Piezas
                valor=valor+1


            print(SEPARADOR)
            print(f'Monto total {TOTAL}\n')
            IVA=TOTAL*16/100
            print(f'Iva del monto total {IVA}\n')
            PRECIOFIN=TOTAL+IVA
            print(f'Precio final de compra {PRECIOFIN}\n')


            continuar = input ('Desea consultar otra Venta?(S/N):')
            if continuar == 'N':
                break

    if respuesta == 3:
        while True:
            TOTAL=0
            valor=0
            print(SEPARADOR)
            fecha_consul = input('Ingrese la fecha a consultar: \n')
            print(f'Fecha consultada: {fecha_consul}')
            # print(Ventas[folio_consul])


            print(SEPARADOR)
            print(f'Venta: ')
            print(f'{"Descripción":<5} | {"Piezas vendidas":<10} | {"Precio Unitario":<15} | {"Fecha":<10} | {"Folio":<5}')

            for k in Ventas:
                if fecha_consul == Ventas[k][0]:
                    for articulo in Ventas[k]:
                        if valor != 0:
                            print(f"{articulo.Descripcion:<5} | {articulo.Piezas:<10} | {articulo.Precioventa:<15} | {Ventas[k][0]}")
                            TOTAL=TOTAL+articulo.Precioventa*articulo.Piezas
                        valor=valor+1
                valor=0


            print(SEPARADOR)
            print(f'Monto total {TOTAL}\n')
            IVA=TOTAL*16/100
            print(f'Iva del monto total {IVA}\n')
            PRECIOFIN=TOTAL+IVA
            print(f'Precio final de compra {PRECIOFIN}\n')


            continuar = input ('Desea consultar otra Venta?(S/N):')
            if continuar == 'N':
                break


    if respuesta == 4:
            valor=0
            Fecha=[]
            Descripcion=[]
            Piezas=[]
            PrecioVenta=[]
            keys=[]
            for k in Ventas:
                for articulo in Ventas[k]:
                    if valor != 0:
                        Descripcion.append(articulo.Descripcion)
                        Piezas.append(articulo.Piezas)
                        PrecioVenta.append(articulo.Precioventa)
                        keys.append(k)
                        Fecha.append(Ventas[k][0])
                    valor=valor+1
                valor=0

            dicc_tocsv={"Folio":keys,"Fecha":Fecha,"Descripcion":Descripcion,"Piezas":Piezas,"PrecioVenta":PrecioVenta}
            df_ventas = pd.DataFrame(dicc_tocsv)

            print(df_ventas)
            df_ventas.to_csv(r'Ventas.csv',index=None,header=True) #No olvidar la extensión del archivo
    
    
    if respuesta == 5:
        break