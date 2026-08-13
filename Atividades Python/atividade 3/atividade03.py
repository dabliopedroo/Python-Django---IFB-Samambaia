def main():
  mb = int(input("Digite o tamanho do arquivo em MB: "))
  mbps = int(input("Digite a velocidade da internet (MBps): "))

  bits = mb*8
  segundos = bits/mbps
  minutos = segundos/60


  print("Velocidade aproximada de dowload em minutos: ", minutos)
main()
