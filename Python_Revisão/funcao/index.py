print("Exemplos Funcoes")

def Dizer_Oi(nome):
    print("Oi " + str(nome))

Dizer_Oi("Lucas")

def fibo(n):
    cont = 0
    num = 1
    aux = 0
    cal = 0
    lista = []
    while cont < n:
        cal = num + aux
        aux = num
        num = cal
        lista += [num]
        cont += 1

    print("\n")
    print("Esses são o numero dá sequencia de Fibonacci".upper())
    print(lista)
    print("\n")

num = input("Digete a quantidade de numeros de Fibbonaci: ")
fibo(int(num))

def fonema(frase):
    texto_minusculo = frase.lower()
    for txt in texto_minusculo:
        aux = txt
        if txt in "aeiou":
            txt = "Vogal"
        else:
            txt = "Consoante"
        print(aux," é uma ", txt)

fonema(input("Digite uma palavra: "))
