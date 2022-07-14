def checkKeys(myDict, key):
    ''' 
    Checks if key is a key in myDict
    Input: a dictionary, a key (corresponding type of the keys of myDict)//
    Return: A boolean that is True if key is a key in myDict
    '''
    return key in myDict

def checkValue(myDict, value):
    ''' 
    Checks if value is a value in myDict
    Input: a dictionary, a value (corresponding type of the values of myDict)//
    Return: A boolean that is True if value is a value in myDict
    '''
    for i in myDict:
        if myDict[i] == value:
            return True
    return False
    #return True if myDict[i] == value for i in myDict else False

def dictFactory(myKeys, myValue):
    ''' 
    Creates a dictionary so that each i-th value of myKeys corresponds to the i-th value 
    of myValues. If the two lists are not the same length, the dictionary will be of the
    largest possible correspondence
    Input: two lists 
    Return: a dictionary 
    '''
    myDict = {}
    for i in range(min(len(myKeys), len(myValue))):
        myDict[myKeys[i]] = myValue[i]
    return myDict

def main():
    print(checkKeys({2: "hi", 10: "hey", -39: "no"}, 3))
    print(checkKeys({3: "hi", 10: "hey", -39: "no"}, 3))

    print(checkValue({3: "hi", 10: "hey", -39: "no"}, "hey"))
    print(checkValue({3: "hi", 10: "hey", -39: "no"}, "yes"))

    print(dictFactory([1, 4, -7], ["no", "yes", "yas"]))


if __name__ == "__main__":
    main()