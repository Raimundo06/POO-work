def gerar_relatorio(publicacoes):
    print("\n===== RELATÓRIO DO ACERVO =====\n")

    total = len(publicacoes)
    lidas = sum(1 for p in publicacoes if p.status == "LIDO")
    lendo = sum(1 for p in publicacoes if p.status == "LENDO")
    nao_lidas = sum(1 for p in publicacoes if p.status == "NAO LIDO")

    print(f"Total de publicações: {total}")
    print(f"Lidas: {lidas}")
    print(f"Lendo: {lendo}")
    print(f"Não lidas: {nao_lidas}\n")

    print("---- LISTAGEM ----")
    for p in publicacoes:
        print(f"{p.titulo} ({p.ano}) - {p.autor} | Status: {p.status} | Nota: {p.avaliacao}")
