if __name__ == '__main__':
    peso=float(input("Qual é seu peso?"))
    altura= float(input("Qual é sua altura?"))
    imc= peso/ (altura ** 2)
    print('IMC dessa pessoa é de {:.1f}'.format(imc))
    if imc <= 18.5:
        print("você está abaixo do peso")
    elif imc <= 25:
        print("Parabéns, você está na faixa de peso normal")
    elif imc <= 30:
        print("Você está em sobrepeso")
    else:
        print("Você esta obeso, cuidado!")



