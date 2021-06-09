def tupla_par(tupla):
    '''
    tupla: uma tupla

    retorna: nova tupla formada pelos elementos que possuem índices pares
    '''
    l = list()
    for c in enumerate(tupla):
        if c[0] % 2 == 0:
            l.append(c[1])
    return tuple(l)


print(tupla_par(('oi', 'estou', 'estudando', 'poo')))
