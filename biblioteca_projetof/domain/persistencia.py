import json
import os
from livro import Livro
from revista import Revista
from anotacao import Anotacao

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE_DIR, "dados.json")


def salvar_publicacoes(publicacoes):
    dados = []

    for p in publicacoes:
        dados.append({
            "tipo": p.__class__.__name__,
            "titulo": p.titulo,
            "autor": p.autor,
            "ano": p.ano,
            "genero": p.genero,
            "num_paginas": p.num_paginas,
            "status": p.status,
            "avaliacao": p.avaliacao,
            "anotacoes": [
                {"texto": a.texto, "trecho": a.trecho}
                for a in p.anotacoes
            ],
            "edicao": getattr(p, "edicao", None)
        })

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_publicacoes():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    publicacoes = []

    for item in dados:
        if item["tipo"] == "Livro":
            pub = Livro(
                item["titulo"],
                item["autor"],
                item["ano"],
                item["genero"],
                item["num_paginas"]
            )
        elif item["tipo"] == "Revista":
            pub = Revista(
                item["titulo"],
                item["autor"],
                item["ano"],
                item["genero"],
                item["num_paginas"],
                item["edicao"]
            )
        else:
            continue

        pub.status = item["status"]
        pub.avaliacao = item["avaliacao"]

        for a in item["anotacoes"]:
            pub.anotacoes.append(
                Anotacao(a["texto"], a["trecho"])
            )

        publicacoes.append(pub)

    return publicacoes
