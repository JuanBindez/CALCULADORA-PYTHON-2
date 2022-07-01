'''
Author: www.github.com/JuanBindez
Description:
Python Version: 3.10
year: 2022
Local: Brazil
'''

import time
from file.calc import Logica
from file.header import header_menu


def ad():
    num1 = int(input("valor 1 >"))
    num2 = int(input("valor 2 >"))
    result = Logica(num1,num2)
    print(result.logica_adicao())

def sub():
    num1 = int(input("valor 1 >"))
    num2 = int(input("valor 2 >"))
    result = Logica(num1,num2)
    print(result.logica_subtracao())

def div():
    num1 = int(input("valor 1 >"))
    num2 = int(input("valor 2 >"))
    result = Logica(num1,num2)
    print(result.logica_divisao())

def mult():
    num1 = int(input("valor 1 >"))
    num2 = int(input("valor 2 >"))
    result = Logica(num1,num2)
    print(result.logica_multiplicacao())


header_menu()
escolha = int(input('>'))

match escolha:
    case 1:
        ad()

    case 2:
        sub()

    case 3:
        div()

    case 4:
        mult()