from persistencia import carregar_publicacoes, salvar_publicacoes


class Colecao:
    def __init__(self):
        self._publicacoes = carregar_publicacoes()

    def adicionar_publicacao(self, pub):
        self._publicacoes.append(pub)

    def listar_todas(self):
        return self._publicacoes

    def buscar_por_titulo(self, termo):
        termo = termo.lower()
        return [p for p in self._publicacoes if termo in p.titulo.lower()]

    def salvar(self):
        salvar_publicacoes(self._publicacoes)
