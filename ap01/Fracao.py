#importar classes caso precise
from math import gcd

class Fracao:
    __num = 1
    __den = 1
    def __init__(self):
        self.__num = Fracao.__num
        self.__den = Fracao.__den
        # self.__reduzir()

    def __reduzir(self):
        if self.__den == 0:
            raise ValueError("o denominador não pode ser zero")

        if self.__den < 0:
            self.__den = -self.__den
            self.__num = -self.__num

        divisor = gcd(self.__num, self.__den)
        self.__num =

    def __add__(self):

        pass
    def __sub__(self):
        pass


    def __str__(self):
        #printando no formato pedido
        return f"{self.__num}/{self.__den}"

@property #getter
def num(self):
    return self.__num
@num.setter #setter
def num(self, value):
    if not isinstance(value, int):
        raise ValueError("must be a integer")
    self.__num = value

@property #getter
def den(self):
    return self.__den
@den.setter #setter
def den(self, value):
    if not isinstance(value, int):
        raise ValueError("must be a integer")
        self.__den = value

if __name__ == '__main__':
   s = Fracao()
   print(s)
