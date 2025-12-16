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

    for i, p in enumerate(pubs, 1):
        print(f"{i}. {p.titulo} - {p.autor} ({p.status})")

    escolha = input_int("Escolha o número: ")
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
            livro = Livro(
                input("Título: "),
                input("Autor: "),
                input_int("Ano: "),
                input("Gênero: "),
                input_int("Páginas: ")
            )
            colecao.adicionar_publicacao(livro)

        elif opcao == "2":
            revista = Revista(
                input("Título: "),
                input("Autor: "),
                input_int("Ano: "),
                input("Gênero: "),
                input_int("Páginas: "),
                input_int("Edição: ")
            )
            colecao.adicionar_publicacao(revista)

        elif opcao == "3":
            for p in colecao.listar_todas():
                print(p)

        elif opcao == "4":
            pub = escolher_publicacao(colecao, "iniciar leitura")
            if pub:
                pub.iniciar_leitura()

        elif opcao == "5":
            pub = escolher_publicacao(colecao, "concluir leitura")
            if pub:
                try:
                    pub.concluir_leitura()
                except Exception as e:
                    print("Erro:", e)

        elif opcao == "6":
            pub = escolher_publicacao(colecao, "anotar")
            if pub:
                pub.adicionar_anotacao(
                    Anotacao(input("Texto: "), input("Trecho: ") or None)
                )

        elif opcao == "7":
            pub = escolher_publicacao(colecao, "avaliar")
            if pub:
                try:
                    pub.registrar_avaliacao(float(input("Nota: ")))
                except Exception as e:
                    print("Erro:", e)

        elif opcao == "8":
            gerar_relatorio(colecao.listar_todas())

        elif opcao == "9":
            colecao.salvar()
            print("Dados salvos. Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
