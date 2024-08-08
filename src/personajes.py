import requests
import json

def traducir(texto, idioma_destino='es'):
    # Este es un ejemplo basico de traduccion. Para una traduccion mas precisa, se podria usar una API como la de Google Translate.
    traducciones = {
        "name": "nombre",
        "status": "estado",
        "species": "especie",
        "type": "tipo",
        "gender": "genero",
        "origin": "origen",
        "location": "ubicacion",
        "image": "imagen",
        "episode": "episodio",
        "url": "url",
        "created": "creado"
    }
    return traducciones.get(texto, texto)

def obtener_personajes():
    url = "https://rickandmortyapi.com/api/character"
    personajes = []
    while url:
        respuesta = requests.get(url)
        datos = respuesta.json()
        for personaje in datos['results']:
            personaje_traducido = {
                traducir("name"): personaje["name"],
                traducir("status"): personaje["status"],
                traducir("species"): personaje["species"],
                traducir("type"): personaje["type"],
                traducir("gender"): personaje["gender"],
                traducir("origin"): personaje["origin"]["name"],
                traducir("location"): personaje["location"]["name"],
                traducir("image"): personaje["image"],
                traducir("episode"): [ep.split('/')[-1] for ep in personaje["episode"]],
                traducir("url"): personaje["url"],
                traducir("created"): personaje["created"]
            }
            personajes.append(personaje_traducido)
        url = datos['info']['next']
    return personajes

def guardar_personajes(personajes):
    with open('personajes.json', 'w', encoding='utf-8') as archivo:
        json.dump(personajes, archivo, ensure_ascii=False, indent=4)

def main():
    personajes = obtener_personajes()
    guardar_personajes(personajes)

if __name__ == "__main__":
    main()