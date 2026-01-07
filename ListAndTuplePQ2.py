#WAP to check if a list contains a palindrome element

word = [1,2,3,2,1]

word2 = word.copy()
word2.reverse()

if(word == word2):
    print("The word is palindrome")
else:
    print("The word is not palidrome")