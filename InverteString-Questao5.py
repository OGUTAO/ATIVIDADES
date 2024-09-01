#Questão 5:
#Python

def inverter_string(s):

    string_invertida = ""

    

    for i in range(len(s) - 1, -1, -1):

        string_invertida += s[i]

    

    return string_invertida



string_original = input("Informe a string que deseja inverter: ")



resultado = inverter_string(string_original)



print(f"String original: {string_original}")

print(f"String invertida: {resultado}")