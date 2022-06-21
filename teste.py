'''teste = [1,2,3,4,5,5.5]


print(sum(teste))
'''



def comanda(sabor_base, tama, escolhidos, preco, valores_escolhidos, m1):
    seu_pedido = []
    conta = []

    if m1 is True:
      seu_pedido.append(f'E também um {sabor_base} de {tama}. Ele acompanha {"".join(x for x in escolhidos)}.')
      conta.append(preco + valores_escolhidos)
    else:
      seu_pedido.append(f'Seu pedido é um {sabor_base} de {tama}. Ele acompanha{"".join(x for x in escolhidos)}.')
      conta.append(preco + valores_escolhidos)

    return seu_pedido, conta

print(comanda('acai', '300ml', [' morango', ' banana'], 9.50, 1, False))
print(comanda('acai', '300ml', [' morango', ' banana'], 9.50, 1, True))