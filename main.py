import methods as forca
import boneco as toy

while True:# Roda o jogo
    tentativas = []
    vidas = forca.start()

    idioma = forca.escolher_idioma()
    lista_boneco = toy.boneco_por_diff(vidas)
    word , dica = forca.get_word(vidas , idioma)

    forca.play(word, vidas, tentativas , lista_boneco , dica)

    escolha = input("\nVocê deseja jogar novamente?\n1.SIM\n2.NAO\n-> ") # Pergunta se o usuário quer jogar novamente
    if escolha == "1" or escolha.upper() == "SIM":
        continue
    else:
        break
        exit()
