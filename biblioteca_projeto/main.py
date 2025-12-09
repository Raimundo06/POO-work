from colecao import Colecao
from livro import Livro
from revista import Revista
from anotacao import Anotacao
from relatorio import gerar_relatorio


def input_int(prompt, default=None):
    try:
        return int(input(prompt))
    except:
        return default


def escolher_publicacao(colecao, acao):
    termo = input(f"Digite parte do título da publicação para {acao}: ").strip()
    pubs = colecao.buscar_por_titulo(termo)

    if not pubs:
        print("Nenhuma publicação encontrada.")
        return None

    print("\nPublicações encontradas:")
    for i, p in enumerate(pubs, 1):
        print(f"{i}. {p.titulo} - {p.autor} ({p.status})")

    escolha = input_int("Escolha o número da publicação: ")
    if escolha is None or escolha < 1 or escolha > len(pubs):
        print("Escolha inválida.")
        return None

    return pubs[escolha - 1]


def menu():
    colecao = Colecao()

    while True:
        print("\n==== MENU BIBLIOTECA ====")
        print("1 - Cadastrar Livro")
        print("2 - Cadastrar Revista")
        print("3 - Listar Publicações")
        print("4 - Iniciar Leitura")
        print("5 - Concluir Leitura")
        print("6 - Anotar")
        print("7 - Avaliar")
        print("8 - Gerar Relatório")
        print("9 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            ano = input_int("Ano: ")
            genero = input("Gênero: ").strip()
            num_pag = input_int("Páginas: ")

            try:
                livro = Livro(titulo, autor, ano, genero, num_pag)
                colecao.adicionar_publicacao(livro)
                print("Livro cadastrado com sucesso!")
            except Exception as e:
                print("Erro:", e)

        elif opcao == "2":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            ano = input_int("Ano: ")
            genero = input("Gênero: ").strip()
            num_pag = input_int("Páginas: ")
            edicao = input_int("Edição: ")

            try:
                revista = Revista(titulo, autor, ano, genero, num_pag, edicao)
                colecao.adicionar_publicacao(revista)
                print("Revista cadastrada com sucesso!")
            except Exception as e:
                print("Erro:", e)

        elif opcao == "3":
            pubs = colecao.listar_todas()
            if not pubs:
                print("Nenhuma publicação cadastrada.")
            else:
                print("\n===== PUBLICAÇÕES =====")
                for i, p in enumerate(pubs, 1):
                    print(f"{i}. {p.titulo} - {p.autor} ({p.status})")

        elif opcao == "4":
            pub = escolher_publicacao(colecao, "iniciar leitura")
            if pub:
                pub.iniciar_leitura()
                print(f"Leitura iniciada para: {pub.titulo}")

        elif opcao == "5":
            pub = escolher_publicacao(colecao, "concluir leitura")
            if pub:
                try:
                    pub.concluir_leitura()
                    print(f"Leitura concluída para: {pub.titulo}")
                except Exception as e:
                    print("Erro:", e)

        elif opcao == "6":
            pub = escolher_publicacao(colecao, "anotar")
            if pub:
                texto = input("Texto da anotação: ").strip()
                trecho = input("Trecho (opcional): ").strip() or None
                anot = Anotacao(texto, trecho)
                pub.adicionar_anotacao(anot)
                print("Anotação adicionada!")

        elif opcao == "7":
            pub = escolher_publicacao(colecao, "avaliar")
            if pub:
                nota = input("Nota (0-10): ").strip()
                try:
                    nota = float(nota)
                    pub.registrar_avaliacao(nota)
                    print("Avaliação registrada.")
                except Exception as e:
                    print("Erro:", e)

        elif opcao == "8":
            pubs = colecao.listar_todas()
            gerar_relatorio(pubs)

        elif opcao == "9":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
