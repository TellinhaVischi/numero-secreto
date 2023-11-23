prova1 = float(input("Digite a nota da sua prova 1: "))
prova2 = float(input("Digite a nota da prova 2: "))
prova3 = float(input("Digite a nota da prova 3: "))

media = (prova1 + prova2 + prova3)/3

if media >= 5:
    print("Você foi aprovado!")
else: 
    print("Que pena, você deverá estudar para sua prova de recuperação!")
