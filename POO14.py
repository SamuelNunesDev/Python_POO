
def Fibonacci(condicao):
    x = y = 1
    contador = 1
    while contador <= condicao:
        contador += 1
        yield x
        x, y = y, x + y
    return f'Já foram retornado os {condicao} valores desejados!'

f = Fibonacci(5)
for i in f:
    print(i)
