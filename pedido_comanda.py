from acai_e_acompanhamentos import deseja_acompanhamentos, escolhe_sabor, tamanho

#Retorna o pedido e o valor total deste.
def comanda(tama, preco, sabor_base, escolhidos, valor_escolhidos):
    seu_pedido = []
    conta = []

    seu_pedido.append(f'Seu pedido é um {sabor_base} de {tama} Ele acompanha:{",".join([ac for ac in escolhidos])}')
    conta.append(preco + valor_escolhidos)

    return seu_pedido, conta


# Capta o pedido e retorna o resultado das outras funções. 
def pedido():
    tama, preco = tamanho()

    sabor_base = escolhe_sabor()

    escolhidos, valor_escolhidos = deseja_acompanhamentos()

    return tama, preco, sabor_base, escolhidos, valor_escolhidos


#Confirmar ou cancelar o pedido.
def confirmacao_pedido(seu_pedido, conta):
    conf = int(input('\n1. Confirmar o pedido\n2. Cancelar o pedido\n>> '))

    if conf == 1:
        print(f'{seu_pedido[0]}. O custo total é de {conta[0]}')

    elif conf == 2:
        print('Que pena. Cancelando o seu pedido.')
        exit()

    else:
        print('Digite uma opção válida!')
        conf = confirmacao_pedido(seu_pedido, conta)