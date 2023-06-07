from helado import Helado
class manejaHelados:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def venta(self,sabores):
        t=input("Ingrese tipo de helado 100gr, 150gr, 250gr, 500gr, 1000gr ")
        
        cSabores=int(input("Ingrese cantidad de sabores "))
        if t=='100':
            precio=500
        elif t=='150':
            precio=600
        elif t=='250':
            precio=800
        elif t=='500':
            precio=1500
        elif t=='1000':
            precio=2900
        self.__lista.append(Helado(t,precio))
        for i in range(cSabores):
            s=int(input("Ingrese id del sabor "))
            s=sabores.sabor(s)
            self.__lista[-1].agregaSabor(s)
    def contar(self,sabor):
        contadores=[]
        for i in range (sabor.dimension()):
            contadores.append(0)
        for helado in (self.__lista):
            helado.cuenta(contadores)
        for i in range(0,5):
            mayor=contadores.index(max(contadores))
            print (i,sabor.sabor(mayor+1))
            contadores[mayor]=0
    def TotGrVen(self,sabores):
        compara=int(input("Ingrese Id del Sabor "))
        acum=int(0)
        for i in range (len(self.__lista)):
            if compara==self.__lista[i].verifica(compara,sabores):
                acum+=self.__lista[i].getGr()
        print (f"Los gramos vendidos del sabor {compara}, es de : {acum} ")
    def verifica(self,valor,sabores):
        band=False
        i=0
        while band==False and i<(len(self.__lista)):
            if valor==sabores.getId():
                band = True
            else:
                i+=1      
                             
    def verificarTp(self,sabores):
        compara=int(input("Ingrese un tipo de helado "))
        i=0
        flag=False
        while flag==False and i<(len(self.__lista)):
            if compara==self.__lista[i].getGr():
                flag=True
                self.cargalista(compara,sabores)
            else:
                i+=1
        if flag==False:
            print("El tipo de helado ingresado, aún no se vende")
    def cargalista(self,compara,sabores):
        ids=[]
        for i in range (len(self.__lista)):
            if compara==self.__lista[i].getGr():
                self.__lista[i].cargalist(ids)
                
        self.muestraTp(ids,sabores)
    def muestraTp(self,ids,sabores):
        print("Los sabores vendidos de ese tipo de helado son: ")
        for idsabor in ids:
            print(f"{sabores.sabor(idsabor).getNom()}")
    
    def recaudacion(self):
        acu1=0
        acu2=0
        acu3=0
        acu4=0
        acu5=0
        for i in range (len(self.__lista)):
            if self.__lista[i].getGr()==100:
                acu1+=self.__lista[i].getPr()
            elif self.__lista[i].getGr()==150:
                acu2+=self.__lista[i].getPr()
            elif self.__lista[i].getGr()==250:
                acu3+=self.__lista[i].getPr()
            elif self.__lista[i].getGr()==500:
                acu4+=self.__lista[i].getPr()
            elif self.__lista[i].getGr()==1000:
                acu5+=self.__lista[i].getPr()
        print(f"La recaudación correspondiente para los 100gr es de ${acu1}")
        print (f"La recaudación correspondiete para los 150gr es de ${acu2}")
        print(f"La recaudación correspondiente para los 250gr es de ${acu3}")
        print(f"La recuación correspondiente para los 500gr es de ${acu4}")
        print(f"La recaudación correspondiente para el de 1000gr es de ${acu5}")