''' Jogo da Forca '''
import os
import string
import GPT

def start(): # Função encarregada de dar a mensagem inicial para o jogador, e fazê-lo escolher a dificuldade

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    msg_terminal = '''
    Bem vindo ao jogo da forca!
    Selecione seu nível de dificuldade:
    - 1.EASY (15 vidas), 
    - 2.MEDIUM (10 vidas), 
    - 3.HARD (5 vidas) 
     -> '''
    dificuldades = {"EASY":13, "MEDIUM":8, "HARD":5, "1":13, "2":8, "3":5}

    while True: # Verifica a dificuldade selecionada e coloca a quantidade de vidas correspondente
        entrada = input(msg_terminal).upper()
        vidas = dificuldades.get(entrada, -1)
        if vidas < 1:
            print("Dificuldade inválida, tente novamente!")
        else:
            break

    print("Dificuldade selecionada:", vidas,  "vidas.")
    print("_____________________________________________________________________")
    return vidas

def escolher_idioma(): # Pede para o usuário um idioma para a palavra, caso ele não digite nada, o valor padrão será português
    idioma = input("Escolha o idioma da palavra secreta: ")
    if idioma == "":
        idioma = "Português"
    return idioma


def get_word(vidas, idioma): # Coleta a palavra e a dica do chat gpt
    dificuldades = {13:"Fácil" , 8:"Médio" , 5:"Difícil"}
    word, dica = GPT.gerador_palavra(dificuldades.get(vidas) , idioma)
    word = word.upper()
    return word , dica

def get_display_word(word, tentativas): # Essa fução configura a palavra oculta a ser exibida na tela (ex: "B_C___")

    display_word = ""
    for letter in word:
        if letter in tentativas:
            display_word += letter
        else:
            display_word += "_"

    return display_word


def msg_round(display_word, tentativas, vidas, lista_boneco, dica): # Essa função cria a mensagem de cara Round
    print("Sua palavra é", display_word)
    print("Quantidade de letras:" , len(display_word))
    print("Dica:" , dica)
    print("Você já usou as letras", tentativas)
    print(">>>> Você possui ", vidas, "vidas. <<<<")
    print(lista_boneco[-(int(vidas)+1)])

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

def play(word, vidas, tentativas, lista_boneco , dica): # Aqui é como o jogo vai rodar

    while True: # loop infinito dos crias

        display_word = get_display_word(word, tentativas) 

        player_status = (display_word == word) # Verifica se o jogador já ganhou ou não

        if player_status:   # Mensagem se o cabra ganhar
            print("VOCÊ GANHOU")
            print("A palavra era:", word)
            break

        elif vidas > 0: # Ele não ganhou mas tem vidas
            msg_round(display_word, tentativas, vidas, lista_boneco , dica)

            hint_letter = get_hint_letter()

            if hint_letter in tentativas: # Verifica se o chute do usuário é uma palavra, uma letra ou inválido e faz as tarefas necessárias
                print("-------------- Você já digitou essa letra antes. Tente novamente -----------------")
                input("Pressione qualquer tecla para continuar ")
            elif hint_letter in word and len(hint_letter) == 1:
                print("--------------------------------- Excelente! -------------------------------------")
                input("Pressione qualquer tecla para continuar ")
                tentativas.append(hint_letter)
            elif len(hint_letter) == len(word):
                chute = input("Este é o seu chute da palavra?\n1.SIM\n2.NA0\n-> ")
                if (chute == "1" or chute.upper() == "SIM") and hint_letter == word:
                    print("VOCÊ GANHOU")
                    print("A palavra era:", word)
                    break
                else:
                    print("Você errou a palavra, perdeu o JOGO!")
                    print(lista_boneco[-1])
                    print("A palavra era: ", word)
                    break

            elif hint_letter in string.ascii_letters and len(hint_letter) == 1:
                print("--------------------------- ERROUUU KKKKKKKKKKKKKK -------------------------------")
                tentativas.append(hint_letter)
                vidas += -1
                input("Pressione qualquer tecla para continuar ")
            else:
                print("----------------- Você digitou algo inválido. Tente novamente --------------------")
                input("Pressione qualquer tecla para continuar ")

            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')


        else: # Jogador perdeu todas as vidas
            print("PERDEU KKKKKKKKK")
            print(lista_boneco[-1])
            print("A palavra era: ", word)
            break

        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')




