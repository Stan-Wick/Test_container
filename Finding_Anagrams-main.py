# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    # Arrange and sort letters in word
    a = word.lower()
    a = sorted(a)
    a = [i for i in a if i !=' ']
    #print(a)

    # Arrange and sort letters in anagram
    b = anagram.lower()
    b = sorted(b)
    b = [i for i in b if i !=' ']
    #print(b)

    # Test if true or false
    return a==b

# Collect user Input
word = input('Word? ')
anagram = input('Anagram? ')
# Find out if both inputs are anagrams
result = find_anagram(word, anagram)
# Print the result
if result == True:
    print('True. They are anagrams')
else:
    print('False. They are not anagrams')

