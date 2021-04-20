# 1. Letter Summary
# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# $ python3 letter_histogram.py
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}



# word = input("Please enter a word: ")

# lowerWord = word.lower()

# def letterHistogram(lowerWord):
#     numberOfLetters = {}
#     for letters in lowerWord:
#         if letters in numberOfLetters:
#             numberOfLetters[letters] += 1
#         else:
#             numberOfLetters[letters] = 1

#     return numberOfLetters

# print(letterHistogram(lowerWord))





# 2. Word Summary
# Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# $ python3 word_histogram.py
# Please enter a sentence: To be or not to be
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}


word = input("Please enter a sentense: ")

lowerWord = word.lower()

def wordHistogram(lowerWord):
    numberOfWords = {}
    splitWord = lowerWord.split()
    for words in splitWord:
        if words in numberOfWords:
            numberOfWords[words] += 1
        else:
            numberOfWords[words] = 1

    return numberOfWords

print(wordHistogram(lowerWord))







# 3. Sorting a histogram
# Given a histogram tally (one returned from either letter_histogram or word_histogram), print the top 3 words or letters.

# $ python3 word_histogram_tally.py

# Please enter a sentence: To be or not to be do be do be do
# The top three words are:
# be: 4
# do: 3
# to: 2