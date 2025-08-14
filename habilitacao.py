nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
possui_carteira = input("1-sim | 2-não: ")

if idade >= 18:
    print("maior de idade !!")
    if possui_carteira == "sim":
        print("Pode DIRIGIR")
    else:
     print("NÃO PODE DIRIGIR !!")
else:
   print("menor de idade !!")