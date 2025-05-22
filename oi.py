def checar(a):
    tamanho = len(str(a))
    original = a
    if tamanho in [13, 15, 16] and a > 0:
        soma = 0
        for i in range(tamanho):
            c = a % 10
            a = a//10
            if i % 2 != 0:
                c *= 2
                if c > 9:
                    c -= 9
            soma += c
        if soma % 10 == 0:
            if tamanho == 13 and original // 10 ** 12 == 4:
                print("visa")
            elif tamanho == 15 and original // (10 ** 13) in [34,37]:
                print("american express")
            elif original // (10 ** 15) == 4:
                print('visa')
            elif 51 <= (original // 10 ** 14) <= 55:
                print("mastercard")
            else:
                print('cartao valido porem nao reconhecido')
        else:
            print("invalido")

    else:
        print("insira um valor valido")


try:
    answer = int(input("x: "))
    checar(answer)
except ValueError:
    print("insira um valor válido")
