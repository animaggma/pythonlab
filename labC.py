str = "HEllO MY name is"
strLow = ""
strUp = ""

for char in str:
    if char.isalpha() and char.islower():     
        strLow += char
    elif char.isalpha() and char.isupper():       
        strUp += char

print(strLow +" "+ strUp)
