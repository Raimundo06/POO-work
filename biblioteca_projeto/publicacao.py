from __future__ import annotations
from datetime import date
from typing import List, Optional
from anotacao import Anotacao

STATUS_NAO_LIDO = "NAO LIDO"
STATUS_LENDO = "LENDO"
STATUS_LIDO = "LIDO"

class Publicacao:
    def __init__(self, titulo: str, autor: str, ano: int, genero: str, num_paginas: int):
        self._titulo = titulo
        self._autor = autor
        self.ano = ano            # passa pela property setter
        self._genero = genero
        self._num_paginas = num_paginas
        self._status = STATUS_NAO_LIDO
        self._data_inclusao = date.today()
        self._data_inicio: Optional[date] = None
        self._data_termino: Optional[date] = None
        self._avaliacao: Optional[float] = None
        self._anotacoes: List[Anotacao] = []

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("Título não pode ser vazio.")
        self._titulo = valor.strip()

    @property
    def autor(self) -> str:
        return self._autor

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, valor: int):
        if valor < 1500:
            raise ValueError("Ano inválido. Deve ser >= 1500.")
        self._ano = valor

    @property
    def genero(self) -> str:
        return self._genero

    @property
    def num_paginas(self) -> int:
        return self._num_paginas

    @property
    def status(self) -> str:
        return self._status

    @property
    def avaliacao(self) -> Optional[float]:
        return self._avaliacao

    @property
    def anotacoes(self) -> List[Anotacao]:
        return list(self._anotacoes)

    @property
    def data_inicio(self) -> Optional[date]:
        return self._data_inicio

    @property
    def data_termino(self) -> Optional[date]:
        return self._data_termino

    def iniciar_leitura(self):
        if self._status == STATUS_LENDO:
            return
        self._status = STATUS_LENDO
        if self._data_inicio is None:
            self._data_inicio = date.today()

    def concluir_leitura(self):
        # Regra: não pode marcar LIDO sem data de início
        if self._data_inicio is None:
            raise ValueError("Não é possível marcar como LIDO sem iniciar a leitura.")
        self._status = STATUS_LIDO
        self._data_termino = date.today()

    def alterar_status(self, novo_status: str):
        if novo_status not in (STATUS_NAO_LIDO, STATUS_LENDO, STATUS_LIDO):
            raise ValueError("Status inválido.")
        if novo_status == STATUS_LIDO:
            self.concluir_leitura()
        elif novo_status == STATUS_LENDO:
            self.iniciar_leitura()
        else:
            self._status = STATUS_NAO_LIDO

    def registrar_avaliacao(self, nota: float):
        # Regra: só pode avaliar após LIDO
        if self._status != STATUS_LIDO:
            raise ValueError("Avaliação só pode ser registrada após leitura concluída (LIDO).")
        if nota < 0 or nota > 10:
            raise ValueError("Avaliação deve ser entre 0 e 10.")
        self._avaliacao = float(nota)

    def adicionar_anotacao(self, anotacao: Anotacao):
        self._anotacoes.append(anotacao)

    def __str__(self) -> str:
        return f"{self._titulo} ({self._ano}) - {self._autor} | {self._status}"

    def __repr__(self) -> str:
        return (f"Publicacao(titulo={self._titulo!r}, autor={self._autor!r}, "
                f"ano={self._ano}, genero={self._genero!r})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Publicacao):
            return False
        return (self._titulo.lower() == other._titulo.lower()
                and self._autor.lower() == other._autor.lower())

    def __lt__(self, other: Publicacao) -> bool:
        return self._ano < other._ano
