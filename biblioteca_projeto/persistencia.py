import sqlite3
from typing import List
from livro import Livro
from revista import Revista
from publicacao import Publicacao
from anotacao import Anotacao
import os

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
            edicao INTEGER,
            data_inicio TEXT,
            data_termino TEXT,
            data_inclusao TEXT
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

def salvar_publicacoes(publicacoes: List[Publicacao]):
    criar_tabelas()
    con = sqlite3.connect(DB)
    cur = con.cursor()
    # Para simplicidade: limpamos e inserimos novamente
    cur.execute("DELETE FROM anotacoes;")
    cur.execute("DELETE FROM publicacoes;")
    con.commit()

    for p in publicacoes:
        tipo = "Livro" if isinstance(p, Livro) else "Revista"
        cur.execute("""
            INSERT INTO publicacoes
            (tipo, titulo, autor, ano, genero, num_paginas, status, avaliacao, edicao, data_inicio, data_termino, data_inclusao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            tipo,
            p.titulo,
            p.autor,
            p.ano,
            p.genero,
            p.num_paginas,
            p.status,
            p.avaliacao,
            getattr(p, "edicao", None),
            getattr(p, "data_inicio", None),
            getattr(p, "data_termino", None),
            getattr(p, "_data_inclusao", None)
        ))
        pub_id = cur.lastrowid
        for a in p.anotacoes:
            cur.execute("""
                INSERT INTO anotacoes (publicacao_id, texto, trecho, data)
                VALUES (?, ?, ?, ?)
            """, (pub_id, a.texto, a.trecho, str(a.data)))
    con.commit()
    con.close()

def carregar_publicacoes():
    if not os.path.exists(DB):
        return []
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM publicacoes")
    linhas = cur.fetchall()
    publicacoes = []
    for row in linhas:
        (id_, tipo, titulo, autor, ano, genero,
         num_paginas, status, avaliacao, edicao,
         data_inicio, data_termino, data_inclusao) = row
        if tipo == "Livro":
            p = Livro(titulo, autor, ano, genero, num_paginas)
        else:
            p = Revista(titulo, autor, ano, genero, num_paginas, edicao)
        # restaurar estado privado onde necessário
        p._status = status
        p._avaliacao = avaliacao
        # não convertemos datas para date por simplicidade; mantemos None ou string
        if data_inicio:
            from datetime import datetime
            try:
                p._data_inicio = datetime.fromisoformat(data_inicio).date()
            except Exception:
                p._data_inicio = None
        if data_termino:
            from datetime import datetime
            try:
                p._data_termino = datetime.fromisoformat(data_termino).date()
            except Exception:
                p._data_termino = None
        # carregar anotacoes
        cur.execute("SELECT texto, trecho, data FROM anotacoes WHERE publicacao_id = ?", (id_,))
        notas = cur.fetchall()
        for texto, trecho, data in notas:
            p.adicionar_anotacao(Anotacao(texto, trecho))
        publicacoes.append(p)
    con.close()
    return publicacoes
