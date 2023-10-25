#Neste código iremos digitar um texto, e selecionar uma das chaves dos idomas que estão armazenadas no dicionário abaixo, aquela que for escolhida, irá traduzir o texto para sua respectiva língua(Obs: NÃO selecionar o número, e sim as letras. Ex: en)
#Translator é importado para obtermos a tradução

from googletrans import Translator

codigo_idiomas = {
    "1-af": "1-Afrikaans",
    "2-ar": "2-Arabic",
    "3-cs": "3-Czech",
    "4-hr": "4-Croatian ",
    "5-da": "5-Danish",
    "6-en": "6-English",
    "7-fr": "7-French",
    "8-de": "8-German",
    "9-el": "9-Greek",
    "10-he": "10-Hebrew",
    "11-it": "11-Italian",
    "12-ko": "12-Korea",
    "13-no": "13-Norwegian",
    "14-es": "14-Spanish",
    "15-pt": "15-Portuguese",
    "16-ru": "16-Russian",
    "17-tr": "17-Turkish",
    "18-sv": "18-Swedish",
    "19-vi": "19-Vietnamese",

}

print(codigo_idiomas.keys())

print(codigo_idiomas.values())

def traduzir_texto(texto, idioma_destino=''):
    # Cria uma instância do tradutor
    translator = Translator()

    #Faz a tradução
    traducao = translator.translate(texto, dest=idioma_destino)

    # Retorne o texto traduzido
    return traducao.text

#Exemplo de uso:
texto_a_ser_traduzido = input("Digite o texto que deseja traduzir: ")
idioma_destino = input("Digite o código do idioma que deseja traduzir o texto: ")

texto_traduzido = traduzir_texto(texto_a_ser_traduzido, idioma_destino)

print(f"Texto traduzido: {texto_traduzido}")