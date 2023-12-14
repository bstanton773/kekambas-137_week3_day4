from wrappers import WeatherAPI, PokeAPI


def main():
    print("Welcome to the Weather and Pokemon app!")
    weather_client = WeatherAPI('1ac9901266fa4ab48f9185441220510')
    poke_client = PokeAPI()
    poke_dex = []
    while True:
        print('Things To Do:\n1. Get Weather Info\n2. Catch Pokemon\n3. Quit')
        choice = input('Which option would you like to do? ')
        while choice not in {'1', '2', '3'}:
            choice = input('Invaild Option. Please choose 1, 2, or 3: ')
        if choice == '3':
            print('Thank you for enjoying our application. Good Bye!')
            break
        elif choice == '1':
            city = input('Please enter the name of the city: ').title()
            weather_info = weather_client.get_current_weather(city)
            if weather_info:
                print(weather_info)
            else:
                print(f"No information on {city}")
        elif choice == '2':
            poke_name = input("What pokemon did you catch? ")
            pokemon = poke_client.get_pokemon(poke_name)
            if pokemon:
                poke_dex.append(pokemon)
                print(f"{pokemon.name} has been caught")
    print('Here are the Pokemon you caught:')
    for poke in poke_dex:
        print(poke)

# If this run.py file is executed directly, run the main function
if __name__ == "__main__":
    main()