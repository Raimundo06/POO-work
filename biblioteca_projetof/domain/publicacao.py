class Publicacao:
    def __init__(self, titulo, autor, ano, genero, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.num_paginas = num_paginas
        self.status = "Não iniciado"   # Não iniciado | Lendo | Concluído
        self.avaliacao = None
        self.anotacoes = []

    def iniciar_leitura(self):
        if self.status == "Não iniciado":
            self.status = "Lendo"
            print("📖 Leitura iniciada.")
        else:
            print("⚠️ A leitura já foi iniciada ou concluída.")

    def concluir_leitura(self):
        if self.status == "Lendo":
            self.status = "Concluído"
            print("✅ Leitura concluída.")
        else:
            print("⚠️ Você só pode concluir uma leitura que esteja em andamento.")

    def registrar_avaliacao(self, nota):
        if self.status != "Concluído":
            print("❌ Você só pode avaliar após concluir a leitura.")
            return

        if not isinstance(nota, int) or nota < 0 or nota > 10:
            print("❌ Nota inválida. Digite um valor entre 0 e 10.")
            return

        self.avaliacao = nota
        print("⭐ Avaliação registrada com sucesso.")

    def adicionar_anotacao(self, texto):
        if not texto.strip():
            print("❌ A anotação não pode ser vazia.")
            return

        self.anotacoes.append(texto)
        print("📝 Anotação adicionada.")

    def __str__(self):
        avaliacao_str = self.avaliacao if self.avaliacao is not None else "Não avaliado"

        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"Ano: {self.ano} | "
            f"Gênero: {self.genero} | "
            f"Páginas: {self.num_paginas} | "
            f"Status: {self.status} | "
            f"Avaliação: {avaliacao_str}"
        )
