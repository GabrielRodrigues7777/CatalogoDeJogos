from jogos import *

def menu():
    while True:
        print("\n=== INVENTÁRIO DE JOGOS ===")
        print("1 - Listar jogos")
        print("2 - Ver jogo")
        print("3 - Adicionar jogo")
        print("4 - Editar jogo")
        print("5 - Deletar jogo")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_jogos()

        elif opcao == "2":
            indice = int(input("Índice do jogo: "))
            ver_jogo(indice)

        elif opcao == "3":
            adicionar_jogo()

        elif opcao == "4":
            indice = int(input("Índice do jogo: "))
            editar_jogo(indice)

        elif opcao == "5":
            indice = int(input("Índice do jogo: "))
            deletar_jogo(indice)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()