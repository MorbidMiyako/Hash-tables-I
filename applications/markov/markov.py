import random

# Read in all the words in one go
with open("input.txt") as f:
    text = f.read()

# TODO: analyze which words can follow other words
"""
dict = {
    word : [follows]
}

go trough array of words: (for i in range(wordArray -1))
    for each:
        dict[wordArray[i]].append[wordArray[i+1]]
"""

newText = ""
toRemove = ["\n", "\r"]

for letter in text:
    if letter not in toRemove:
        newText += letter

wordsArray = newText.split(" ")

endLetters = [".", "!", "?"]

wordDict = {}
startWordArray = []
endWordArray = []


def randomSentence():

    for i in range(len(wordsArray)-1):
        # if i < 60:
        #     print(wordsArray[i])
        #     if wordsArray[i][len(wordsArray[i])-1] == "\n" or wordsArray[i][len(wordsArray[i])-1] == "\r":
        #         print("_____________")
        #         print("_____________")
        #         print("_____________")
        #         print("_____________")
        #         wordsArray[i] = wordsArray[:-1]
        #     print(wordsArray[i])
        # if wordsArray[i][len(wordsArray[i])-1] == "n":
        # if wordsArray[i][len(wordsArray[i])-1] == "r":
        # if wordsArray[i][len(wordsArray[i])-1] == "\"":

        if wordsArray[i][len(wordsArray[i])-1] in endLetters:
            endWordArray.append(wordsArray[i])

        if wordsArray[i][len(wordsArray[i])-1] == "\"":
            if wordsArray[i][len(wordsArray[i])-2] in endLetters:
                endWordArray.append(wordsArray[i])

        if wordsArray[i][0].isupper():
            startWordArray.append(wordsArray[i])

        if wordsArray[i][0] == "\"":
            if wordsArray[i][1].isupper():
                startWordArray.append(wordsArray[i])

        if wordsArray[i] in wordDict:
            wordDict[wordsArray[i]].append(wordsArray[i+1])
        else:
            wordDict[wordsArray[i]] = [wordsArray[i+1]]

    lastWord = random.choice(startWordArray)
    sentenceArray = [lastWord]
    while lastWord not in endWordArray:
        # print(lastWord)
        # print(lastWord in endWordArray)
        lastWord = random.choice(wordDict[lastWord])
        sentenceArray.append(lastWord)

    print("\n")
    print(" ".join(sentenceArray))

# print(wordsArray)
# print(startWordArray)
# print(endWordArray)


# TODO: construct 5 random sentences
# Your code here

for i in range(5):
    randomSentence()
