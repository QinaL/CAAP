'''
CAAP CS Lab 2
QinaLiu, Soraya Wilson
2022-07-19
'''

def printList(listy):
    ''' 
    Prints each element in a list to the terminal, one per line
    Input: a list
    Return: None 
    '''
    for i in listy:
        print(i)

def printTriangle(num):
    ''' 
    Prints num lines, with the first line of the pattern num num-1 ... 1, and each next line 
    with a starting num of one less that previous line until the line prints 1
    Input: one int
    Return: None 
    '''
    # 0 and neg nums ?
    for i in range(num, 0, -1):
        line = ""
        for j in range(i, 0, -1):
            line += str(j) + " "
        print(line)

def reverseList(listy):
    ''' 
    Reverses the elements in the given list
    Input: a list
    Return: a list with reversed elements 
    '''
    newList = []
    for i in range(len(listy)-1, -1, -1):
        newList.append(listy[i])
    return newList

def reverseString(string):
    ''' 
    Reverses a string
    Input: a string
    Return: a string 
    '''
    newString = list(string)
    return "".join(reverseList(newString))

def isEven(num):
    ''' 
    Checks if a number is even
    Input: an int
    Return: a boolean that is True if num is even
    '''
    return num % 2 == 0

def isOdd(num):
    ''' 
    Checks if a number is odd
    Input: an int
    Return: a boolean that is True if num is odd
    '''
    return num % 2 != 0 

def isMod3(num):
    ''' 
    Checks if a number can be evenly divided by 3
    Input: an int
    Return: a boolean that is True if num can be evenly divided by 3
    '''
    return num % 3 == 0

def filterList(myList, myFilter):
    ''' 
    Filters the given list with the given function myFilter
    Input: a list, a function
    Return: a list with only the elements that is True for myFilter
    '''
    newList = []
    for i in myList:
        if myFilter(i):
            newList.append(i)
    return newList

def main():
    print("Running printList([1, 3, -10, 854980])")
    printList([1, 3, -10, 854980])
    print("Done! \n------------------------\n")

    print("Running printTriangle(7)")
    printTriangle(7)
    print("Done! \n------------------------\n")
    
    print("Running printTriangle(0)")
    printTriangle(0)
    print("Done! \n------------------------\n")

    print("Running printTriangle(-3)")
    printTriangle(-3)
    print("Done! \n------------------------\n")

    print("Running reverseList([0, 10, -96, 2823, 2])")
    print(reverseList([0, 10, -96, 2823, 2]))
    print("Done! \n------------------------\n")

    print("Running reverseList([])")
    print(reverseList([]))
    print("Done! \n------------------------\n")

    print("Running reverseString(\"hello world!\")")
    print(reverseString("hello world!"))
    print("Done! \n------------------------\n")

    print("Running reverseString(\"\")")
    print(reverseString(""))
    print("Done! \n------------------------\n")

    print("Running isEven(138)")
    print(isEven(138))
    print("Done! \n------------------------\n")

    print("Running isEven(137)")
    print(isEven(137))
    print("Done! \n------------------------\n")

    print("Running isOdd(137)")
    print(isOdd(137))
    print("Done! \n------------------------\n")

    print("Running isOdd(138)")
    print(isOdd(138))
    print("Done! \n------------------------\n")

    print("Running isMod3(139)")
    print(isMod3(139))
    print("Done! \n------------------------\n")

    print("Running isMod3(99)")
    print(isMod3(99))
    print("Done! \n------------------------\n")

    print("Running filterList([1, 2, 3, 109, -24, 0, -37], isEven)")
    print(filterList([1, 2, 3, 109, -24, 0, -37], isEven))
    print("Done! \n------------------------\n")

    print("Running filterList([], isMod3)")
    print(filterList([], isMod3))
    print("Done! \n------------------------\n")

if __name__ == "__main__":
    main()
