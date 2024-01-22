print("****************************")
print("*****JOGO DE ADVINHAÇÃO*****")
print("****************************")

import random
numero = random.randint(0,99)   #Valor atribuído a variável numero para ser advinhado

print("\nBem-vindo ao jogo de advinhar qual número é!")
print("Escolha o nível de dificuldade abaixo:")
print("Nível 1 = 15 chances\nNível 2 = 10 chances\nNível 3 = 5 chances")

#Abaixo foi criado uma condição para receber a 
#decisão do usuário em relação ao nível de dificuldade
chances = 0
while chances != 1 and 2 and 3:
    try:

        chances = int(input("\nDigite 1 para nível 1, 2 para nível 2 ou 3 para nível 3: "))
        nivel_1 = chances == 1
        nivel_2 = chances == 2
        nivel_3 = chances == 3
        if (nivel_1):
            print("\nVocê tem 15 chances")
            chances = 15
            break
        elif (nivel_2):
            print("\nVocê tem 10 chances")
            chances = 10
            break
        elif (nivel_3):
            print("\nVocê tem 5 chances")
            chances = 5
            break
        else:
            print("\nValor inválido. Por favor digite um número entre 1, 2 e 3.")
            
    except ValueError:
        print("\nValor inválido. Por favor digite um número entre 1, 2 e 3.")

rodada = 0
while rodada != chances:

    print("\nO número misterioso está entre 0 e 99. Boa sorte!")
    for rodada in range(1, chances + 1):  #Foi usado o loop for e atribuído parâmetros 
                                          # a função range
        try:        
            print("\nChance {} de {}".format(rodada, chances))
            
            palpite = int(input("\nDigite um número: "))

            acertou = palpite == numero #Foi atribuído as condicionais dentro de outra variável
            maior = palpite > numero #assim o código fica mais bem organizado
            menor = palpite < numero 

            if (acertou):
                print("\n** Você acertou!! **\n")
                break
            elif (maior):
                print("\nVocê errou! Seu palpite foi maior que o número secreto.")
                if(rodada == chances):
                    print(f"\nVocê não conseguiu desta vez! O número era: {numero}")
                    break
            elif (menor):
                print("\nVocê errou! Seu palpite foi menor que o número secreto.")
                if(rodada == chances):
                    print(f"\nVocê não conseguiu desta vez! O número era: {numero}")#Aqui, caso o 
        # usuário não acerte, será mostrado qual era o número secreto
                    break
                    
        except NameError:
            print("\nValor incorreto. Digite um número.")
        except ValueError:
            print("\nValor incorreto. Digite um número.")

    print("\n>>>Fim de jogo!<<<")
    break