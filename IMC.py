nome = input("Digite seu nome: ")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print("você é: ABAIXO DO PESO 😁😁😁")
elif imc < 24.9:
    print("você tem: PESO NORMAL 🙂🙂🙂")
else:
    print("você tem: OBSIDADE 😧🤒")

print(f"o imc do aluno {nome} é: {imc: .2f}")
