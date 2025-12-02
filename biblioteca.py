class Biblioteca:
    def __init__(self):
        self._acervo = []

    def adicionar(self, publicacao):
        self._acervo.append(publicacao)

    def remover(self, titulo):
        self._acervo = [p for p in self._acervo if p.titulo != titulo]

    def buscar(self, titulo):
        return [p for p in self._acervo if titulo.lower() in p.titulo.lower()]

    @property
    def acervo(self):
        return self._acervo
