#Funções são basicamente bloco de código projetado para executar alguma tarefa específica, com a ideia de poder reutiliza-las em algum momento no futuro em nosso código. 

def calcular_media(*numeros):
    
    soma = sum(numeros)
    quantidade = len(numeros)  
    media = soma / quantidade 
    return media  

print("Média:", calcular_media(10, 20, 30))   

def sumar_3(x):
    
    return x + 3  


sumar = lambda x: x + 3

print("Somar 3 a um número:", sumar(5)) 