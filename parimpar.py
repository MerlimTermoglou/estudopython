numero = input("digite um numero: ")
# o comando input smp retorna um valor
# em formato texto. n importa se foi digitado
# um numero. ele smp retorna um texto
# sendo assim, foi necessario converter a variavel
# numero para um valor inteiro. utilizamos o
# comando int.

if int(numero) % 2 == 0:
    print("o numero é par")
else:
    print("o numero é impar")