def separate_and_count(text):
    lower_case = []
    upper_case = []
    count = 0

    for char in text:
        count += 1  
        if char.islower():
            lower_case.append(char)
        elif char.isupper():
            upper_case.append(char)
      
    result = ''.join(lower_case) + ''.join(upper_case)

    return result, count

input_text = input("Enter your text: ")
result_text, count = separate_and_count(input_text)

print("Processed text:", result_text)
print("Total count of characters:", count)
