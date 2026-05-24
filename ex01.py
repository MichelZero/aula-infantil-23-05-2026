# autor: Michel
# data: 23/05/2026

# Criar um programa que peça números 
# ao usuário e vá somando-os. 
# O programa deve parar e exibir o total 
# apenas quando o usuário digitar o número 0.

soma = 0
print("informe número ZERO para finalizar!")

while True:
  valor = int(input("informe um valor [0 -> stop]: "))
  if valor == 0:
    pass
  soma = soma + valor
  
print(f"o total foi de {soma}")