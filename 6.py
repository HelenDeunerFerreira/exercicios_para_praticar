# Faça um programa que percorre uma lista com o seguinte formato:
# [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]].
# Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre
# Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9.
# O programa deve imprimir na tela:
# a) o total de faltas do campeonato
# b) o time que fez mais faltas
# c) o time que fez menos faltas

lista = [['Brasil', 'Italia', [10, 9]], [
    'Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7, 8]]]

faltasBrasil = int(lista[0][2][0]) + int(lista[1][2][0])
faltasItalia = int(lista[0][2][1]) + int(lista[2][2][0])
faltasEspanha = int(lista[2][2][1]) + int(lista[1][2][1])


def totalFaltas():
    faltaJogo1 = int(lista[0][2][0]) + int(lista[0][2][1])
    faltaJogo2 = int(lista[1][2][0]) + int(lista[1][2][1])
    faltaJogo3 = int(lista[2][2][0]) + int(lista[2][2][1])

    totalJogos = faltaJogo1 + faltaJogo2 + faltaJogo3

    print(f'O total de faltas dos 3 jogos é {totalJogos}')


def maisFaltas():
    if faltasBrasil > faltasItalia and faltasBrasil > faltasEspanha:
        print(
            f'O Brasil é o país com mais faltas, tendo um total de {faltasBrasil}')
    elif faltasItalia > faltasEspanha and faltasItalia > faltasBrasil:
        print(
            f'A Italia é o país com mais faltas, tendo um total de {faltasItalia}')
    elif faltasEspanha > faltasBrasil and faltasEspanha > faltasItalia:
        print(
            f'A Espanha é o país com mais faltas, tendo um total de {faltasEspanha}')
    elif faltasBrasil == faltasItalia:
        print(
            f'O número de faltas entre Itália e Brasil é o mesmo: um total de {faltasBrasil}')
    elif faltasBrasil == faltasEspanha:
        print(
            f'O número de faltas entre Espanha e Brasil é o mesmo: um total de {faltasBrasil}')
    elif faltasEspanha == faltasItalia:
        print(
            f'O número de faltas entre Itália e Espanha é o mesmo: um total de {faltasEspanha}')


def menosFaltas():
    if faltasBrasil < faltasItalia and faltasBrasil < faltasEspanha:
        print(
            f'O Brasil é o país com menos faltas, tendo um total de {faltasBrasil}')
    elif faltasItalia < faltasEspanha and faltasItalia < faltasBrasil:
        print(
            f'A Italia é o país com mais faltas, tendo um total de {faltasItalia}')
    elif faltasEspanha < faltasBrasil and faltasEspanha < faltasItalia:
        print(
            f'A Espanha é o país com mais faltas, tendo um total de {faltasEspanha}')
    elif faltasBrasil == faltasItalia:
        print(
            f'O número de faltas entre Itália e Brasil é o mesmo: um total de {faltasBrasil}')
    elif faltasBrasil == faltasEspanha:
        print(
            f'O número de faltas entre Espanha e Brasil é o mesmo: um total de {faltasBrasil}')
    elif faltasEspanha == faltasItalia:
        print(
            f'O número de faltas entre Itália e Espanha é o mesmo: um total de {faltasEspanha}')


totalFaltas()
maisFaltas()
menosFaltas()
