from random import*
executa = True

nomesmacho = ["Valente", "Thor", "Bruce", "Pretinho", "Hulk", "Zeus", "Monstro", "Sheik", "Duque"," Bob", " Tobby", "Chico", "Zeca", "Apolo", "Tom", "Juca"]

nomesfemea = ["Valentina", "Penélope", "Princesa", "Mel", "Pérola", "Amora", "Princesa", "Belinha", "Lisa", "Cleo", "Filó", "Cristal", "Mimi", " Rebecca"]


print("Serviço de escolha de nome para animal de estimação")
print("-----------------------")


sexo = input("Seu animal é macho ou fêmea?").lower()
macho = sexo
fêmea = sexo

print('''
Menu
    c = obter nome
    a = adicionar nome
    d = remover nome
    q = sair
''')

while executa == True:
    if sexo == macho:

        menuChoice = input("\n>_").lower()

        if menuChoice == 'c':

            print(f'Você deve chamar seu animal de estimação de {choice(nomesmacho)}.')

       

        elif menuChoice == 'a':
            itemToAdd = input("Adicione o nome:")
            if itemToAdd not in nomesmacho:
                nomesmacho.append(itemToAdd)
            else:
                print("Esse nome já está na lista.")

        elif menuChoice == 'd':
            itemToDelete = input("Insira o nome a ser removido:")
            if itemToDelete in nomesmacho:
               nomesmacho.remove(itemToDelete)
            else:
                print("O nome não está na lista!")

        elif menuChoice == 'p':
            print(nomesmacho)
        
        elif menuChoice == 'q':
            executa = False

        else:
            print("Insira uma opção válida!")

    if sexo == fêmea:

        menuChoice = input("\n>_").lower()

        if menuChoice == 'c':

            print(f'Você deve chamar seu animal de estimação de {choice(nomesfemea)}.')

       

        elif menuChoice == 'a':
            itemToAdd = input("Adicione o nome:")
            if itemToAdd not in nomesfemea:
                nomesfemea.append(itemToAdd)
            else:
                print("Esse nome já está na lista.")

        elif menuChoice == 'd':
            itemToDelete = input("Insira o nome a ser removido:")
            if itemToDelete in nomesfemea:
               nomesfemea.remove(itemToDelete)
            else:
                print("O nome não está na lista!")

        elif menuChoice == 'p':
            print(nomesfemea)
        
        elif menuChoice == 'q':
            executa = False

        else:
            print("Insira uma opção válida!")

