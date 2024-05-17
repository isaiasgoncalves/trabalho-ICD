import methods as forca


tentativas = []
vidas = forca.start()
word = forca.get_word()

forca.play(word, vidas, tentativas)
