def numero_perfeito(num):
    '''
    num: um número inteiro

    Essa função retorna True se num for um número perfeito e False caso contrário.
    '''
    l = list()
    for n in range(1, num):
        if num % n == 0:
            l.append(n)
    if sum(l) == num:
        return True
    else:
        return False


numero_perfeito(28)
