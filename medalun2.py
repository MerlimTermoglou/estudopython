'''
Crie um programa para mostrar se o aluno esta aprovado, reprovado,ou em rec.
O program deve pedir 4 notas e realizar o calculo da media.
se a media do aluno for:

>= 6 aprov
<= 4 reprov
>4 e <6 rec

'''

nota1 = float (input("digite a primeira nota do aluno: ") )
nota2 = float (input("digite a segunda nota do aluno: ") )
nota3 = float (input("digite a terceira nota do aluno: ") )
nota4 = float (input("digite a quarta nota do aluno: ") )

media = (nota1 + nota2 + nota3 + nota4) /4

media = float(media)
if media >= 6:
    print("Aprovado")
elif media <= 4:
    print("Reprovado")
else:
    print("Recuperação")