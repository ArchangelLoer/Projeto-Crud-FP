cardapio = []
mesas=[]
pedidos=[]


#Funcoes da parte do cardapio 
def adicionar_prato():
    nome = input("Nome do prato: ")
    descricao = input("Descrição: ")
    ingredientes = input("Ingredientes: ")
    preco = float(input("Preço: "))
    categoria = input("Categoria: ")

    prato = {
        "nome": nome,
        "descricao": descricao,
        "ingredientes": ingredientes,
        "preco": preco,
        "categoria": categoria
    }

    cardapio.append(prato)
    print("Prato adicionado com sucesso!")

def listar_cardapio():
    if cardapio:
        print("\n-- Cardápio --")
        for prato in cardapio:
            print(f"Nome: {prato['nome']}")
            print(f"Descrição: {prato['descricao']}")
            print(f"Ingredientes: {prato['ingredientes']}")
            print(f"Preço: R${prato['preco']:.2f}")
            print(f"Categoria: {prato['categoria']}")
            print("-" * 20)
    else:
        print("Cardápio vazio!")

def atualizar_prato():
    nome = input("Digite o nome do prato que deseja atualizar: ")
    encontrado = False

    for prato in cardapio:
        if prato['nome'].lower() == nome.lower():
            print(f"Prato encontrado: {prato['nome']}")
            prato['nome'] = input("Novo nome: ")
            prato['descricao'] = input("Nova descrição: ")
            prato['ingredientes'] = input("Novos ingredientes: ")
            prato['preco'] = float(input("Novo preço: "))
            prato['categoria'] = input("Nova categoria: ")
            print("Prato atualizado com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print("Prato não encontrado no cardápio.")

def remover_prato():
    nome = input("Digite o nome do prato que deseja remover: ")
    encontrado = False

    for prato in cardapio:
        if prato['nome'].lower() == nome.lower():
            cardapio.remove(prato)
            print("Prato removido com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print("Prato não encontrado no cardápio.") #Fim das funcoes

def fazer_pedido():
    while True:
     pedidoRealizado = False
     pedido = input("diga o nome do prato:")
     for prato in cardapio:
            if prato['nome'].lower() == pedido.lower():

                pedido = {
                    "prato" : prato,
                    "status" : "Em preparo"
                }
                pedidos.append(pedido)
                print("Seu pedido foi realizado.")
                pedidoRealizado = True
                break
    
        
     if not pedidoRealizado:
        print("prato não encontrado. Tente novamente")
     
     break

def listar_pedido():
    if not pedidos:
        print("A lista de pedidos está vazio.")
    else:
        print("\n--- Pedidos ---")
        for pedido in pedidos:
            print(pedido['prato']['categoria'] + " " + pedido['prato']['nome'] +  " - R$" + str(pedido['prato']['preco']) + " " + pedido["status"])
    
def atualizar_status():
    categoria_Pedido = input("Digite a categoria do pedido:")
    novo_status = input("Digite o status do pedido:")

    for pedido in pedidos:
        if pedido['prato']["categoria"] == categoria_Pedido:
            pedido["status"] = novo_status
            print(f"Status do pedido {categoria_Pedido} atualizado para '{novo_status}'.")
            return
    print(f"Pedido com ID {categoria_Pedido} não encontrado.")

def ordenar_por_numero(m):
    return m['numero']

def criar_mesa():
    print("---Criando Mesa--")
    num_mesa=int(input("Digite o número da mesa: "))

    while num_mesa<1:
        print("Por favor, insira um número positivo para a mesa.")
        num_mesa=int(input("Digite o número da mesa: "))

    mesa_ja_reservada= False

    for m in mesas:
        if m['numero']==num_mesa:
            mesa_ja_reservada=True

    if mesa_ja_reservada:
        print("Mesa já reservada. Escolha outra.")

    else:
        while True:
            status_mesa=input("Digite o status da mesa (D, R, O, I): ").lower()

            if status_mesa in ('d', 'r', 'o', 'i'):
                nova_mesa={'numero':num_mesa,'status':status_mesa}
                mesas.append(nova_mesa)
                mesas.sort(key=ordenar_por_numero)
                print("Mesa criada com sucesso! ")
                break

            else:
                print("Status Invalido")

def listar_mesas():
    print("---Listando Mesas---")

    if not mesas:
        print("Nenhuma mesa encontrada.")
        return

    for m in mesas:
        status = m['status'].lower()

        if status == 'd':
            descricao = 'Disponível'
        elif status == 'r':
            descricao = 'Reservada'
        elif status == 'o':
            descricao = 'Ocupado'
        else:
            descricao = 'Indisponível'

        print(f"Mesa {m['numero']} - Status: {descricao}")
        

def atualizar_mesa():
    print("---Atualizando Mesa---")
    num_mesa=int(input("Digite o número da mesa que deseja atualizar: "))

    for m in mesas:
        if m['numero']==num_mesa:
             while True:
                status_mesa=input("Digite o status da mesa (D, R, O, I): ").lower()

                if status_mesa in ('d', 'r', 'o', 'i'):
                    m['status']=status_mesa
                    print("Mesa atualizada com sucesso! ")
                    break

                else:
                    print("Status Invalido")
            
        else:
            print("Mesa não encontrada.")
        break

def remover_mesa():
    print("---Removendo Mesa---")
    num_mesa=int(input("Digite o número da mesa que deseja remover: "))

    for m in mesas:
        if m['numero']==num_mesa:
            mesas.remove(m)
            print("Mesa removida com sucesso!")
            break
    else:
        print("Mesa não encontrada.")
        
def menu(): #menu principal 
    while True:
        print("----- RESTAURANTE DOS CRUDES -----")
        print("1- Cardápio")
        print("2- Pedidos")
        print("3- Mesas")
        print("0- Sair")
        resposta = int(input("Digite a opção desejada: "))

        if resposta == 1: #caso o usuario digite o cardapio
            while True:
                print("-- Cardápio --")
                print("1- Adicionar Prato")
                print("2- Listar Cardápio")
                print("3- Atualizar Prato")
                print("4- Remover Prato")
                print("0- Voltar ao Menu Principal")
                opcao1 = int(input("Digite a opção desejada: "))

                if opcao1 == 1: #Chamando as fucoes feita anteriomente
                    adicionar_prato()
                elif opcao1 == 2:
                    listar_cardapio()
                elif opcao1 == 3:
                    atualizar_prato()
                elif opcao1 == 4:
                    remover_prato()
                elif opcao1 == 0:
                    print("Voltando ao Menu Principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif resposta == 2: # Parte incompleta 
            print("Pedidos")
            print("1- Fazer Pedido")
            print("2- Listar Pedidos")
            print("3- Atualizar Status do Pedido")
            print("4- Fechar Conta")
            opcao2 = int(input("Digite a opção desejada: "))

            if opcao2==1:
                fazer_pedido()

            elif opcao2==2:
                listar_pedido()

            elif opcao2==3:
               atualizar_status('categoria_Pedido', 'novo_status')

        elif resposta == 3: #Parte incompleta 
         while True:
            print("----Mesas----")
            print("1- Criar Mesa")
            print("2- Listar Mesas")
            print("3- Atualizar Mesa")
            print("4- Remover Mesa")
            print("0- Voltar ao Menu Principal")
            opcao3 = int(input("Digite a opção desejada: "))

            if opcao3==1:
             criar_mesa()

            elif opcao3==2:
             listar_mesas()

            elif opcao3==3:
                atualizar_mesa()

            elif opcao3==4:
                remover_mesa()

            elif opcao3==0:
                print("Voltando ao Menu Principal...")
                break

        elif resposta==0:
         print("Saindo do programa...")
         break

        else:
            print("Opção inválida.")
    
menu() #fechando a funcao menu