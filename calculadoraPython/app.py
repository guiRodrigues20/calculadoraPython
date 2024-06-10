
def adicionar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y


def calculadora():
    while True:
        # Exibe o menu de opções
        print("\nSelecione a operação desejada:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        
        escolha = input("Digite a opcao (1/2/3/4/5): ")

     
        if escolha == '5':
            print("Saindo da calculadora. Até logo!")
            break

       
        if escolha in ['1', '2', '3', '4']:
            try:
                
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                # Trata erro de entrada inválida
                print("Entrada inválida. Por favor, digite números válidos.")
                continue

           
            if escolha == '1':
                print(f"Resultado: {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                print(f"Resultado: {resultado}")
        else:
            
            print("Opção inválida. Por favor, escolha uma opção válida.")


calculadora()
