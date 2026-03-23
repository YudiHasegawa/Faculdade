print("Cadastro")
nome = input("Digite o seu nome: ")
senha = input("Digite uma senha: ")
idade = int(input("Digite a sua idade: "))
incorreto = False
while True:
    print("\nLogin\n")
    nomelogin = input("Digite o seu nome: ")
    nomesenha = input("Digite a sua senha: ")
    if nomelogin == nome and nomesenha == senha:
        print(f"""Login feito com sucesso
              
Conta
              
Nome: {nome}
Idade: {idade} anos""")
        break
    else:
        incorreto = True
        while incorreto == True:
            escolha = input("""
    Nome ou senha incorreta, digite 1 para tentar novamente ou 0 para mudar a senha: """)
            if escolha == "1":
                incorreto == False
            elif escolha == "0":
                nomesenha == input("Digite a sua nova senha: ")
                incorreto == False
            else:
                print("Operação inválida")