class Colecao:
    def __init__(self):
        self._publicacoes = []

    def adicionar_publicacao(self, pub):
        self._publicacoes.append(pub)

    def remover_publicacao(self, titulo):
        self._publicacoes = [p for p in self._publicacoes if p.titulo != titulo]

    def buscar_por_titulo(self, titulo):
        return [p for p in self._publicacoes if titulo.lower() in p.titulo.lower()]

    def buscar_por_autor(self, autor):
        return [p for p in self._publicacoes if autor.lower() in p.autor.lower()]

    def buscar_por_genero(self, genero):
        return [p for p in self._publicacoes if genero.lower() in p.genero.lower()]

    def buscar_por_status(self, status):
        return [p for p in self._publicacoes if p.status == status]

    def gerar_relatorio(self):
        return {
            "total_publicacoes": len(self._publicacoes),
            "lidos": len([p for p in self._publicacoes if p.status == "LIDO"]),
            "nao_lidos": len([p for p in self._publicacoes if p.status == "NAO LIDO"]),
            "lendo": len([p for p in self._publicacoes if p.status == "LENDO"])
        }
