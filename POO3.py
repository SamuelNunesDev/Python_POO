def obter_mais_longa_substring(s):
    '''
    s: string que será passada

    Essa função retorna a mais longa substring de texto em ordem alfabética.
    '''

    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
         'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
         'x': 24, 'y': 25, 'z': 26}
    l = list()
    substring1 = ''
    for pos, letra in enumerate(s):
        if pos == 0:
            substring1 += letra
        elif d[letra] >= d[substring1[-1]]:
            substring1 += letra
        else:
            l.append(substring1)
            substring1 = letra
        if pos == len(s) - 1:
            l.append(substring1)
    maior_substring = ''
    for sub in l:
        if len(sub) > len(maior_substring):
            maior_substring = sub
    return maior_substring


obter_mais_longa_substring('azcbobobegghakl')
