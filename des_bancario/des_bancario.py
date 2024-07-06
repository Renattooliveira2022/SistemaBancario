from datetime import datetime
from time import sleep

hora_atual = datetime.now().hour
caixa = 0
limite = 500
saques_realizados = 0  # Contador de saques
max_saques = 3  # Número máximo de saques permitidos

            
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
sleep(0.3)  
print('                   SISTEMA BANCÁRIO"               ')
sleep(0.3)  
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('')
print(f'      SALDO ATUAL R$ {caixa}   ')

while True:
   
    opc = str(input("Escolha a operação desejada = [D] Depositar [E] D.Extrato [S]Saque [Q]Sair do Sistema: ")).upper()
    print()  
    if opc == "S":  
        if saques_realizados >= max_saques:
            print('Você atingiu o número máximo desaque permitidos')
        else:
            opc_s = float(input('Valor do Saque R$ '))         
            if opc_s > caixa:   
                print(f'Saldo Disponível R$ {caixa:.2f}')
                print('------------------------------------------------------------')
                print("Valor de saldo indisponível para saque. Escolha outra Opção!")
                print('------------------------------------------------------------')
            elif opc_s > limite:
                print('Lembrando que o limite para saque é até R$ 500.00')
            elif opc_s <= caixa:  
                caixa -= opc_s
                saques_realizados +=1 
                
                print(f'Saldo atual: R$ {caixa:.2f}')
                print(f'Saques restantes: {max_saques - saques_realizados}')
       
    elif opc == "D": 
          opc_d = float(input('Informe o valor de Depósito R$ ')) 
          caixa += opc_d
          print(f'Saldo Total R$ {caixa:.2f}')
    elif opc == "E":
              print("====EXTRATO====")
              print(f'Saldo Total R$ {caixa:.2f}')
              print('===============')     
    elif opc == "Q":
              print('Operação Finalizada!')
              break
    else:
        print('Opção Inválida! Tente Novamente.')

if hora_atual >= 00 and hora_atual <=12:
    print("Bom dia!")
elif hora_atual >12 and hora_atual <= 18:
    print("Boa tarde!")
else:
    print("Boa noite!")
# DESCRIÇÃO DAS VARIÁVEIS
# opc     → Pergunta de Opções
# opc_s   → Opção para sacar
# opc_d   → Opção para depósito
# opc_e   → Opção para extrato
# opc_q   → Opção para extrato
# caixa   → Tudo (saque, deposito e extrato)
# limite  → Limitando saque em R$ 500.00


