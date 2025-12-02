class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []

    def registrar_leitura(self, publicacao):
        self.historico.append(publicacao)
