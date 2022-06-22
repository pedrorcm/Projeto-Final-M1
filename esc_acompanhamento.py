def esc_acompanhamentos():
    quantidade = 3
    escolha = 1, 2, 3, 4
    
    
    for rodada in range(1, quantidade +1):
      print("Complemento {} de {}".format(rodada, quantidade))
      escolha_acompanhamentos_str = int(input('Escolha um acompanhamento, por número: ')) 
      
      escolha_acompanhamentos  = int(escolha_acompanhamentos_str)
      
    
    if (escolha_acompanhamentos < 0) or (escolha_acompanhamentos > 12):
        print('Digite um acompanhamento válido.')
        
        complemento1 = escolha_acompanhamentos = escolha
        complemento2 = escolha_acompanhamentos = escolha
        complemento3 = escolha_acompanhamentos = escolha
        
        
    if(complemento1):
        print
    elif(complemento2):
        print    

    elif(complemento3):
        print
        
              
    
    
    rodada = rodada +1
    escolha_acompanhamentos = esc_acompanhamentos()
    
esc_acompanhamentos