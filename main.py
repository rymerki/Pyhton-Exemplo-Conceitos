from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:
    try:
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        idade = int(input("Digite sua idade: "))
        usuario = Usuario(nome, sobrenome, idade)

        # append adiciona objetos na lista
        lista_usuarios.append(usuario)

        if usuario.idade == 99:
            break
        if usuario.idade == 98:
            continue

        print(f"Olá {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

        if usuario.idade <= 17:
            print(f"{usuario.nome} é adolescente")
        elif usuario.idade >= 18 and usuario.idade <= 50:
            print(f"{usuario.nome} é adulto.")
        else:
            print(f"{usuario.nome} é idoso")

        continuar = int(input("Deseja continuar cadastrando? 0 - Sair 1 - Continuar "))
    except ValueError:
        print("Você deve informar um número válido.")
else:
    print("Lista de usuários cadastrados: ")
    for x in lista_usuarios:
        print(f"Nome completo: {x.nome} {x.sobrenome} - Idade: {x.idade}")

    print(f"O loop entrou no else")