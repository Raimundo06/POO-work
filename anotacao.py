from datetime import date

class Anotacao:
    def __init__(self, texto, trecho=None):
        self._texto = texto
        self._trecho = trecho
        self._data = date.today()

    @property
    def texto(self):
        return self._texto

    @property
    def trecho(self):
        return self._trecho

    @property
    def data(self):
        return self._data

    def __str__(self):
        return f"Anotação: {self._texto} ({self._data})"
