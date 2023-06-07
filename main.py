import csv
from sabor import Sabor
from helado import Helado
from manejaHelados import manejaHelados
from manejaSabores import ManejaSabor
if __name__=='__main__':
    unSabor=ManejaSabor()
    unHelado=manejaHelados()
    unSabor.carga()
    unSabor.muestratodo()
    print ("----------HELADERÍA EL CONITO----------")
    print ("1. Registrar venta ")
    print ("2. Mostrar los 5 sabores mas vendidos ")
    print ("3. Ver gramos de helados vendidos por codigo de sabor ")
    print ("4. Ver helados vendidos por tipo (tamaño) ")
    print ("5. Ver importe total recaudado ")
    opc=int(input("Seleccione una opcion "))
    while opc!=0:
        if opc==1:
            unHelado.venta(unSabor)
        elif opc==2:
            unHelado.contar(unSabor)
        elif opc ==3:
            unHelado.TotGrVen(unSabor)
        elif opc==4:
            unHelado.verificarTp(unSabor)
        elif opc==5:
            unHelado.recaudacion()
        print ("----------HELADERÍA EL CONITO----------")
        print ("1. Registrar venta ")
        print ("2. Mostrar los 5 sabores mas vendidos ")
        print ("3. Ver gramos de helados vendidos por codigo de sabor ")
        print ("4. Ver helados vendidos por tipo (tamaño) ")
        print ("5. Ver importe total recaudado ")
        opc=int(input("Seleccione una opcion "))
             
        