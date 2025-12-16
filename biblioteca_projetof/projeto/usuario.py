class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self.historico = []

    def registrar_leitura(self, publicacao):
        self.historico.append(publicacao)