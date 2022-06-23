from time import sleep
from random import random
from pedido_comanda import pedido, comanda, confirmacao_pedido


#Linhas que compõe o menu de informações
def mostraLinha():
    print('-' * 20)
    
#Apresenta informações ao cliente
def informacoes():
    mostraLinha()
    print("Informações: ")
    mostraLinha()

    duvidas = int(input("""
1- Como realizar seu pedido.
    
2- Áreas de entrega.
    
3- Dias e horários de funcionamento.
    
4- Métodos de pagamento.
    
5- Voltar para o menu
    
Digite o número referente à sua dúvida
    
>> """))
        
    if duvidas == 1:
        print ("\nPara pedir o seu açaí, você deve ir na opção 'Escolha o seu açaí', digitando o número no menu inicial.")

    elif duvidas == 2: 
        print ("\nEntregamos no raio de até 10km.\n\n")

    elif duvidas == 3:
        print("\nTemos essa novidade para você: agora funcionamos todos os dias das 9:00 às 21:00.\n\n")

    elif duvidas == 4:
        print("\nAceitamos PIX, cartão de débito e crédito e dinheiro.\nCobramos no ato da entrega.\n\n")

    elif duvidas == 5:
        print('Direcionando para o Menu Principal... Aguarde')
        sleep(2)
        chamar_menu()
        
    else:
        print("\nDigite uma opção válida.")
   
    
    sleep(1.5)
    informacoes()


#Função de menu principal

def chamar_menu():

  caminho = int(input('''
Escolha uma das opções do nosso menu:
1. Menu & Preços
2. Escolha seu açaí
3. Acompanhe o seu pedido
4. Informações
5. Sair
>> '''))

  if caminho == 1:
    print('''
Nossos açaís custam de acordo com seu tamanho!
300ml -> R$ 9.50
500ml -> R$ 12.50
700ml -> R$ 14.00

Cada acompanhamento custa R$0.50!
Saboreie já o seu!''')
    sleep(2)
 

  elif caminho == 2:
    sleep(.5)
    tama, preco, sabor_base, escolhidos, valor_escolhidos = pedido()
    seu_pedido, conta = comanda(tama, preco, sabor_base, escolhidos, valor_escolhidos)

    confirmacao_pedido(seu_pedido, conta)


  elif caminho == 3:
    print('\nSeu pedido está há %.2fkm' % (random()*10))
    sleep(1)
 

  elif caminho == 4:
    informacoes()

  elif caminho == 5:
    exit()

  else:
    print('\nOpção inválida. Escolha uma opção entre 1 e 5.\n')