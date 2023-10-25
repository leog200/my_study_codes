#Código que permite ao usuário acessar uma nóticia de algum site (NÃO SÃO TODOS QUE PERMITEM, E OS QUE PERMITEM, A NOTÍCIA NÃO É LIDA COM CLAREZA, TUDO EMBARAÇADO)
#O código não te redireciona até o site, ele lê a notíca por aqui mesmo.... no final do código tem as explicações de como foi feito e o que cada função do código faz

import requests
from bs4 import BeautifulSoup
import pyttsx3

def get_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h3')

    new_list = []

    for headline in headlines:
        new_list.append(headline.text)
    return new_list

def speak_news(new_list):
        engine = pyttsx3.init()

        for news in new_list:
            engine.say(news)
            engine.runAndWait()

if __name__ == "__main__":
    news_url = input("Insira a URL do site de notícias: ")
    
if news_url:
    news_list = get_news(news_url)

    if news_list:
        speak_news(news_list)

    else:
        print("Não foi possível obter notícias.")

else:
    print("URL não fornecida. O programa será encerrado.")

#import requests: Esta linha importa a biblioteca requests, que é usada para fazer solicitações HTTP para buscar o conteúdo de uma página da web.

#from bs4 import BeautifulSoup: Importa a classe BeautifulSoup da biblioteca beautifulsoup4, que é usada para analisar o HTML de uma página da web.

#import pyttsx3: Importa a biblioteca pyttsx3, que é usada para sintetizar e reproduzir texto em voz.

#def get_news(url): Define uma função chamada get_news que recebe uma URL como argumento. Essa função é responsável por fazer uma solicitação HTTP para a URL fornecida, baixar a página da web e extrair as manchetes de notícias dela. Aqui estão os principais comandos dentro dessa função:

#response = requests.get(url): Faz uma solicitação GET para a URL especificada e armazena a resposta na variável response.

#soup = BeautifulSoup(response.text, 'html.parser'): Analisa o HTML da página da web usando o BeautifulSoup e cria uma representação em árvore do documento HTML na variável soup.

#headlines = soup.find_all('h3'): Procura todas as tags HTML <h3> na página da web e armazena-as na lista headlines.

#O loop for itera pelas manchetes encontradas e as adiciona à lista news_list.

#def speak_news(news_list): Define uma função chamada speak_news que recebe uma lista de manchetes como argumento. Essa função é responsável por usar a biblioteca pyttsx3 para ler em voz alta as manchetes de notícias fornecidas. O pyttsx3 é usado para inicializar o mecanismo de síntese de fala e ler as notícias em voz alta.

#if __name__ == "__main__":: Esta linha verifica se o script está sendo executado como o programa principal (em oposição a ser importado como um módulo em outro script). Isso é uma boa prática para garantir que o código dentro deste bloco seja executado apenas quando o script é executado diretamente.

#news_url =  Define a URL do site de notícias que você deseja buscar.

#news_list = get_news(news_url): Chama a função get_news com a URL como argumento para buscar as manchetes de notícias e armazená-las na variável news_list.

#if news_list:: Verifica se a lista de notícias não está vazia. Se houver notícias disponíveis, a próxima linha será executada.

#speak_news(news_list): Chama a função speak_news para ler em voz alta as notícias da lista.

#else:: Se a lista de notícias estiver vazia (ou seja, não foi possível obter notícias), esta parte do código será executada.

#print("Não foi possível obter notícias."): Exibe uma mensagem informando que não foi possível obter notícias.





