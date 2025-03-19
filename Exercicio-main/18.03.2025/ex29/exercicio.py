def exibir_menu():
    print("Se Cadastre Aqui")
    print("1 - Novo Cadastro")
    print("2 - Ver Cadastro")
    print("3 - Sair")
    print("----------------------")



def cadastrar_pessoa (cadastros):
    Nome = input("Nome:")
    Idade = input("Idade:")
    Turma = input("Turma:")
    Curso = input("Curso:")
    cadastros.append({"Nome":Nome, "Idade": Idade, "Turma": Turma, "Curso": Curso})
    print("Cadastro foi Atualizado com sucesso!")


def ver_cadastros (cadastros):
    if not cadastros:
        print("Nenhum Cadastro Encontrado.")
    else:
        print("\n ----Lista de Cadastros ----")

        for i, pessoa in enumerate (cadastros, 1):
            print(f"{i} . nome:) {pessoa['Nome']}, Idade:{pessoa['Idade']}, Turma:{pessoa['turma']}, Curso: {pessoa['Curso']}")
                  
                  



def main ():
    cadastros = []
    while True:
        exibir_menu()
        opção = input("Escolha Uma Opção:  ") 

        if opção == "1":
            cadastrar_pessoa(cadastros)

        elif opção == "2":
            ver_cadastros (cadastros)

        elif opção == "3":
            print("Obrigado Por utilizar!")
            break
            
        else:
            print("Algo Deu Errado, tente novamente")




if __name__ == "__main__":
    main()
