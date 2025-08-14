nome = input("Digite seu nome: ")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print("você é: ABAIXO DO PESO 😁😁😁")
    print("É importante manter uma alimentação saudável.")
elif imc < 24.9:
    print("você tem: PESO NORMAL 🙂🙂🙂")
    print("Continue assim!")
elif imc < 29.9:
    print("você tem: SOBREPESO 😬😬😬")
    print("Cuidado com a alimentação e pratique exercícios!")
elif imc < 34.9:
    print("você tem: OBESIDADE GRAU 1 😟😟😟")
    print("É importante consultar um médico para orientações.")
elif imc < 39.9:
    print("você tem: OBESIDADE GRAU 2 😢😢😢")
    print("É fundamental buscar ajuda profissional.")
elif imc >= 40:
    print("você tem: OBESIDADE GRAU 3 😱😱😱")
    print("É crucial procurar um médico imediatamente.")
else:
    print("você tem: OBESIDADE 😧🤒")
    print("É importante buscar ajuda profissional.")

print(f"o imc do aluno {nome} é: {imc:.2f}")