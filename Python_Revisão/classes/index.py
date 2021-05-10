class Estudante:
    def __init__(self, nome, idade, comida):
        self.nome = nome
        self.idade = idade
        self.comida = comida

    def dizer_oi(self):
        print("Oi " + self.nome  + "comedor de " + self.comida)

class Professor(Estudante):
    def dizer_oi_teacher(self):
        print("Oi " + self.nome + " Professor"  + "comedor de " + self.comida)

aluno_1 = Estudante("Lucas", 24,"Alho")
aluno_1.dizer_oi()

professor_1 = Professor("Maicon", 24, "Super_Alho")
professor_1.dizer_oi_teacher()