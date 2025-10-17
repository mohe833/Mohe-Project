print("Welcome to my mini Python project! ")
print("Hier kannst du den Plural des Names üben!")
print("Wenn der Plural und Singular gleich sind, schreib bitte -.")
print("Done by MOhammed")

user = input("Wie ist dein Name?: ").capitalize()
print(f"Welcome {user}!")
score = 0
wortliste = {"Bruder": "Brüder",
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
             "Neffe": "Neffen"}

for questions, answers in wortliste.items():
    answer = input(f"Was ist der Plural von {questions}?: ").strip().capitalize()
    if answer == answers:
        print(f"richtig! {user}, gut gemacht!")
        score += 1
        print(f"{user}, du hast {score} von {len(wortliste)}")
    else:
        print(f"falsch! Die richtige Antwor ist {answers}.")

if score == len(wortliste):
    print(f"Super Arbeit {user}!")
    print(f"Du hast {score} von {len(wortliste)}")
elif score > 20:
    print(f"{user} Du hast es gut gemacht!")
    print(f"Du hast {score} von {len(wortliste)}")
elif score < 15:
    print(f"{user}, Übung macht den Meister. \n Versuch sie, nochmals zu üben!")
    print(f"Du hast {score} von {len(wortliste)}")

print("Ich heisse Mohammed und vielen Dank für das Testen meines Codes!")

    
    

