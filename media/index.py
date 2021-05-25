alunos = []
quantidade = int(input("Numero de alunos: "))

alunos = [[str(input("Nome: ")), int(input("Nota_1: ")), int(input("Nota_2: ")), int(input("Nota_3: "))] for num in range(quantidade)]

print()

def imprimir_medias(aluno, media):
    print(f"O Aluno {aluno} obteve a média {media}")

def calcular_media_aluno(aluno):
    for al in aluno:
        nome = al[0]
        nota1 = al[1]
        nota2 = al[2]
        nota3 = al[3]
        media = (nota1 + nota2+ nota3)/3
        imprimir_medias(nome, media)

calcular_media_aluno(alunos)

def imprimir_medias_turma(medias):
    m_parametro = medias
    media_lista = []
    soma = 0

    for m in m_parametro:
        media_lista = media_lista + [(m[1] + m[2] + m[3]) / 3]

    for n in media_lista:
        soma = soma + n

    print(f"A média da turma é ${soma / quantidade}")

imprimir_medias_turma(alunos)
