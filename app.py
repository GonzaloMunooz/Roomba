from flask import Flask, render_template
import json

app = Flask(__name__)

# Ruta para cargar la puntuación máxima desde el archivo JSON
def load_high_score():
    try:
        with open("high_score.json", "r") as file:
            data = json.load(file)
            return data.get("high_score", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

@app.route("/")
def index():
    max_score = load_high_score()  # Cargar la puntuación máxima
    return render_template("./index.html", max_score=max_score)

if __name__ == "__main__":
    app.run(debug=True)
