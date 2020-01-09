original = input("What is your sentence? ").strip().lower()
words = original.split()
new_words = []
for word in words:
    if word [0] in "aeiou":
        new_word = word + "(v)"
        new_words.append(new_word)

    else:
        vowel_index = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_index = vowel_index + 1
            else:
                break
        cons = word[:vowel_index]
        the_rest = word[vowel_index:]
        new_word = the_rest + cons + "(c)"
        new_words.append(new_word)

output = " ".join(new_words)
print(output)
        

    


    
