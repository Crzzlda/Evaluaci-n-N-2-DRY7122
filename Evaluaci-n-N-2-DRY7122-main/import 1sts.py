import requests
from geopy.geocoders import Nominatim

api_key = '6fc3a31c-9b80-463a-9dbf-7670365c305b'
def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="distance_calculator")
    location = geolocator.geocode(ciudad)
    if location:
        return f'{location.latitude},{location.longitude}'
    else:
        print(f"No se pudo obtener coordenadas para {ciudad}")
        return None
ciudad_origen = input("Ingrese la Ciudad de Origen: ")
ciudad_destino = input("Ingrese la Ciudad de Destino: ")
origen_coords = obtener_coordenadas(ciudad_origen)
destino_coords = obtener_coordenadas(ciudad_destino)

if origen_coords and destino_coords:
    url = f'https://graphhopper.com/api/1/route?point={origen_coords}&point={destino_coords}&vehicle=car&locale=es&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        distance_meters = data['paths'][0]['distance']
        distance_kilometers = distance_meters / 1000
        print(f'La distancia entre {ciudad_origen} y {ciudad_destino} es de aproximadamente {distance_kilometers:.2f} km')
    else:
        print('Error en la solicitud:', response.status_code, response.text)
else:
    print("No se pudo calcular la distancia debido a problemas con las coordenadas.")