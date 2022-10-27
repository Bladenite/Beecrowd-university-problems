#Huaauhahhuahau

risada = [*input()]

vogais = ["a", "e", "i" , "o", "u"]
risada_final = [letra for letra in risada if letra in vogais]
risada_final_copia = risada_final[:]
risada_final_copia.reverse()
if risada_final == risada_final_copia:
    print("S")
else:
    print("N")

