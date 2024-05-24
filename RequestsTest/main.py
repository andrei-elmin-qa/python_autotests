import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '12b9aee3a2f9294f71c966d1d927a643'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}



body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change = {
    "pokemon_id": "20062",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_catch = {
    "pokemon_id": "20062"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)

response_change = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print (response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print (response_catch.text)


messege = response_create.json()['message']
print(messege)

messege = response_change.json()['message']
print(messege)

messege = response_catch.json()['message']
print(messege)