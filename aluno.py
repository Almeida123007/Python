nome = input("Digite seu nome: ")

nota_1 = float(input("digite a primeira nota: "))
nota_2 = float(input("digite a segunda nota: "))
nota_3 = float(input("digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"A média de {nome} é {media:.2f}")

if media >= 7:
    print(f"Parabéns {nome}, você foi aprovado!😁😁😁 sua média foi {media:.2f}!")
elif media >= 4:
    print(f"Desculpe {nome}, você está de recuperação!😰😰😰 sua média foi {media:.2f}")
else:
    print(f"Infelizmente {nome}, você foi reprovado!😢😢😢 sua média foi {media:.2f}")
