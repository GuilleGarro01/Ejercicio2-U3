class Sabor:
    __idSabor=""
    __ingredientes=""
    __nomSabor=""
    def __init__(self,sabor,ingredientes,nom):
        self.__idSabor=int(sabor)
        self.__ingredientes=ingredientes
        self.__nomSabor=nom      
    def __str__(self):
        return (f"{self.__idSabor}, {self.__ingredientes}, {self.__nomSabor} ")
    def getId(self):
        return self.__idSabor
    def getNom(self):
        return self.__nomSabor

    
    