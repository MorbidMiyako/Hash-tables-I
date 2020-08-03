# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

f = open('ciphertext.txt', 'r')

completeCipher = f.read()

lettersDict = {}

ignoredLetters = [" ", ",", ".", "\'", "\n", "\"", ';',
                  ':', '-', '?', '!', 'â', '€', '”', '(', '1', ')']

totalLetters = 0

valueLetterPairs = []

for letter in completeCipher:
    if letter in ignoredLetters:
        pass
    elif letter in lettersDict:
        lettersDict[letter] += 1
    else:
        lettersDict[letter] = 1

lettersList = list(lettersDict.items())

lettersList.sort(key=lambda e: e[1], reverse=True)

newLettersDict = dict(lettersList)

frequencyOrder = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L',
                  'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

counter = 0

for letter in newLettersDict:
    newLettersDict[letter] = counter
    counter += 1

decodedText = ""

for letter in completeCipher:
    if letter in newLettersDict:
        decodedText += frequencyOrder[newLettersDict[letter]]
    else:
        decodedText += letter

print(decodedText)
