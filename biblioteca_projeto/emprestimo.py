from datetime import date

class Emprestimo:
    def __init__(self, usuario, publicacao):
        self.usuario = usuario
        self.publicacao = publicacao
        self.data_emprestimo = date.today()
        self.devolvido = False

    def devolver(self):
        self.devolvido = True
