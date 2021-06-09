class FilaDePrioridade:

    def __init__(self, nome):
        self.nome = nome
        self.l = list()

    def inserir(self, item, prioridade):
        self.l.append(item)
        self.l.append(prioridade)

    def remover(self):
        self.maior_idade = 0
        for pos, item in enumerate(self.l):
            if type(item) == int and self.maior_idade < item:
                self.maior_idade = item
                self.pos_idade = pos
        self.retorno = (self.l[self.pos_idade - 1], self.l[self.pos_idade])
        self.l.pop(self.pos_idade)
        self.l.pop(self.pos_idade - 1)
        return self.retorno
    pass

f = FilaDePrioridade('Pessoas')
f.inserir('samuel', 22)
f.inserir('saulo', 18)
f.inserir('Mãe', 45)
f.inserir('Carol', 48)
print(f.remover())
print(f.remover())
print(f.remover())
print(f.remover())
