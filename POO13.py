class SomentePares(list):

    def append(self, inteiro):

        if not isinstance(inteiro, int):
            raise TypeError('Somente números inteiros podem ser cadastrados.')
        elif inteiro % 2 != 0:
            raise ValueError('Somente números pares podem ser cadastrados.')
        super().append(inteiro)

    pass

l = SomentePares()
l.append(2)
print(l)
