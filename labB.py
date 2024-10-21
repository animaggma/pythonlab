dict1 = {
    "name1": "Anna",
    "name2": "Ani",
    "name3": "Astgh",
    "name4": "Arev",
}
dict2 = {
    "surname1": "Sargsyan",
    "surname2": "Kirakosya",
    "surname3": "Hovhannisyan",
    "surname4": "Harutyunyan",
}


names = list(dict1.values())
surnames = list(dict2.values())

for i in range(len(names)):
    print(names[i] + " " + surnames[i])
