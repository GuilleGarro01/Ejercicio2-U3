import csv
from sabor import Sabor
class ManejaSabor: 
    __lista2=[]
    def __init__(self):
        __lista2=[]
    def carga(self):
        archivo=open('sabores.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            self.AgregaALista(fila[0],fila[1],fila[2])
    def AgregaALista(self,idSabor,ingredientes,nombre):
        self.__lista2.append(Sabor(idSabor,ingredientes,nombre))
    def muestratodo(self):
        for i in self.__lista2:
            print(i)
    def sabor(self,i):
        return self.__lista2[i-1]
    def dimension(self):
        return (len(self.__lista2))

