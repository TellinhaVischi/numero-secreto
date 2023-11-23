prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
prova3 = float(input("Digite a nota da terceira prova: "))

media = (prova1 + prova2 + prova3)/3

if media >= 5:
    print("Parabéns, você passou e não está de recuperação!")
else:
    print("Poxa vida, você ficou de recuperação!")