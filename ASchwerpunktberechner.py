import json

coords = []
with open("DataLayer.json") as file:
    data = json.load(file)
    for Entry in data["features"]:
        zer = Entry["geometry"]["coordinates"][0]
        one = Entry["geometry"]["coordinates"][1]
        coords.append((zer, one))
null = 0
eins = 0
for (zer, one) in coords:
    null += zer
    eins += one
null = null/len(coords)
eins = eins/len(coords)
print((eins, null))
