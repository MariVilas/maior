import random
from time import sleep

resposta = 'SN'
while True:
    a = int(input('Entre com um número:'))

    b = int(input('Entre com um número:'))
    print('-' * 40)
    print('-' * 40)
    print("Cal\n")
    sleep(1)
    print("cu\n")
    sleep(1)
    print("lando!!!\n")
    if a >= b:
        print('O Primeiro número é maior que o segundo')

    else:
        print('O Segundo número é maior que o primeiro')



    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
     break
print('-' * 40)
print('-' * 40)
