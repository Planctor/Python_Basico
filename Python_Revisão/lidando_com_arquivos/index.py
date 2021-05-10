arquivo_texto = open("arquivo.txt", 'w')
arquivo_para_ler = open("arquivo.txt", 'r')

try:
    arquivo_texto_txt = open("arquivo.txt", 'x')
except:
    print("\n======== Arquivo já Existe ========\n")

for i in range(3):
    arquivo_texto.write("Sim eu como alho\n")
arquivo_texto.close()

for arq in arquivo_para_ler.readlines():
    print(arq)
arquivo_para_ler.close()


