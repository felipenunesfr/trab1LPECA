#Programa Agênda Telefônica LP ECA - Felipe Nunes Fraga

'''

O exercício de hoje é
Escrever um programa que faça uma agenda básica

Com as seguintes funções:
- Inserir na agenda
- Remover da agenda
- Editar agenda
- Contar elementos da agenda
- Interface modo texto

'''


#Criar lista------------------------------------------------------------------------------------------
lista = []



#Criar arquivo----------------------------------------------------------------------------------------
arquivo = open("Agenda Telefônica.txt", "a")




#Definir funções---------------------------------------------------------------------------------------


def salvar_contatos(lista): #Colocar contato da lista no arquivo --------------------------------------
    arquivo = open("Agenda Telefônica.txt", "w")

    for agenda in lista:
        arquivo.write("{} # {} # {}\n".format(agenda['nome'], agenda['telefone'], agenda['data']))

    arquivo.close()



def existe_contato(lista, nome): #Conferir se contato existe no arquivo, além da lista do programa rodando

    if len(lista) > 0:
        for agenda in lista:
            if nome in agenda['nome']:
                return True

    return False



def carregar_contatos(): #Coloca contato do arquivo na lista--------------------------------------------
    lista = []

    arquivo = open("Agenda Telefônica.txt", "r")

    for linha in arquivo.readlines():
        coluna = linha.strip().split(" # ")

        agenda = {
            "nome": coluna[0],
            "telefone": coluna[1],
            "data": coluna[2]
        }

        lista.append(agenda)

    arquivo.close()

    return lista



def insere(lista): # 1 - Inserir Contato-------------------------------------------------------------------
    print("===========================================")
    
    print("\n\n == Inserir Contato == ")
    while True:
        nome = input("\nDigite o nome do contato: ")

        if not existe_contato(lista, nome):
            break
        else:
            print("\nEsse contato já foi cadastrado.")
            print("\nPor favor, tente outro nome.")
        
    agenda = {
        "nome": input("\nConfirme o nome do contato: "),
        "telefone": input("\nDigite o telefone do contato: "),
        "data": input("\nDigite a data de inserção do contato: "),
    }

    lista.append(agenda)

    print("\nO contato {} foi inserido com sucesso!".format(agenda['nome']))



def remove(lista): # 2 - Remover contato-------------------------------------------------------------------
    print("===========================================")

    print("\n\n == Excluir Contato == ")
    delete = ""
    if len(lista) > 0:

        nome = input("\nDigite o nome do contato a ser excluído: ")
        if existe_contato(lista, nome):
            for i, agenda in enumerate(lista):
                if agenda['nome'] == nome:
                    print("\nO contato foi encontrado. As informações seguem abaixo:")
                    print("Nome: {}".format(agenda['nome']))
                    print("Telefone: {}".format(agenda['telefone']))
                    print("Data de Inserção: {}".format(agenda['data']))
                    print("===========================================")
                    
                    delete = input("\nTem certeza que deseja excluir o contato? 1- Sim 2- Não: ")
                    if delete == "1":
                        del lista[i]

                        print("\nO contato {} foi apagado com sucesso!".format(nome))
                        break
                    elif delete == "2":
                        pass
                    else:
                        print("Comando errado, digite 1 ou 2")
        else:
            print("\nNão existe contato cadastrado no sistema com o nome: {}.".format(nome))

    else:
        print("\nNão existe nenhum contato cadastrado no sistema.")




def edita(lista): # 3 - Editar contato---------------------------------------------------------------------------
    print("===========================================")

    print("\n\n == Editar Contato == ")
    if len(lista) > 0:
        nome = input("\nDigite o nome do contato a ser editado: ")
        if existe_contato(lista, nome):
            for agenda in lista:
                if agenda['nome'] == nome:
                    print("\nO contato foi encontrado. As informações seguem abaixo:")
                    print("Nome: {}".format(agenda['nome']))
                    print("Telefone: {}".format(agenda['telefone']))
                    print("Data de Inserção: {}".format(agenda['data']))
                    print("===========================================")

                    agenda['telefone'] = input("\nDigite o novo telefone do contato: ")
                    agenda['data'] = input("\nDigite a data de alteração do contato: ")

                    print("\n Os dados do contato {} foram editados com sucesso!".format(agenda['nome']))
                    break

        else:
            print("\nNão existe contato cadastrado no sistema com o nome: {}.".format(nome))

    else:
        print("\nNão existe nenhum contato cadastrado no sistema.")



def contabiliza(lista): # 4 - Contar contatos---------------------------------------------------------------
    print("===========================================")

    print("\n\n == Contabilizar Contatos == ")
    if len(lista) > 0:
        print("\n\nQuantidade de contatos: {}\n".format(len(lista)))
    else:
        print("\nNão existe nenhum contato cadastrado no sistema.")



def crialista(lista): # 5 - Listar contatos-----------------------------------------------------------------
    print("===========================================")

    print("\n\n == Lista de Contatos == ")
    if len(lista) > 0:
        for i, agenda in enumerate(lista):
            print("Contato {}:".format(i+1))
            print("\tNome: {}".format(agenda['nome']))
            print("\tTelefone: {}".format(agenda['telefone']))
            print("\tData de Inserção: {}".format(agenda['data']))
            print("===========================================")

        print("\nQuantidade de contatos: {}\n".format(len(lista)))

    else:
        print("\nNão existe nenhum contato cadastrado no sistema.")



def busca(lista): # 6 - Buscar contato----------------------------------------------------------------------
    print("===========================================")

    print("\n\n == Buscar Contato == ")
    if len(lista) > 0:

        nome = input("\nDigite o nome do contato a ser encontrado: ")
        if existe_contato(lista, nome):
            for agenda in lista:
                if nome in agenda['nome']:
                    print("\nO contato foi encontrado. As informações seguem abaixo:")
                    print("Nome: {}".format(agenda['nome']))
                    print("Telefone: {}".format(agenda['telefone']))
                    print("Data de Inserção: {}".format(agenda['data']))
                    print("===========================================")
                    break
        else:
            print("\nNão existe contato cadastrado no sistema com o nome: {}.".format(nome))

    else:
        print("\nNão existe nenhum contato cadastrado no sistema.")






#Loop do menu da agenda-------------------------------------------------------------------------------------

comando = ""

lista = carregar_contatos()

while (comando != "FIM"):
    print("\n===========================================")
    print("\n === Bem vindo à agenda de LP do Felipe Nunes ===\n")
    print("*Você tem 7 opções para escolher:\n")
    print(" 1 - Inserir contato")
    print(" 2 - Remover contato")
    print(" 3 - Editar contato")
    print(" 4 - Contar contatos")
    print(" 5 - Listar contatos")
    print(" 6 - Buscar contato")
    print(" 7 - Encerrar sessão")
    comando = input("\nDigite o comando que você deseja: ")
    if comando == "1":
        insere(lista)
        salvar_contatos(lista)
    elif comando == "2":
        remove(lista)
        salvar_contatos(lista)
    elif comando == "3":
        edita(lista)
        salvar_contatos(lista)
    elif comando == "4":
        contabiliza(lista)
    elif comando == "5":
        crialista(lista)
    elif comando == "6":
        busca(lista)
    elif comando == "7":
        print("\n=== Finalizando o programa... ===")
        comando = "FIM"
    else:
        print("\nComando não encontrado, tente novamente.")