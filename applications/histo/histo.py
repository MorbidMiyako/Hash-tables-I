# Your code here


f = open('robin.txt', 'r')

completeCipher = f.read()


ignoredLetters = ["\"", ":", ";", ",", ".", "-", "+", "=",
                  "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\n", "\r", "?", "!"]

longest_word = 0

lowercase_and_cleaned = ""

for letter in completeCipher:
    if letter not in ignoredLetters:
        lowercase_and_cleaned += letter.lower()

wordsArray = lowercase_and_cleaned.split(" ")
wordsDict = {}

for words in wordsArray:
    words = str(words)
    if words in wordsDict:
        wordsDict[words] += "#"
    else:
        if len(words) > longest_word:
            longest_word = len(words)
        wordsDict[words] = "#"

wordsList = list(wordsDict.items())
# print(wordsList.sort(key=lambda e: e[0]))
wordsList.sort()
wordsList.sort(key=lambda e: e[1], reverse=True)

for wordTupels in wordsList:
    spaces = (longest_word+2-len(wordTupels[0]))*" "
    print(f"{wordTupels[0]}{spaces}{wordTupels[1]}")
