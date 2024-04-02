def menu():
    print("Selecione a conversão desejada:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = int(input("Digite o número da opção: "))
    return opcao

def celsius_para_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 1)

def fahrenheit_para_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 1)

opcao = menu()

def converter_numero(numero):
    if numero % 1 == 0:
        return int(numero)
    else:
        return float(numero)

temperatura = float(input("Digite a temperatura a ser convertida: "))
temperatura = converter_numero(temperatura)


if opcao == 1:
    resultado = celsius_para_fahrenheit(temperatura)
    resultado = converter_numero(resultado)
    print(f"{temperatura} Celsius equivalem a {resultado} Fahrenheit.")
elif opcao == 2:
    resultado = fahrenheit_para_celsius(temperatura)
    resultado = converter_numero(resultado)
    print(f"{temperatura} Fahrenheit equivalem a {resultado} Celsius.")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

