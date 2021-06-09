

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def outro_contrutor(cls, nome, sobrenome):
        cls.sobrenome = sobrenome
        return cls(nome)

p = Pessoa('samuel')
print(p.nome)
p = Pessoa.outro_contrutor('saulo', 'nunes')
print(p.sobrenome)

