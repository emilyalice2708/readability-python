from cs50 import get_string

#Define a method to count letters
def letter_count(string):
    count = 0
    for i in range(len):
        if string[i].isalpha():
            count += 1
    return count

#Define a method to count words
def word_count(string):
    count = 0
    for i in range(len):
        if string[i] == ' ':
            count += 1
    count += 1
    return count

#Define a method to count sentences
def sentence_count(string):
    count = 0
    for i in range(len):
        if string[i] == '.' or string[i] == '?' or string[i] == '!':
            count += 1
    return count

#Obtain text input from user
text = get_string("Text: ")
#Define a length variable for use in above methods
len = len(text)
#Define variables for each count using above methods
letters = letter_count(text)
words = word_count(text)
sentences = sentence_count(text)

#Calculate L, S by comparing word count to 100
multi_value = 100 / words
L = multi_value * letters
S = multi_value * sentences
#Calculate index value and round to nearest integer
index = round(0.0588 * L - 0.296 * S - 15.8)

#Return corresponding grade
if index >= 1 and index < 16:
    print(f"Grade {index}")
elif index < 1:
    print("Before Grade 1")
else:
    print("Grade 16+")

