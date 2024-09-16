from datetime import datetime

ano_nascimento = int(input("Informe o ano em que você nasceu: "))

hoje = datetime.now()

idade = hoje.year - ano_nascimento

print(f"Sua idade é: {idade}")
