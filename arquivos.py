# -*- coding: utf-8 -*- 

def create_past(name, text):
    file = open(name +'.txt' ,'w')
    file.write(text)
    file.close()
    return True

def read_file(name):
    file = open(name, 'r')
    lines = file.readlines()
    for line in lines:
        print(line)

def update_file(name, text):
    file = open(name, 'a')
    file.write(text)
    file.close()
    return True

def delete_file(name):
    file = open(name, 'w')
    file.write("")
    file.close()
    return True


execute = 10

while execute != 0:
    print("Escolha uma opção: \n1- Criar arquivo de texto \n2- Ler arquivo de texto \n3- Atualizar arquivo de texto \n4- Apagar arquivo de texto \n0- Para sair do programa")
    execute = int(input("Qual opção você deseja? "))

    # Para criar arquivo de texto
    if execute == 1: 
        name = input("Digite o nome do arquivo que deseja criar: ")
        txt = input("Escreva os dados deste arquivo: ")
        verification = create_past(name, txt)

        if verification:
            print("Seu arquivo foi criado com sucesso!")
        else:
            print("Não foi possível criar seu arquivo! Por favor tente novamente!")
    
    # Para ler o arquivo de texto, necessário informar o nome do arquivo
    elif execute == 2:
        name = input("Digite o nome do arquivo que deseja ler: ")
        name = name + ".txt"
        read_file(name)
    
    # Para atualizar um arquivo de texto, necessário informar o nome do arquivo e o texto a ser acrescentado
    elif execute == 3: 
        name = input("Digite o nome do arquvio que deseja atualizar: ")
        name = name + ".txt"
        txt = input("Escreva aqui seu texto: ")
        verification = update_file(name, txt)

        if verification:
            print("Seu arquivo foi atualizado com sucesso!")
        
        else:
            print("Algo deu errado! Tente novamente por favor!")

    # Limpa todos os dados de um arquivo .txt
    elif execute == 4:
        name = input("Digite o nome do arquivo que deseja apagar: ")
        name = name + ".txt"
        verification = delete_file(name)
        
        if verification:
            print("Seu arquivo foi deletado com sucesso!")
        
        else:
            print("Algo deu errado! Tente novamente por favor")
    
    # Fecha a aplicação
    elif execute == 0:
        print("Obrigado por utilizar nosso programa!")
        break



        