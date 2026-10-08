import json
import os

ARQUIVO = "jogos.json"

def carregar_jogos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_jogos(jogos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(jogos, f, indent=4, ensure_ascii=False)

def listar_jogos():
    jogos = carregar_jogos()
    if not jogos:
        print("Nenhum jogo cadastrado.")
        return

    for i, jogo in enumerate(jogos):
        print(f"{i} - {jogo['nome']} ({jogo['ano']})")

def ver_jogo(indice):
    jogos = carregar_jogos()
    try:
        jogo = jogos[indice]
        print("\nDetalhes do jogo:")
        for chave, valor in jogo.items():
            print(f"{chave}: {valor}")
    except:
        print("Índice inválido.")

def adicionar_jogo():
    jogos = carregar_jogos()

    nome = input("Nome: ")
    genero = input("Gênero: ")
    ano = input("Ano: ")

    novo = {
        "nome": nome,
        "genero": genero,
        "ano": ano
    }

    jogos.append(novo)
    salvar_jogos(jogos)
    print("Jogo adicionado!")

def deletar_jogo(indice):
    jogos = carregar_jogos()
    try:
        removido = jogos.pop(indice)
        salvar_jogos(jogos)
        print(f"Jogo '{removido['nome']}' removido!")
    except:
        print("Índice inválido.")

def editar_jogo(indice):
    jogos = carregar_jogos()
    try:
        jogo = jogos[indice]

        print("Deixe vazio para não alterar.")

        nome = input(f"Nome ({jogo['nome']}): ") or jogo['nome']
        genero = input(f"Gênero ({jogo['genero']}): ") or jogo['genero']
        ano = input(f"Ano ({jogo['ano']}): ") or jogo['ano']

        jogos[indice] = {
            "nome": nome,
            "genero": genero,
            "ano": ano
        }

        salvar_jogos(jogos)
        print("Jogo atualizado!")

    except:
        print("Índice inválido.")