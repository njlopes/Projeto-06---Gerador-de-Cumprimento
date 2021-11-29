from random import*

print("Gerador de Cumprimentos")
print("--------------------")

adjetivos = ["maravilhoso", "acima da média", "excelente","incrível","espetacular", "esplêndido", "fantástico", "extraordinário"]
hobbies = ["andar de bicicleta", "programar", "fazer chá", "desenhar", "cozinhar"]


nome = input("Qual é o seu nome?:")
print("Aqui está o seu cumprimento", nome,":")




print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
print("De nada!")
