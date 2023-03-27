'''
- Linhas de código caso tenha acertado.
 resp2 = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
            if resp2 == "nao":
                print("Tudo bem! ")
                x = False
            elif resp2 == "sim":
                print("Reiniciando... ")
            else:
                print("Não entendi! Obrigado por jogar! ")
                x = False
'''
'''
- Vamo dnv
- Substituir numteste pelo valor da dificuldade
'''
x = True
while x == True:
    import random
    #numteste = 5
    #numteste2 = 15
    #numteste3 = 3
    #num = 1
    num = random.randint(1,3)
    difi = random.randint(1,10)
    difi2 = random.randint(11,25)
    difi3 = random.randint(26,50)
    if num == 1: #Dificuldade 1 - difi
        print("Dificuldade fácil(Números de 1 a 10). Boa sorte ")
        chute = int(input("Vamos, chute um número! "))
        if chute == difi:
            perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
            if perg == "nao":
                print("Tudo bem! ")
                x = False
            elif perg == "sim":
                print("Reiniciando... ")
            else:
                print("Não entendi! Obrigado por jogar! ")
                x = False
        if chute < difi: #1- Tentativa
            resp1 = int(input("Eita, chutou abaixo... Tenta de novo "))
            if resp1 < difi: #2- Tentativa
                resp2 = int(input("Abaixo de novo... Tenta de novo, última chance "))
                if resp2 < difi: #3- Tentativa
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                    x = False
                elif resp2 == difi:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
            elif resp1 == difi:
                perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                if perg == "nao":
                    print("Tudo bem! ")
                    x = False
                elif perg == "sim":
                    print("Reiniciando... ")
                else:
                    print("Não entendi! Obrigado por jogar! ")
                    x = False
            elif resp1 > difi:
                resp2 = int(input("Eita... Foi acima... Tenta de novo, última chance "))        
                if resp2 == difi:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 < difi:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False

        if chute > difi: #1- Tentativa
            resp1 = int(input("Eita, chutou acima... Tenta de novo "))
            if resp1 < difi: #2- Tentativa
                resp2 = int(input("Dessa vez foi abaixo... Última chance "))
                if resp2 < difi: #3- Tentativa
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                    x = False
                elif resp2 == difi:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
            elif resp1 == difi:
                perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                if perg == "nao":
                    print("Tudo bem! ")
                    x = False
                elif perg == "sim":
                    print("Reiniciando... ")
                else:
                    print("Não entendi! Obrigado por jogar! ")
                    x = False
            elif resp1 > difi:
                resp2 = int(input("Eita... Foi acima... Tenta de novo, última chance "))        
                if resp2 == difi:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 < difi:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False

    if num == 2: #Dificuldade 2 - difi2
        print("Dificuldade média(Números de 11 a 25). Boa sorte ")
        chute = int(input("Vamos, chute um número! "))
        if chute == difi2:
            perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
            if perg == "nao":
                print("Tudo bem! ")
                x = False
            elif perg == "sim":
                print("Reiniciando... ")
            else:
                print("Não entendi! Obrigado por jogar! ")
                x = False
        if chute < difi2: #1- Tentativa
            resp1 = int(input("Eita, chutou abaixo... Tenta de novo "))
            if resp1 < difi2: #2- Tentativa
                resp2 = int(input("Abaixo de novo... Tenta de novo, última chance "))
                if resp2 < difi2: #3- Tentativa
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                    x = False
                elif resp2 == difi2:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi2:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
            elif resp1 == difi2:
                perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                if perg == "nao":
                    print("Tudo bem! ")
                    x = False
                elif perg == "sim":
                    print("Reiniciando... ")
                else:
                    print("Não entendi! Obrigado por jogar! ")
                    x = False
            elif resp1 > difi2:
                resp2 = int(input("Eita... Foi acima... Tenta de novo, última chance "))        
                if resp2 == difi2:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi2:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 < difi2:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False

        if chute > difi2: #1- Tentativa
            resp1 = int(input("Eita, chutou acima... Tenta de novo "))
            if resp1 < difi2: #2- Tentativa
                resp2 = int(input("Dessa vez foi abaixo... Última chance "))
                if resp2 < difi2: #3- Tentativa
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                    x = False
                elif resp2 == difi2:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi2:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
            elif resp1 == difi2:
                perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                if perg == "nao":
                    print("Tudo bem! ")
                    x = False
                elif perg == "sim":
                    print("Reiniciando... ")
                else:
                    print("Não entendi! Obrigado por jogar! ")
                    x = False
            elif resp1 > difi2:
                resp2 = int(input("Eita... Foi acima... Tenta de novo, última chance "))        
                if resp2 == difi2:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi2:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 < difi2:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False

    if num == 3: #Dificuldade 3 - difi3
        print("Dificuldade difícil(Número de 26 a 50). Boa sorte ")
        chute = int(input("Vamos, chute um número! "))
        if chute == difi3:
            perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
            if perg == "nao":
                print("Tudo bem! ")
                x = False
            elif perg == "sim":
                print("Reiniciando... ")
            else:
                print("Não entendi! Obrigado por jogar! ")
                x = False
        if chute < difi3: #1- Tentativa
            resp1 = int(input("Eita, chutou abaixo... Tenta de novo "))
            if resp1 < difi3: #2- Tentativa
                resp2 = int(input("Abaixo de novo... Tenta de novo, última chance "))
                if resp2 < difi3: #3- Tentativa
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                    x = False
                elif resp2 == difi3:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi3:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
            elif resp1 == difi3:
                perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                if perg == "nao":
                    print("Tudo bem! ")
                    x = False
                elif perg == "sim":
                    print("Reiniciando... ")
                else:
                    print("Não entendi! Obrigado por jogar! ")
                    x = False
            elif resp1 > difi3:
                resp2 = int(input("Eita... Foi acima... Tenta de novo, última chance "))        
                if resp2 == difi3:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi3:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 < difi3:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False

        if chute > difi2: #1- Tentativa
            resp1 = int(input("Eita, chutou acima... Tenta de novo "))
            if resp1 < difi2: #2- Tentativa
                resp2 = int(input("Dessa vez foi abaixo... Última chance "))
                if resp2 < difi2: #3- Tentativa
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                    x = False
                elif resp2 == difi3:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi3:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
            elif resp1 == difi3:
                perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                if perg == "nao":
                    print("Tudo bem! ")
                    x = False
                elif perg == "sim":
                    print("Reiniciando... ")
                else:
                    print("Não entendi! Obrigado por jogar! ")
                    x = False
            elif resp1 > difi3:
                resp2 = int(input("Eita... Foi acima... Tenta de novo, última chance "))        
                if resp2 == difi3:
                    perg = input("Parabéns, você acertou. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 > difi3:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False
                elif resp2 < difi3:
                    print("Agora já era...")
                    perg = input("É uma pena, você perdeu. Deseja jogar de novo? Responda com sim ou nao. ")
                    if perg == "nao":
                        print("Tudo bem! ")
                        x = False
                    elif perg == "sim":
                        print("Reiniciando... ")
                    else:
                        print("Não entendi! Obrigado por jogar! ")
                        x = False