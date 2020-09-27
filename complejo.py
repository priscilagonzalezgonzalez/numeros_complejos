class Complejo():
    def __init__(self, pReal, pImaginaria):
        self.pReal = pReal
        self.pImaginaria = pImaginaria
    
    def imprimir(self):
        print("El numero es: " + str(self.pReal), end = "")
        if(self.pImaginaria >= 0):
            print("+", end = "")
        print(str(self.pImaginaria) + "i")
    
    def suma(self, other):
        sReal = self.pReal + other.pReal
        sImaginario = self.pImaginaria + other.pImaginaria
        print(str(sReal), end="")
        if sImaginario >= 0:
            print("+", end="")
        print(str(sImaginario) + "i")
    
    def resta(self, other):
        newOtherR = other.pReal * -1
        newOtherI = other.pImaginaria * -1
        sReal = self.pReal + newOtherR
        sImaginario = self.pImaginaria + newOtherI
        print(str(sReal), end="")
        if sImaginario >= 0:
            print("+", end="")
        print(str(sImaginario) + "i")

       




