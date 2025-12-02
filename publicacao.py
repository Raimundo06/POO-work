from datetime import date

class Publicacao:
    def __init__(self, titulo, autor, ano, genero, num_paginas):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._genero = genero
        self._num_paginas = num_paginas
        self._status = "NAO LIDO"
        self._data_inclusao = date.today()
        self._avaliacao = None
        self._anotacoes = []

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("Título não pode ser vazio.")
        self._titulo = valor

    @property
    def autor(self):
        return self._autor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1500:
            raise ValueError("Ano inválido.")
        self._ano = valor

    @property
    def genero(self):
        return self._genero

    @property
    def num_paginas(self):
        return self._num_paginas

    @property
    def status(self):
        return self._status

    @property
    def avaliacao(self):
        return self._avaliacao

    @property
    def anotacoes(self):
        return self._anotacoes

    def alterar_status(self, novo_status):
        if novo_status not in ["NAO LIDO", "LENDO", "LIDO"]:
            raise ValueError("Status inválido.")
        self._status = novo_status

    def registrar_avaliacao(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("Avaliação deve ser entre 0 e 10.")
        self._avaliacao = nota

    def adicionar_anotacao(self, anotacao):
        self._anotacoes.append(anotacao)

    def __str__(self):
        return f"{self._titulo} ({self._ano}) - {self._autor}"

    def __repr__(self):
        return f"Publicacao(titulo='{self._titulo}', autor='{self._autor}')"

    def __eq__(self, other):
        return (self._titulo == other._titulo and self._autor == other._autor)

    def __lt__(self, other):
        return self._ano < other._ano
