menu="""
---------------------------------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
---------------------------------------
=> """

saldo = 0
limite = 500
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao= input(menu)
    opcao = opcao.lower()
    
    if opcao=="d":
        print("Deposito")
        deposito = int (input("quanto deseja depositar: "))
        if deposito > 0:
            saldo +=deposito
            extrato+=f"Deposito: R$ {deposito:.2f} \n"
            print ("SALDO TOTAL = " , saldo)
        else:
            print("Valor não permitido")
    elif opcao=="s":
        print("Sacar")
        if numero_saques<3:
            numero_saques +=1
            saque = int(input("quanto deseja sacar: "))
            if saque<=limite and saque<saldo:
                saldo -= saque
                extrato+=f"Saque R$ {deposito:.2f} \n"

                print ("SALDO TOTAL = " , saldo)
            else:
                print("Saldo insuficiente ou limite excedido")
        else:
            print("limite de saque excedido")    

    elif opcao=="e":
        print ("----------- Extrato ---------")
        print(extrato)
        print ("SALDO TOTAL = " , saldo)
        print("---------------------------------")

    elif opcao=="q":
        break
    else:
        print("Essa opção não existe")