from persistencia import criar_tabelas, salvar_publicacao, carregar_publicacoes
from livro import Livro
from revista import Revista
from relatorio import gerar_relatorio

criar_tabelas()

def menu():
    while True:
        print("\n==== MENU BIBLIOTECA ====")
        print("1 - Cadastrar Livro")
        print("2 - Cadastrar Revista")
        print("3 - Listar Publicações")
        print("4 - Gerar Relatório")
        print("5 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            genero = input("Gênero: ")
            num_pag = int(input("Páginas: "))

            livro = Livro(titulo, autor, ano, genero, num_pag)
            salvar_publicacao(livro)
            print("Livro salvo com sucesso!")

        elif opcao == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            genero = input("Gênero: ")
            num_pag = int(input("Páginas: "))
            edicao = int(input("Edição: "))

            revista = Revista(titulo, autor, ano, genero, num_pag, edicao)
            salvar_publicacao(revista)
            print("Revista salva com sucesso!")

        elif opcao == "3":
            pubs = carregar_publicacoes()
            if not pubs:
                print("Nenhuma publicação cadastrada.")
            else:
                print("\n=== PUBLICAÇÕES ===")
                for p in pubs:
                    print(p)

        elif opcao == "4":
            pubs = carregar_publicacoes()
            gerar_relatorio(pubs)

        elif opcao == "5":
            break

        else:
            print("Opção inválida.")

menu()
