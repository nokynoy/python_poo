from frota import *

def operar_carro(carro : Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo(km/h)  : "))
        carro.acelerar(v, t)

if __name__ == "__main__":
    print('Cadastre o 1° carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros= float(input('Quantos litros no tanque'))
    cm= float(input('Qual consumo médio'))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, True, litros, cm)

    print('Cadastre o 2° carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Quantos litros no tanque'))
    cm = float(input('Qual consumo médio'))
    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, True, litros, cm)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600 and(carro1.tanque>0 and carro2.tanque>0):
        try:
            op = 0
            while op not in (1, 2):
                op = int(input("Qual carro [1,2]?"))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

            print('Infos atuais do carro')
            print(carro1)
        except Exception as e:
            print("Erro!")
            print(e)

    if carro1.motor_on:
        carro1.desligar()
    if carro2.motor_on:
        carro2.desligar()

    print(carro1)
    print(carro2)

    if carro1.odometro >= 600:
        print("O 1° carro ganhou")
    elif carro2.odometro >= 600:
        print("O 2° carro ganhou")
    elif carro1.tanque == 0:
        print("Acabou o tanque ")
    else:
        print("Acabou o tanque ")
