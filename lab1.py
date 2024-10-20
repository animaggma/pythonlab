def count_vowels_and_consonants(text):
    vowels = "աեիոուօ"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha(): 
            consonant_count += 1

    return vowel_count, consonant_count

text = " "
vowels, consonants = count_vowels_and_consonants(text)
print(f"Ձայնավորներ: {vowels}, Բաղաձայններ: {consonants}")
