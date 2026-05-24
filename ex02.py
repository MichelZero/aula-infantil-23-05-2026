# autor: Michel
# data: 23/05/2026

# Criar um programa que peça números 
# ao usuário e vá somando-os. 
# O programa deve parar e exibir o total 
# apenas quando o usuário digitar o número 0.
# informe quantos número foram adicionado a soma.

soma = 0 # variável para armazenar a soma dos números
quant = 0 # variável para armazenar a quantidade de números digitados
print("informe o número ZERO para finalizar!")

while True:
  valor = int(input("informe um valor [0 -> stop]: "))
  if valor == 0:
    break
  soma = soma + valor 
  quant = quant + 1
  
print(f"o total foi de {soma}")
print(f"a quantidade foi de {quant}")
media = soma/quant
print(f"a média foi de {media}")