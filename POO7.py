class Pessoa:

    def __init__(self, nome, idade):
        self.nome, self.idade = nome, idade
    pass

class PessoaFisica(Pessoa):

    def __init__(self, cpf, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf
    pass

class PessoaJuridica(PessoaFisica):

    def __init__(self, nome, idade, cpf, cnpj):
        PessoaFisica.__init__(self, cpf, nome, idade)
        self.cnpj = cnpj
    pass

p = PessoaJuridica(nome='samuel', idade=22, cpf='02270190670', cnpj='1234')
print(p.cnpj)
