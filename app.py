
# Building an API
from flask import Flask
from pokemon_data import pokemon_response

# If you run app.py directly __name__ == __main__ (ONLY in this scenario type)
app = Flask(__name__)
CORS(app)

# DICTIONARY
banana = {
    "test": "ok",
    "banana": True,
    "count": 1
}

# Endpoint for the Root Route to name/main 
# DECORATOR
@app.route("/")
def home():
    return banana 

# Create a Proxy-Key
@app.route("/get-key")
def get_key():
    return {"key": "ciecgueg857439284nvbdd"}

# Lewis Created his own Pokemon API
null = None 
@app.route("/pokemon")
def get_pokemon():
    return pokemon_response