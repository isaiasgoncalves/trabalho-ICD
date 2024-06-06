from openai import OpenAI

def gerador_palavra(difficulty, language):

    # Prompt baseado nos parâmetros fornecidos
    prompt = [
        {
            "role": "user",
            "content": f"Gere uma palavra e uma dica de no maximo duas palavras para um jogo da forca seguindo os parâmetros: Idioma: {language}, Dificuldade: {difficulty}; Separe a palavra e a dica por ponto e vírgula (exemplo: Gato;Era objeto de culto no Egito), sem usar acentos (se a palavra tiver acento, retorne ela sem o acento. EX: pajé / paje) e aplicando o idioma especificado na palavra e na dica. Seja criativo."
        }
    ]

    # Inicializa o cliente da OpenAI
    client = OpenAI(api_key='COLOCAR CHAVE AQUI')

    # Chama o modelo da OpenAI para gerar a palavra e a dica
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        max_tokens=50,
        temperature=1
    )

    # A resposta vem como um objeto ChatCompletion
    generated_text = response.choices[0].message.content

    # Extrai a palavra e a dica
    word, hint = generated_text.split(';')

    palavra = word.strip()
    dica = hint.strip()

    return palavra, dica

