data = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 2,
    "f": 1
}

occurrencescount = {}
for value in data.values():
    if value in occurrencescount:
        occurrencescount[value] += 1
    else:
        occurrencescount[value] = 1

print(occurrencescount)
