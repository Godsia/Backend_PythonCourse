from flask import *
from dotenv import dotenv_values

app = Flask(__name__)


@app.route("/")
def server_info():
    return "My server"

@app.route("/author")
def author():
    author = {
        "name": "Stas",
        "course": 3,
        "age": 21,
    }
    return jsonify(author)

def get_port():
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5000

if __name__ == "__main__":
    app.run(debug=True, port=get_port())
