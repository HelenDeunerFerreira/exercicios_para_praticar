# a) Faça uma função que receba duas listas e retorne True se são iguais ou False caso contrário.
# * Duas listas são iguais se possuem os mesmos valores e na mesma ordem.
# b) Faça uma função que receba duas listas e retorne True se têm os mesmos elementos ou False
# caso contrário
# * Duas listas possuem os mesmos elementos quando são compostas pelos mesmos valores,
# mas não obrigatoriamente na mesma ordem.

import collections
lista1 = list(input('Primeira lista: '))
lista2 = list(input('Segunda lista: '))


def listasIguais():

    if lista1 == lista2:
        print('As listas são iguais!')
    else:
        print('As listas NÃO são iguais.')


def listasElementos():

    if(collections.Counter(lista1) == collections.Counter(lista2)):
        print('As duas listas contém os mesmos elementos!')
    else:
        print('As duas listas NÃO contém os mesmos elemntos.')


def escolha():
    escolhaUsuario = input(
        'O que você deseja fazer? 1 - comparar listas para ver se são iguais ou 2 - comparar listas para verificar se possuem os mesmos elementos')

    if escolhaUsuario == '1':
        listasIguais()
    elif escolhaUsuario == '2':
        listasElementos()
    else:
        print('Essa escolha não é válida!')


escolha()
