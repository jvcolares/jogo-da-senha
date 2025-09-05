import random

print("------Jogo da Senha-----")

digito_senha0=int(random.randint(0,4))
digito_senha1=int(random.randint(0,4))
digito_senha2=int(random.randint(0,4))
digito_senha3=int(random.randint(0,4))

acertou = False

tentativas = 4
i = 0
while not acertou and i < tentativas:
    print(f"Tentativa numero:{i}")
    print(f"Tente adivinhar a senha")
    print(f"Digite 4 dígitos entre 0 e 4 sucessivamente")

    escolha0=int(input())
    escolha1=int(input())
    escolha2=int(input())
    escolha3=int(input())

    num_acertos = 0

    if digito_senha0 == escolha0:
        print(digito_senha0,end="")
        num_acertos += 1
    else: print("*", end="")

    if digito_senha1 == escolha1:
        print(digito_senha1,end="")
        num_acertos += 1
    else: print("*", end="")

    if digito_senha2 == escolha2:
        print(digito_senha2,end="")
        num_acertos += 1
    else: print("*", end="")

    if digito_senha3 == escolha3:
        print(digito_senha3,end="")
        num_acertos += 1
    else: print("*", end="")

    i = i + 1



