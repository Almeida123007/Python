valor_total = float(input("Digite valor total: "))
porcentagem =float(input("Digite a porcentagem: "))

valor_porcentagem = valor_total * (porcentagem / 100)

print(f"o valor de: {porcentagem} % de {valor_total} é: {valor_porcentagem: .1f}")