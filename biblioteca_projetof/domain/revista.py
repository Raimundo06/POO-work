from publicacao import Publicacao


class Revista(Publicacao):
    def __init__(self, titulo, autor, ano, genero, num_paginas, edicao):
        super().__init__(titulo, autor, ano, genero, num_paginas)
        self.edicao = edicao

    def __str__(self):
        return super().__str__() + f" | Edição: {self.edicao}"
