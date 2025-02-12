#You have a list of ten random words which starts with letters A, C, or P.
#Write a function that takes a list of the word_list and prints new list 
#with all words that starts with letter P.

#txt = "Hi, welcome to my world."

#x = txt.startswith(("Hello", "Hi"))

#print(x)

from typing import List


word_list = ['Apple', 'Car', 'Proud', 'Apricot', 'Plank', 'Calk', 'Alphabet', 'Cork', 'August', 'Plain', 'peach']

def starts_with_p(word_list: List[str]) -> List[str]:
    return [word for word in word_list if word.upper().startswith('P')]
print(starts_with_p(word_list))

