# Crie uma função que recebe uma lista de números e
# a. retorne o maior elemento
# b. retorne a soma dos elementos
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a média dos elementos
# e. retorne a soma dos elementos com valor negativo

def listaNumeros():
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    n3 = int(input('Terceiro número: '))
    n4 = int(input('Quarto número: '))
    n5 = int(input('Quinto número: '))

    listaDeNumeros = [n1, n2, n3, n4, n5]
    listaSem = [n2, n3, n4, n5]
    soma = n1 + n2 + n3 + n4 + n5

    resposta = input('Escolha o que deseja fazer com a lista: ')

    if resposta == 'a':
        maiorNumero = 0
        for i in listaDeNumeros:
            if i > maiorNumero:
                maiorNumero = i
        print(f'O maior número dessa lista é {maiorNumero}')

    elif resposta == 'b':
        print(f'A soma dos números da sua lista é {soma}')

    elif resposta == 'c':
        ocorrencias = 1
        for i in listaSem:
            if i == n1:
                ocorrencias += 1
        print(
            f'O número de vezes em que o primeiro elemento da sua lista aparece: {ocorrencias}')

    elif resposta == 'd':
        media = soma/5
        print(f'A média aritmética dos elemnetos listados é {media}')

    elif resposta == 'e':
        somaNegativos = 0
        for i in listaDeNumeros:
            listaNegativos = []
            if i < 0:
                listaNegativos.append(i)
                for i in listaNegativos:
                    somaNegativos += i
        print(f'A soma dos elementos negativos é {somaNegativos}')

    else:
        print('Essa opção não é válida!')


listaNumeros()
