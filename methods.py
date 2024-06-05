''' Jogo da Forca '''
import random
import os

def start(): # Função encarregada de dar a mensagem inicial para o jogador, e fazê-lo escolher a dificuldade

    os.system('clear')
    msg_terminal = '''
    Bem vindo ao jogo da forca!
    Selecione seu nível de dificuldade:
    - EASY (15 vidas), 
    - MEDIUM (10 vidas), 
    - HARD (5 vidas) 
     -> '''
    dificuldades = {"EASY":15, "MEDIUM":10, "HARD":5}

    while True:
        entrada = input(msg_terminal).upper()
        vidas = dificuldades.get(entrada, -1)
        if vidas < 1:
            print("Dificuldade inválida, tente novamente!")
        else:
            break

    print("Dificuldade selecionada:", vidas,  "vidas.")
    print("_____________________________________________________________________")
    return vidas



def get_word(): # Obtém a palavra. Essa função deve ser alterada
    words = [
    'Pedra',
    'Papel',
    'Tesoura',
    'Vasco',
    'Camacho',
    'Thevez'
            ]
    word = random.choice(words).upper()
    return word

def get_display_word(word, tentativas): # Essa fução configura a palavra oculta a ser exibida na tela (ex: "B_C___")

    display_word = ""
    for letter in word:
        if letter in tentativas:
            display_word += letter
        else:
            display_word += "_"

    return display_word


def msg_round(display_word, tentativas, vidas): # Essa função cria a mensagem de cara Round
    print("Sua palavra é", display_word)
    print("Você já usou as letras", tentativas)
    print(">>>> Você possui ", vidas, "vidas. <<<<")

def get_hint_letter(): # Função que recebe a letra do jogador, adapta ela para ser lida
    while True:

        hint_letter = input("Dê uma letra: ")
        if hint_letter:
            hint_letter = hint_letter.upper()
            break
        else:
            print("Input inválido, tente novamente!")

    return hint_letter

####################################################################################################################

def play(word, vidas, tentativas): # Aqui é como o jogo vai rodar

    while True: # loop infinito dos crias

        os.system('clear')

        display_word = get_display_word(word, tentativas) 

        player_status = (display_word == word) # Verifica se o jogador já ganhou ou não

        if player_status:   # Mensagem se o cabra ganhar
            print("VOCÊ GANHOU")
            print("A palavra era: ", word)
            break

        elif vidas > 0: # Ele não ganhou mas tem vidas
            msg_round(display_word, tentativas, vidas)

            hint_letter = get_hint_letter()

            if hint_letter in tentativas:
                print("-------------- Você já digitou essa letra antes. Tente novamente -----------------")
            elif hint_letter in word:
                print("--------------------------------- Excelente! -------------------------------------")
                tentativas.append(hint_letter)
            else:
                print("--------------------------- ERROUUU KKKKKKKKKKKKKK -------------------------------")
                tentativas.append(hint_letter)
                vidas += -1

        else: # perdeu kkkkkkkkk
            print("PERDEU KKKKKKKKK")
            print("A palavra era: ", word)
            break



