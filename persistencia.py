import sqlite3
from livro import Livro
from revista import Revista
from anotacao import Anotacao

DB = "biblioteca.db"

def criar_tabelas():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS publicacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            genero TEXT,
            num_paginas INTEGER,
            status TEXT,
            avaliacao REAL,
            edicao INTEGER
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS anotacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            publicacao_id INTEGER,
            texto TEXT,
            trecho TEXT,
            data TEXT,
            FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
        );
    """)

    con.commit()
    con.close()


def salvar_publicacao(pub):
    con = sqlite3.connect(DB)
    cur = con.cursor()

    tipo = "Livro" if isinstance(pub, Livro) else "Revista"

    cur.execute("""
        INSERT INTO publicacoes
        (tipo, titulo, autor, ano, genero, num_paginas, status, avaliacao, edicao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        tipo,
        pub.titulo,
        pub.autor,
        pub.ano,
        pub.genero,
        pub.num_paginas,
        pub.status,
        pub.avaliacao,
        getattr(pub, "edicao", None)
    ))

    pub_id = cur.lastrowid

    for a in pub.anotacoes:
        cur.execute("""
            INSERT INTO anotacoes (publicacao_id, texto, trecho, data)
            VALUES (?, ?, ?, ?)
        """, (pub_id, a.texto, a.trecho, str(a.data)))

    con.commit()
    con.close()


def carregar_publicacoes():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    cur.execute("SELECT * FROM publicacoes")
    linhas = cur.fetchall()

    publicacoes = []

    for row in linhas:
        (id, tipo, titulo, autor, ano, genero,
         num_paginas, status, avaliacao, edicao) = row

        if tipo == "Livro":
            pub = Livro(titulo, autor, ano, genero, num_paginas)
        else:
            pub = Revista(titulo, autor, ano, genero, num_paginas, edicao)

        pub._status = status
        pub._avaliacao = avaliacao

        # carregar anotações
        cur.execute("SELECT texto, trecho, data FROM anotacoes WHERE publicacao_id = ?", (id,))
        notas = cur.fetchall()

        for texto, trecho, data in notas:
            pub.adicionar_anotacao(Anotacao(texto, trecho))

        publicacoes.append(pub)

    con.close()
    return publicacoes
