
conjunto1 = set(input("Digite os valores do conjunto 1:"))
conjunto2 = set(input("Digite os valores do conjunto 2:"))

uniao = (conjunto1 | conjunto2)
print("\nO valor da União dos conjuntos 1 e 2 é:", uniao) 


intersecao = conjunto1 & conjunto2
print("\nO valor da Interseção dos conjuntos 1 e 2 é:", intersecao)  


diferenca = conjunto1 - conjunto2
print("\nO valor da diferença dos conjuntos 1 e 2 é:", diferenca)  


diferenca_simetrica = conjunto1 ^ conjunto2
print("\nO valor da diferença simétrica dos conjuntos 1 e 2 é:", diferenca_simetrica)