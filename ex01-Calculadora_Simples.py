# 1. Calculadora Simples: Crie um programa que permita ao usuário realizar operações matemáticas básicas (adição, subtração, multiplicação e divisão) e exiba o resultado.

def calculadora_simples():
    print("\n\nCalculadora:\n\n")
    
    operacao = set(input("Informe a operação que você deseja:\n1. SOMA.\n2. SUBTRAÇÃO\n3. MULTIPLICAÇÃO\n4. DIVISÃO.\n"))
    
    if operacao == 1:
        for