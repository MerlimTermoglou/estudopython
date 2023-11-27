# se a nota for > ou = a 6 o aluno esta aprovado
# se a nota for < ou = a 4 o aluno esta reprovado
# se a nota for > que 4 e < que 6 o aluno esta de recuperaçao

media = input("digite a nota do aluno: ")

media = float(media)
if media >= 7:
    print("Aprovado")
elif media <= 4:
    print("Reprovado")
else:
    print("Recuperação")