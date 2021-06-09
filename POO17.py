from abc import ABCMeta, abstractmethod
from tkinter import Tk

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def som(self):
        return 'O animal faz: '

class Gato(Animal):

    def som(self):
        print(super(Gato, self).som())
        print('miau miau')

class Cachorro(Animal):

    def som(self):
        print('au au au')

class Factory:

    def produzir_som(self, object_type):
        return eval(object_type)().som()

a = Factory()
a.produzir_som('Gato')
help(Tk)