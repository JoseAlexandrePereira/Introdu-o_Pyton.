'''Leia os valores de dois pontos flutuantes de dupla precisão A e B, correspondentes às notas de dois alunos. Após isso, calcule a média do aluno, considerando que a nota A tem peso 3,5 e a B tem peso 7,5. Cada nota pode ser de zero a dez, sempre com um dígito após a vírgula. Não se esqueça de imprimir o final da linha após o resultado, caso contrário você receberá “Erro de apresentação”. Não se esqueça do espaço antes e depois do sinal de igual.

Entrada
O arquivo de entrada contém valores de 2 pontos flutuantes com um dígito após o ponto decimal.

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo a seguir, com 5 dígitos após a vírgula e com um espaço em branco antes e depois do sinal de igual.'''

def calcular_media():
    peso_1 = 3.5
    peso_2 = 7.5

    while True:
        try:
            nota_1 = float(input("Insira sua nota 1: "))
            nota_2 = float(input("Digite sua nota 2: "))
            
            if nota_1 < 0 or nota_1 > 10.0 or nota_2 < 0 or nota_2 > 10.0:
                print("ERRO: Digite uma nota válida.")
            else:
                media = ((nota_1 * peso_1) + (nota_2 * peso_2)) / (peso_1 + peso_2)
                media_arredondada = round(media, 5) #irá 
                print("MÉDIA = " + str(media_arredondada))
                
                if media_arredondada > 6.0:
                    print("\nAluno APROVADO.\n")
                elif media_arredondada <= 4.0:
                    print("\nAluno REPROVADO.\n")
                else:
                    print("\nAluno de RECUPERAÇÃO.\n")
                
                break  # Sai do loop se as notas forem válidas e a média for calculada
        except ValueError:
            print("ERRO: Insira um número válido para as notas.")

def main():
    while True:
        calcular_media()
        resposta = input("Deseja calcular outra média? (s/n): ").strip().lower()
        if resposta != 's':
            break
    print("Programa encerrado")

# Chama a função principal para executar
main()
