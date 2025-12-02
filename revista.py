from publicacao import Publicacao

class Revista(Publicacao):
    def __init__(self, titulo, autor, ano, genero, num_paginas, edicao):
        super().__init__(titulo, autor, ano, genero, num_paginas)
        self._edicao = edicao

    @property
    def edicao(self):
        return self._edicao

    def __str__(self):
        return f"[Revista] {self.titulo} - Edição {self._edicao}"
