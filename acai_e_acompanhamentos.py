#Função para exibir os elementos das listas de sabores e acompanhamentos
def tuas_opcoes(flavors):
    for i in flavors:
        print(i)


#Escolhe o tamanho do açaí e define o preço.
def tamanho():
    tam = int(input('''
Qual o tamanho desejado?
1. 300ml - R$9.50
2. 500ml - R$12.50
3. 700ml - R$14
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
        print('Escolha um dos tamanhos disponíveis!')
        tama, preco = tamanho()

    return tama,preco


#Apresentação e escolha de sabores
def escolhe_sabor():
    sabores = ['\nQual o Sabor desejado?','1-Açaí puro','2-Açaí com xarope de guaraná','3-Açaí batido com banana','4-Casadinho(açaí e creme de cupuaçu)','5-Açaí zero açúcar']

    tuas_opcoes(sabores)

    escolha = int(input('>> '))
    
    if (escolha < 1) or (escolha > 5):
        sabores = escolhe_sabor()
    
    return sabores[escolha][2:]


#Escolha se deseja ou não colocar acompanhamentos
def deseja_acompanhamentos():
    acompanhas = input('\nDeseja adicionar acompanhamentos? S/N\n> ').upper()

    if acompanhas == 'S' or acompanhas == 'SIM':
        escolhidos, valor_escolhidos = acompanhamentos()

    elif acompanhas == 'N' or acompanhas == 'NAO' or acompanhas == 'NÃO':
        escolhidos, valor_escolhidos = [' nada'], 0

    else:
        print('Digite uma opção válida')
        escolhidos, valor_escolhidos = deseja_acompanhamentos()
    
    return escolhidos, valor_escolhidos


#Lista e escolha de acompanhamentos
def acompanhamentos():
    lista_acompanhamentos = ['0- Leite Condensado','1- Granola','2- Morango','3- Banana','4- Amendoim','5- Paçoca','6- Leite em pó','7- Kiwi','8- Calda de maracujá','9- Calda de morango','10- Calda de chocolate','11- Sair']

    escolhidos = []

    for i in lista_acompanhamentos:
        print(i)
  
    escolha_acompanhamentos = esc_acompanhamentos()

    while escolha_acompanhamentos>11:
        print('Escolha uma opção válida')
        escolha_acompanhamentos = esc_acompanhamentos()

    while (escolha_acompanhamentos != 11):
        escolhidos.append(lista_acompanhamentos[escolha_acompanhamentos][2:])
        escolha_acompanhamentos = esc_acompanhamentos()


    valor_acomp = len(escolhidos) * 0.5
  
    return escolhidos, valor_acomp


#Validação de escolha de acompanhamentos
def esc_acompanhamentos():
  escolha_acompanhamentos = int(input('Escolha um acompanhamento, por número: '))

  if (escolha_acompanhamentos < 0) or (escolha_acompanhamentos > 12):
    print('Digite um acompanhamento válido.')
    escolha_acompanhamentos = esc_acompanhamentos()
  
  return escolha_acompanhamentos