from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get the first 150 Pokémon from the API
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=150")
    data = response.json()
    pokemon_list = data['results']
    
    # Create an empty list to store our Pokémon details
    pokemons = []
    
    for pokemon in pokemon_list:
        # Each Pokémon has a URL like "https://pokeapi.co/api/v2/pokemon/1/"
        url = pokemon['url']
        parts = url.strip("/").split("/")
        id = parts[-1]  # The last part is the Pokémon's ID
        
        # Make an image URL for the Pokémon
        image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
        
        # Add the Pokémon details to our list
        pokemons.append({
            'name': pokemon['name'].capitalize(),
            'id': id,
            'image': image_url
        })
    
    # Show our webpage with the Pokémon data
    return render_template("index.html", pokemons=pokemons)

if __name__ == '__main__':
    app.run(debug=True)
