### Praktisk uppgift 1 ###
namn = " aNnA kaRlSsOn "

rensat_namn = namn.strip()
gemener = rensat_namn.lower()
med_versaler = gemener.title()

nytt_namn = med_versaler.replace(" ","-")
print(nytt_namn)

### Praktisk uppgift 2 ###
order = ("bröd", "mjölk", "ägg", "smör", "ost", "yoghurt")
print(order[:3])
print(order[3:])
print(order[::2])

### Praktisk uppgift 3 ###
filmer = ["Inception", "The Matrix", "Interstellar", "The Prestige"]
filmer.append("Memento")
filmer[1] = "The Lord of the Rings"
filmer.pop(3)
filmer.insert(2, "The Dark Knight")
print(filmer)