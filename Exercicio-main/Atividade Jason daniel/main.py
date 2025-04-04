import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("\n --- CADASTROS ---")
    print("Se Cadastre Aqui")
    print("1 - Novo Cadastro")
    print("2 - Ver Cadastro")
    print("3 - Sair")
    print("----------------------")

    def salvar_cadastros (cadastros):
        with open (arquivo_cadastros, "w", enconding = "utf-8") as arquivo:
            json.dump(cadastros, arquivo_cadastros, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try:
        with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):











def cadastrar_pessoa (cadastros):
    Nome = input("Nome:")
    Idade = input("Idade:")
    Turma = input("Turma:")
    Curso = input("Curso:")

    cadastros.append({"Nome":Nome, "Idade": Idade, "Turma": Turma, "Curso": Curso})
    salvar_cadastros (cadastros)
    print("Cadastro foi Atualizado com sucesso!")
