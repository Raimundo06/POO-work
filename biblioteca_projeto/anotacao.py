from datetime import date

class Anotacao:
    def __init__(self, texto: str, trecho: str | None = None):
        if not texto:
            raise ValueError("Anotação não pode ser vazia.")
        self._texto = texto
        self._trecho = trecho
        self._data = date.today()

    @property
    def texto(self) -> str:
        return self._texto

    @property
    def trecho(self) -> str | None:
        return self._trecho

    @property
    def data(self) -> date:
        return self._data

    def __str__(self) -> str:
        return f"Anotação: {self._texto} ({self._data})"
