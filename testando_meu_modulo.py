import meu_modulo

nome = str(input("Digite seu nome: "))

meu_modulo.saudar(nome)

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))

resultado = meu_modulo.calcular_soma(numero_1, numero_2)

print("A soma dos números " + str(numero_1) + " e " + str(numero_2) + " é: " + str(resultado))