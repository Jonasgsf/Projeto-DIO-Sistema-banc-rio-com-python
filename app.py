menu = '''

    (d) Depositar
    (s) Sacar
    (e) Extrato
    (q) Sair

'''
saldo = 0

extrato = ""

qtd_saque = 0

MAX_SAQUE_DAY = 3

MAX_SAQUE_VALUE = 500

while True:
    entrada = input(menu)

    match entrada:
        case "d":
            while True :
                valor_deposito = float (input("insira o valor de depósito desejado :"))
                if valor_deposito <= 0:
                    print("valor inváido, tente novamente")
                    continue
                else :
                    saldo += valor_deposito
                    extrato += f'''Depósito no valor de : {valor_deposito}\n'''
                    break

    

        case "s":
                
                if saldo == 0:
                    print("Sem saldo para saque, por favor efetue um deposito antes de realizar o saque")
                    
                elif (qtd_saque == MAX_SAQUE_DAY):
                    print("valor máximo de saques diario atingido, tente novamente em 24 horas")
                    
                else:
                    while True: 
                        valor_saque = float(input("informe o valor do saque : "))

                        if (valor_saque > MAX_SAQUE_VALUE):
                            print("o saque está fora do limite diário permitido, insira um novo valor")
                            continue

                        elif (valor_saque > saldo) or (valor_saque <= 0):
                            print(f'''saldo insuficiente ou inválido, por favor tente novamente. 
                                  Seu saldo é : {saldo}''')
                            continue
                        else:
                            saldo -= valor_saque
                            qtd_saque += 1
                            extrato += f'''saque no valor de : {valor_saque}\n'''
                            break
        case "e":
            print("=======EXTRATO=======")
            print("Sem movimentações" if not extrato else extrato )
            print("Saldo atual : R$ {:.2f}".format (saldo))
            

        case "q":
            break 

        case _: 
            print("operação inválida, tente novamente")
       
