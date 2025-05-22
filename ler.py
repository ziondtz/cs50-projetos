

def analise(text):
    empalavras = False
    palavras = 0
    emfrases = False
    frases = 0
    letras = 0
    for i in text:
        if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
            letras += 1
        if i == " ":
            empalavras = False
        elif i != " " and empalavras == False:
            empalavras = True
            palavras += 1
        if i in [".", "?", "!"]:
            emfrases = False
        elif i not in [".", "?", "!"] and emfrases == False:
            emfrases = True
            frases += 1
    return palavras, frases, letras

text = input("text: ")
palavras, frases, letras = analise(text)
index = round(0.0588 * (letras * 100 / palavras) - 0.296 * (frases * 100 / palavras) - 15.8)
if index < 1:
    print("before grade 1")
elif index >= 16:
    print("grade 16+")
else:
    print(f"grade {index}")
