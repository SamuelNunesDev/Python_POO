from abc import ABCMeta, abstractmethod

class Animal:

    @abstractmethod
    def falar(self):
        return 'Eu sou um animal!'
    pass

class Cachorro(Animal):

    def falar(self):
        return f'{super().falar()} Au Au'

c = Cachorro()
print(c.falar())
