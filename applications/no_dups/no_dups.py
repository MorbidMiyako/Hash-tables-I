def no_dups(s):
    # Your code here
    # set automatically orders ;-;
    """
    if len(s.split(" ")) <= 1:
        print(s)
        return s
    print(str(" ".join(list(set(s.split(" "))))))
    return str(" ".join(list(set(s.split(" ")))))
    """
    wordsArray = s.split(" ")
    returnArray = []

    if len(wordsArray) <= 1:
        print(s)
        return s
    for word in wordsArray:
        if word not in returnArray:
            returnArray.append(word)
    print(" ".join(returnArray))
    return " ".join(returnArray)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
