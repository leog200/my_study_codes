#Neste código iremos digitar a latitude e a longitude de alguma cidade em que você deseja ver no mapa
#mapa_localidade.html é o arquivo que irá buscar sua cidade no mapa

import folium

#Função para solicitar a localidade ao usuário
def obter_localidade():
    latitude = float(input("Digite a latitude da localidade: "))
    longitude = float(input("Digite a longitude da localidade: "))
    return latitude, longitude

#Função para mostrar a localidade em um mapa
def mostrar_localidade_mapa(latitude, longitude):
    mapa = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup="Localidade").add_to(mapa)
    mapa.save("mapa_localidade.html")
    print("Mapa da localidade salvo como 'mapa_localidade.html'.")

#Exemplo de uso:
print("Digite as coordenadas da localidade:")
latitude, longitude = obter_localidade()
mostrar_localidade_mapa(latitude, longitude)
