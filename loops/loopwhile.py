'''
Este exemplo vai imprimindo a variável contador, e no final do bloco de código,
aumenta seu valor em 1. Conforme a condição, enquanto o contador for menor
que 5, o bloco de código dentro dele será executado. Quando o valor chega em 5, a
condição não é mais verdadeira e o bloco não é mais executado.
'''

contador = 0
while contador <= 5:
    print(contador)
    contador = contador + 1