
#AVALIAÇÃO1 
## Alunos: Pedro H. O. Marques e Rodrigo Meireles


def consulta(conta):
  print(f"Seu saldo atual eh de R${conta}")
  
# saca o valor da conta, diminuindo do saldo atual
def sacar(conta):
  print(f"\nSeu saldo atual eh de: R${conta} \n")

  saque = float(input("Digite o valor que deseja retirar da sua conta: "))
  if saque < conta:
    conta = conta - saque
    print(f"Seu saldo atual eh de: R${conta}")
  
  else:
    print ("\nSaldo insuficiente...\n")

  return conta
    
#altera valor atual adicionando o valor depositado    
def depositar(conta):
  deposito = float(input("Digite o valor que gostaria de adicionar a sua conta: "))

  conta = conta + deposito
  print(f"\nSeu saldo atual eh de R${conta}\n")

  return conta

#função principal do menu
def main ():
  conta = 200

  while True:
    print("===Menu===\n")
    print("===1 - Depositar===")
    print("===2 - Sacar===")
    print("===3 - Consultar===")
    print("===4 - Sair===\n")
    print("===========\n")
  

    menu = (int(input("Digite o que gostaria de acessar no menu: ")))

    match menu:
      case 1:
        #chama a função depositar em conta
        conta = depositar(conta)

      case 2:
        #chama a função de saque em conta
        conta = sacar(conta)
      
      case 3:
        #chama a função de consultado do saldo em conta
        consulta(conta)
      
      case 4:
        #sai do loop
        print("Saindo...")
        break
      case _:
        print("Invalido")
      

main()
