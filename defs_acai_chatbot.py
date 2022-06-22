#Função para exibir os elementos das listas de sabores e acompanhamentos
def tuas_opcoes(flavors):
  for i in flavors:
    print(i)

#Apresentação e escolha de sabores
def escolhe_sabor():
  sabores = ['0-Açaí puro','1-Açaí com xarope de guaraná','2-Açaí batido com banana','3-Casadinho(açaí e creme de cupuaçu)','4-Açaí zero açúcar']

  tuas_opcoes(sabores)

  escolha = int(input('>> '))
  return sabores[escolha][2:]


#Tamanho do açaí. Vai definir o preço.
def tamanho():
    tam = int(input('''
Qual o tamanho desejado?
1. \033[33m300ml\033[m - R$9.50
2. \033[33m500ml\033[m - R$12.50
3.\033[33m 700ml\033[m - R$14
>> '''))

    if tam == 1:
        tama = '300ml'
        preco = 9.50

    elif tam == 2:
        tama = '500ml'
        preco = 12.50
    
    elif tam == 3:
        tama = '700ml'
        preco = 14
    
    else:
        print('\033[31mEscolha um dos tamanhos disponíveis!\033[m')
        tama, preco = tamanho()

    return tama,preco


#Validação de escolha de acompanhamentos
def esc_acompanhamentos():
  escolha_acompanhamentos = int(input('Escolha um acompanhamento, por número: \n '))

  if (escolha_acompanhamentos < 0) or (escolha_acompanhamentos > 12):
    print('\033[31mDigite um acompanhamento válido.\033[m\n')
    escolha_acompanhamentos = esc_acompanhamentos()
  
  return escolha_acompanhamentos

#Apresentação e escolha de acompanhamentos
def acompanhamentos():
  lista_acompanhamentos = ['0- Leite Condensado','1- Granola','2- Morango','3- Banana','4- Amendoim','5- Paçoca','6- Leite em pó','7- Kiwi','8- Calda de maracujá','9- Calda de morango','10- Calda de chocolate','11- Sair']

  escolhidos = []

  for i in lista_acompanhamentos:
    print(i)
  
  escolha_acompanhamentos = esc_acompanhamentos()

  while escolha_acompanhamentos != 12:
    escolhidos.append(lista_acompanhamentos[escolha_acompanhamentos][2:])
    escolha_acompanhamentos = esc_acompanhamentos()


  valor_acomp = len(escolhidos) * 0.5
  
  return escolhidos, valor_acomp


#####
def valida_opcoes(texto):
    if texto == 'S' or texto == 'SIM':
        pass
    elif texto == 'N' or texto == 'NAO' or texto == 'NÃO':
        pass
    else:
        print('\033[31mDigite uma opção válida\033[m\n')
        

def deseja_acompanhamentos():
    acompanhas = input('Deseja adicionar acompanhamentos? S/N\n> ').upper()

    if acompanhas == 'S' or acompanhas == 'SIM':
        escolhidos, valor_escolhidos = acompanhamentos()
    elif acompanhas == 'N' or acompanhas == 'NAO' or acompanhas == 'NÃO':
        escolhidos, valor_escolhidos = ' nada', 0
    else:
        print('\033[31mDigite uma opção válida\033[m\n')
        escolhidos, valor_escolhidos = deseja_acompanhamentos()
    
    return escolhidos, valor_escolhidos

def mais_um():
    outro = input('\033[33mDeseja outro no mesmo pedido?\033[m \n>> ').upper()

    if outro == 'S' or outro == 'SIM':
        return True
    elif outro == 'N' or outro == 'NAO' or outro == 'NÃO':
        return False

def pedido():
    tama, preco = tamanho()

    sabor_base = escolhe_sabor()
        
    escolhidos, valor_escolhidos = deseja_acompanhamentos()

    return tama, preco, sabor_base, escolhidos, valor_escolhidos


''''    m1 = mais_um()

    

    if m1 is True:
        cmd = comanda(sabor_base, tama, escolhidos, preco, valor_escolhidos, m1)
        pedido()

    else:
        cmd = comanda(sabor_base, tama, escolhidos, preco, valor_escolhidos, m1)
        print('Encerrando Pedido!')

    return cmd'''

def menu():

    caminho = int(input('''
\033[36mBem vindo!\033[m\n
Opções do nosso menu:
1. Escolha seu açaí
2.Status do pedido
3.Informações
4.Sair
>> Digite a sua desejada:  \n'''))

    if caminho == 1:
        tama, preco, sabor_base, escolhidos, valor_escolhidos = pedido()
        seu_pedido, conta = comanda(tama, preco, sabor_base, escolhidos, valor_escolhidos)
        print(f'\033[33m{seu_pedido}. O custo total é de {conta}\033[m\n')

    elif caminho == 2:
        pass
    elif caminho == 3:
        pass
    elif caminho == 4:
        pass
    else:
        caminho = menu()

def comanda(tama, preco, sabor_base, escolhidos, valor_escolhidos):
    seu_pedido = []
    conta = []

    if len(seu_pedido) == 0:
        seu_pedido.append(f'\033[32mSeu pedido é um {sabor_base} de {tama}. Ele acompanha{"".join([x for x in escolhidos])}.\033[m\n')
        conta.append(preco + valor_escolhidos)

    else:
        seu_pedido.append(f'\033[32mE também um {sabor_base} de {tama}. Ele acompanha {"".join([x for x in escolhidos])}.\033[m\n')
        conta.append(preco + valor_escolhidos)

    return seu_pedido, conta

menu()


def cliente():
    #nome do cliente
    nome = input("> Digite o nome do cliente").upper()
    return nome

def responde_nome(nome):   
    #interagindo com o cliente
        clientes = ("STEPHANIE", "IAGO", "PEDRO", "IVES")

        if nome in clientes:
            frase = "Olha quem voltou, como é bom revê-lo!!!!!"
        else:
            frase = "Muito prazer! Seja bem-vindo(a) a toca do açaí"
        return(frase + nome)

def endereço():
    bairro  = str(input("Digite o teu bairro: "))
    rua = int(input("Agora a sua rua: "))
    num = int(input("Digite o número (apto, casa): "))
    cep = int(input("Digite o seu CEP: "))
    complementoEnd= str(input("Digite algum complemento do seu endereço, se tiver: "))
    return bairro, rua, num, cep, complementoEnd

def complementos():
    compl1 = input("Complemento1: ")
    compl2 = input("Complemento2: ")
    compl3 = input("Complemento3: \n")
    pergunta = input("\033[33mVocê quer adicionar com custo adicional de R$ 0,50 (por produto) mais algum complemento?\nDigite: \033[3m\n ")    
    return compl1, compl2, compl3, pergunta

def mostraLinha():
    print('-' * 20)
    
def informacoes():
    mostraLinha()
    print("  \033[33m  Informações: \033[m ")
    mostraLinha()
    duvidas = int(input("1- Realizar pedido.\n\n2- Áreas de entrega.\n\n3- Dias e horários de funcionamento.\n\n4- Métodos de pagamento.\n\n\033[33mDigite o número referente à sua dúvida:\033[m "))
        
    if duvidas == 1:
        print ("\nPara pedir o seu açaí, você deve ir na opção \033[33m'Escolha o seu açaí'\033[m, digitando o número \033[33m1\033[m no \033[33mmenu inicial.\033[m\n\n")
        pass
    elif duvidas == 2: 
        print ("\nEntregamos em Águas Claras, Taguatinga, Guará e Vicente Píres\n\n")
        pass
    elif duvidas == 3:
        print("\nTemos essa novidade para você: agora funcionamos \033[32mtodos os dias das 9:00 às 21:00\033[33m.\n\n")
        pass
    elif duvidas == 4:
        print("\nAceitamos \033[32mPIX, cartão de débito e crédito e dinheiro.\033[m\nSó cobraremos no momento da entrega.\n\n")
        pass
    else:
        print("\n\033[31mDigite uma opção válida.\033[m")
        return informacoes()
informacoes()  
        