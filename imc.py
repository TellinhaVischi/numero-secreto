# Para calcular o indice de massa corporea (imc)
# imc = seu peso (em kg) / altura ** 2

# Vamos fazer uma calculadora de imc em python

peso = float(input("Coloque o seu peso: "))

altura = float(input("Qual a sua altura? "))

imc = peso / (altura ** 2)

if imc <=18.5:
    print("Cuidado, procure um médico! Você está abaixo do peso!")
elif imc >= 18.6 and imc <= 24.9:
    print("Parabéns, você está no peso ideal!")