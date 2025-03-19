def exibir_menu():
    print("Se Cadastre Aqui")
    print("1 - Novo Cadastro")
    print("2 - Ver Cadastro")
    print("3 - Sair")
    print("----------------------")



def cadastrar_pessoa (cadastros):
    Nome = input("Nome:")
    Idade = input("Nome:")
    Turma = input("Turma:")
    Curso = input("Curso:")
    cadastros.append({"Nome":Nome, "Idade": Idade, "Turma": Turma, "Curso": Curso})
    print("Cadastro foi Atualizado com sucesso!")