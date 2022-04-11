
opcao = 0

while opcao != 3:    

    print('MENU')
    print('1. Celsius para Fahrenheit')
    print('2. Fahrenheit para Celsius')
    print('3. Sair')

    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
        celsius = float(input('Digite a temperatura em Celsius: '))
        fahrenheit = (celsius/5)*9 + 32
        print(celsius, '°C =', fahrenheit, '°F')


    elif opcao == 2:
        fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        celsius = (fahrenheit-32)/9*5
        print(fahrenheit, '°F =', celsius, '°C')

    elif opcao != 3:
        print('Opção inválida!')
  

print('Obrigado por executar!')


'''
if opcao == 1:
        repetir = 's'
        while repetir == 's':
            celsius = float(input('Digite a temperatura em Celsius: '))
            fahrenheit = (celsius/5)*9 + 32
            print(celsius, '°C =', fahrenheit, '°F')
            repetir = input('Deseja fazer mais conversões °C/°F (s/n): ')
'''