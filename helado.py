class Helado:
    __gramos=""
    __precio=""
    __sabores=[]
    def __init__(self,gr,pr):
        self.__gramos=int(gr)
        self.__precio=pr
        self.__sabores=[]
    def agregaSabor(self,s):
        self.__sabores.append(s)
    def cuenta(self,contadores):
        for sabor in self.__sabores:
            contadores[sabor.getId()-1]+=1
    def getGr(self):
        return(self.__gramos)    
    def cargalist(self,listaIds):
        for sabor in self.__sabores:
            if sabor.getId() not in listaIds:
                listaIds.append(sabor.getId())
    def getPr(self):
        return (self.__precio)