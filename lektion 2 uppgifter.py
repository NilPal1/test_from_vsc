### Praktisk uppgift 1 ###
# namn = " aNnA kaRlSsOn "

# rensat_namn = namn.strip()
# gemener = rensat_namn.lower()
# med_versaler = gemener.title()

# nytt_namn = med_versaler.replace(" ","-")
# print(nytt_namn)

### Praktisk uppgift 2 ###
# order = ("bröd", "mjölk", "ägg", "smör", "ost", "yoghurt")
# print(order[:3])
# print(order[3:])
# print(order[::2])

### Praktisk uppgift 3 ###
# filmer = ["Inception", "The Matrix", "Interstellar", "The Prestige"]
# filmer.append("Memento")
# filmer[1] = "The Lord of the Rings"
# filmer.pop(3)
# filmer.insert(2, "The Dark Knight")
# print(filmer)

### Praktisk uppgift 4 ###
data = {
    "studenter": [
    ("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
    ("Bob", {"ålder": 22, "ämnen": ("Biologi"), "aktiv": False}),
    ("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
    ("Diana", {"ålder": 24, "ämnen": ("Matematik", "Fysik"), "aktiv": False}),
    ("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv": 
True}),
    ],
    "kurser": {
    "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
    "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
    "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
    }
}
aktiva_studenter = [student[0] for student in data["studenter"] if student[1]["aktiv"]]
print(aktiva_studenter)
print(tuple(aktiva_studenter))