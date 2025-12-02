from publicacao import Publicacao

class Livro(Publicacao):
    def __str__(self):
        return f"[Livro] {self.titulo} - {self.autor}"
