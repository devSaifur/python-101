class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result = self.__result + a

    def subtract(self, a):
        self.__result = self.__result - a

    def multiply(self, a):
        self.__result = self.__result * a

    def divide(self, a):
        if a != 0:
            self.__result = self.__result // a
        else:
            raise ValueError("Cannot divide by zero")

    def modulo(self, a):
        if a != 0:
            self.__result = self.__result % a
        else:
            raise ValueError("Cannot divide by zero")

    def power(self, a):
        self.__result = self.__result**a

    def square_root(self):
        if self.__result >= 0:
            self.__result = self.__result**0.5
        else:
            raise ValueError("Cannot calculate square root of negative number")

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result
