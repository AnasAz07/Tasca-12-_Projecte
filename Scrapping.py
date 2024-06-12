import requests

def funscrap():
    # URL base para obtener la lista de ubicaciones
    url = "https://pokeapi.co/api/v2/location"
    
    # Realizar una solicitud GET a la URL base
    res = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if res.status_code == 200:
        # Convertir la respuesta a un objeto JSON
        datos = res.json()
        
        # Iterar sobre cada ubicación en los resultados
        for location in datos['results']:
            # Obtener la URL específica de cada ubicación
            location_url = location['url']
            
            # Realizar una solicitud GET a la URL específica de la ubicación
            location_res = requests.get(location_url)
            
            # Verificar si la solicitud fue exitosa
            if location_res.status_code == 200:
                # Convertir la respuesta a un objeto JSON
                location_data = location_res.json()
                
                # Imprimir los detalles de la ubicación
                print(f"\nDetalles de la ubicación {location_data['name']}:")
                print(f"ID: {location_data['id']}")
                print(f"Nombre: {location_data['name']}")
                print("Áreas:")
                
                # Iterar sobre cada área de la ubicación y imprimir su nombre
                for area in location_data['areas']:
                    print(f"- {area['name']}")
            else:
                # Si la solicitud a la URL específica falla, imprimir un mensaje de error
                print(f"No se pudieron obtener los datos de la ubicación en URL: {location_url}")