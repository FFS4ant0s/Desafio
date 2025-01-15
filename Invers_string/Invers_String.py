def inverter_string(s):
    inversa = ""
    for i in range(len(s)-1, -1, -1):
        inversa += s[i]
    return inversa


string = input("Digite uma string para inverter: ")
print(f"A string invertida é: {inverter_string(string)}")
