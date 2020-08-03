def word_count(s):
    # Your code here
    ignoredLetters = ["\"", ":", ";", ",", ".", "-", "+", "=",
                      "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&",  "?", "!"]

    replaceLetters = ["\n", "\r", "\t"]

    longest_word = 0

    lowercase_and_cleaned = ""

    for letter in s:
        if letter not in ignoredLetters:
            if letter not in replaceLetters:
                lowercase_and_cleaned += letter.lower()
            else:
                lowercase_and_cleaned += " "

    wordsArray = lowercase_and_cleaned.split(" ")
    wordsDict = {}

    print(wordsArray)

    for words in wordsArray:
        words = str(words)
        if words in wordsDict:
            wordsDict[words] += 1
        else:
            if len(words) > longest_word:
                longest_word = len(words)
            wordsDict[words] = 1

    del wordsDict[""]
    print(wordsDict)
    return wordsDict

    # wordsList = list(wordsDict.items())
    # # print(wordsList.sort(key=lambda e: e[0]))
    # wordsList.sort()
    # wordsList.sort(key=lambda e: e[1], reverse=True)

    # for wordTupels in wordsList:
    #     spaces = (longest_word+2-len(wordTupels[0]))*" "
    #     print(f"{wordTupels[0]}{spaces}{wordTupels[1]}")


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
