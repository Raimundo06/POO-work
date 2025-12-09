def gerar_relatorio(publicacoes):
    from datetime import date
    total = len(publicacoes)
    lidas = sum(1 for p in publicacoes if p.status == "LIDO")
    lendo = sum(1 for p in publicacoes if p.status == "LENDO")
    nao_lidas = total - lidas - lendo
    avaliacoes = [p.avaliacao for p in publicacoes if p.avaliacao is not None]
    media = (sum(avaliacoes) / len(avaliacoes)) if avaliacoes else None
    top5 = sorted([p for p in publicacoes if p.avaliacao is not None], key=lambda x: x.avaliacao, reverse=True)[:5]

    print("\n===== RELATÓRIO DO ACERVO =====\n")
    print(f"Total de publicações: {total}")
    print(f"Lidas: {lidas}")
    print(f"Lendo: {lendo}")
    print(f"Não lidas: {nao_lidas}")
    if media is not None:
        print(f"Média das avaliações: {media:.2f}")
    else:
        print("Média das avaliações: N/A")
    print("\nTop 5 publicações mais bem avaliadas:")
    for p in top5:
        print(f" - {p.titulo} ({p.ano}) - {p.autor} | Nota: {p.avaliacao}")
    print()
