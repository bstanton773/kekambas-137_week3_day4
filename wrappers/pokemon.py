import requests
from ascii_magic import AsciiArt

class Pokemon:
    def __init__(self, poke_id, name, height, weight, image_url):
        self.id = poke_id
        self.name = name.title()
        self.height = height
        self.weight = weight
        self.image_url = image_url
        
    def __str__(self):
        art = AsciiArt.from_url(self.image_url)
        art_string = art.to_ascii()
        return f"{art_string}\nName: {self.name}\nHeight: {self.height}\nWeight: {self.weight}"
    
    def __repr__(self):
        return f"<Pokemon {self.id}|{self.name}>"

class Berry:
    def __init__(self, berry_id, name, growth_time, size, smoothness):
        self.id = berry_id
        self.name = name.title()
        self.growth_time = growth_time
        self.size = size
        self.smoothness = smoothness
        
    def __str__(self):
        return f"""Name: {self.name}
Growth Time: {self.growth_time} day(s)
Size: {self.size}
Smoothness: {self.smoothness}"""
    
    def __repr__(self):
        return f"<Berry {self.id}|{self.name}>"

class PokeAPI:
    base_url = 'https://pokeapi.co/api/v2/'
    
    # Private method to build the request url and get the data
    def __get(self, endpoint, id_or_name):
        request_url = self.base_url + endpoint + "/" + id_or_name
#         print(request_url)
        res = requests.get(request_url)
        if res.ok:
            return res.json()
        else:
            return None
        
    def get_pokemon(self, poke_name):
        # Make the API request
        data = self.__get('pokemon', poke_name.lower())
        # Check if we get back data
        if data:
            # Pull the specific data
            poke_id = data.get('id')
            name = data.get('name')
            height = data.get('height')
            weight = data.get('weight')
            image_url = data.get('sprites').get('front_default')
            # Create a Pokemon instance with that data
            new_pokemon = Pokemon(poke_id, name, height, weight, image_url)
            # return the new Pokemon instance
            return new_pokemon
        # if no data
        else:
            print(f"{poke_name} is not a Pokemon")
            
    # Create a get_berry method that will return a Berry instance (id, name, growth_time, size, smoothness)
    def get_berry(self, berry_name):
        # Make the API request
        data = self.__get('berry', berry_name.lower())
        if data:
            berry_id = data.get('id')
            name = data.get('name')
            growth_time = data.get('growth_time')
            size = data.get('size')
            smoothness = data.get('smoothness')
            new_berry = Berry(berry_id, name, growth_time, size, smoothness)
            return new_berry
        else:
            print(f"{berry_name} is not a Berry")
    
