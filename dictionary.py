def checkKeys(myDict, key):
    ''' 
    Checks if key is a key in myDict
    Input: a dictionary, a key (any type/corresponding type of the keys of myDict)
    Return: A boolean that is True if key is a key in myDict
    '''
    return key in myDict

def checkValue(myDict, value):
    ''' 
    Checks if value is a value in myDict
    Input: a dictionary, a value (any type/corresponding type of the values of myDict)
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
    print("Running checkKeys({2: \"hi\", 10: \"hey\", -39: \"no\"}, 3)")
    print(checkKeys({2: "hi", 10: "hey", -39: "no"}, 3))
    print("Done! \n------------------------\n")

    print("Running checkKeys({3: \"hi\", 10: \"hey\", -39: \"no\"}, 3)")
    print(checkKeys({3: "hi", 10: "hey", -39: "no"}, 3))
    print("Done! \n------------------------\n")
    
    print("Running checkValue({3: \"hi\", 10: \"hey\", -39: \"no\"}, \"hey\")")
    print(checkValue({3: "hi", 10: "hey", -39: "no"}, "hey"))
    print("Done! \n------------------------\n")

    print("Running checkValue({3: \"hi\", 10: \"hey\", -39: \"no\"}, \"yes\")")
    print(checkValue({3: "hi", 10: "hey", -39: "no"}, "yes"))
    print("Done! \n------------------------\n")

    print("Running checkValue({3: \"hi\", 10: \"hey\", -39: \"no\"}, \"yes\")")
    print(checkValue({3: "hi", 10: "hey", -39: "no"}, "yes"))
    print("Done! \n------------------------\n")

    print("Running dictFactory([1, 4, -7, 0], [\"no\", \"yes\", \"yas\", \"yas\"])")
    print(dictFactory([1, 4, -7, 0], ["no", "yes", "yas", "yas"]))
    print("Done! \n------------------------\n")

    print("Running dictFactory([1, 4, -7, 0], [\"no\", \"yes\", \"yas\", \"yas\", \"yassss kweeen\"])")
    print(dictFactory([1, 4, -7, 0], ["no", "yes", "yas", "yas", "yassss kween"]))
    print("Done! \n------------------------\n")

    print("Running dictFactory([1, 4, -7, 0], [\"no\", \"yes\", \"yassss kweeen\"])")
    print(dictFactory([1, 4, -7, 0], ["no", "yes", "yassss kweeen"]))
    print("Done! \n------------------------\n")


if __name__ == "__main__":
    main()