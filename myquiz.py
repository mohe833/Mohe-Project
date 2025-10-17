from flask import Flask, render_template, request

app = Flask(__name__)

wortliste = {

    "Bruder": "Brüder",

    "Eltern": "-",

    "Familie": "Familien",

    "Fest": "Feste",

    "Geschwister": "-",

    "Grossvater": "Grossväter",

    "Mutter": "Mütter",

    "Onkel": "-",

    "Schwester": "Schwestern",

    "Sohn": "Söhne",

    "Tante": "Tanten",

    "Tochter": "Töchter",

    "Vater": "Väter",

    "Vorname": "Vornamen",

    "Besuch": "Besuche",

    "Cousin": "Cousins",

    "Cousine": "Cousinen",

    "Enkel": "-",

    "Enlelin": "Enklinnen",

    "Familienname": "Familiennamen",

    "Geschenk": "Geschenke",

    "Party": "Partys",

    "Nichte": "Nichten",

    "Neffe": "Neffen"

}

@app.route("/", methods=["GET", "POST"])

def quiz():

    score = 0

    if request.method == "POST":

        user = request.form.get("username").capitalize()

        for i, (question, answer) in enumerate(wortliste.items()):

            user_answer = request.form.get(f"q{i}").capitalize()

            if user_answer == answer:

                score += 1

        return f"<h1>{user}, dein Ergebnis: {score} von {len(wortliste)}</h1>"

    html = "<h1>Willkommen zu meinem Mini-Projekt!</h1>"

    html += "<form method='POST'>"

    html += "Wie ist dein Name?: <input type='text' name='username' required><br><br>"

    for i, (question, answer) in enumerate(wortliste.items()):

        html += f"<label>Was ist der Plural von {question}?: </label>"

        html += f"<input type='text' name='q{i}' required><br><br>"

    html += "<input type='submit' value='Abschicken'>"

    html += "</form>"

    return html

if __name__ == "__main__":

    app.run(debug=True)
 