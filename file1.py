'''
CAAP CS Lab 2
QinaLiu, Soraya Wilson
2022-07-19
'''

import calendar
from datetime import date

def numDigits(num):
    ''' 
    Determines how many digits are in a number (not float or string)
    Input: one int
    Return: an int that represents the number of digits 
    '''
    # in case negative int
    if num < 0:
        num = abs(num)
    return len(str(num))

def test_numDigits():
    assert numDigits(1) == 1
    assert numDigits(111) == 3
    assert numDigits(29048201) == 8

def numberOfSecondsAlive(year, month, day):
    '''
    Determines how many seconds alive from the birthday given
    Input: three ints
    Return: an int that represents the number of seconds alive
    '''
    daysTotal = 0 

    today = date.today()
    #(type(today.year))

    if today.year != year:
        # days lived in year of birth 
        for i in range(month, 13):
            daysInThisMonth = calendar.monthrange(year, i)[1]
            if i == month:
                daysTotal += daysInThisMonth- day
            else:
                daysTotal += daysInThisMonth
        # days lived in full years (not this year, nor birth year)
        for i in range(year+1, today.year):
            daysTotal += 365 + calendar.isleap(i)
        
        # days lived in this year
        for i in range(1, today.month):
            daysTotal += calendar.monthrange(year, i)[1]
        daysTotal += today.day
    # born this year
    else:
        for i in range(month, today.month):
            daysInThisMonth = calendar.monthrange(year, i)[1]
            if i == month:
                daysTotal += daysInThisMonth - day
            else:
                daysTotal += daysInThisMonth
        # born in this year, this month
        if month == today.month:
            daysTotal += today.day - day
        # lived in this month to current date
        else: 
            daysTotal += today.day
    return daysTotal * 86400

def promptBirthday():
    '''
    Calls numberOfSecondsAlive() with parameters taken from standard input by the user
    Input: nothing
    Return: an int that represents the number of digits 
    '''
    print("What is your birthyear?")
    year = int(input())
    print("What month were you born?")
    month = int(input())
    print("What day were you born ?")
    day = int(input())
    return numberOfSecondsAlive(year, month, day)

def main():
    #test_numDigits()
    print("Running numDigits(99)")
    print(numDigits(99))
    print("Done! \n------------------------\n")

    print("Running numDigits(-100)")
    print(numDigits(-100))
    print("Done! \n------------------------\n")

    print("Running numberOfSecondsAlive(2022, 7, 13)")
    print(numberOfSecondsAlive(2022, 7, 13))
    print("Done! \n------------------------\n")

    print("Running numberOfSecondsAlive(2021, 7, 14)")
    print(numberOfSecondsAlive(2021, 7, 14))
    print("Done! \n------------------------\n")

    print("Running numberOfSecondsAlive(2020, 7, 14)")
    print(numberOfSecondsAlive(2020, 7, 14))
    print("Done! \n------------------------\n")

    print("Running numberOfSecondsAlive(2022, 6, 20)")
    print(numberOfSecondsAlive(2022, 6, 20))
    print("Done! \n------------------------\n")

    print("Running numberOfSecondsAlive(2019, 6, 20)")
    print(numberOfSecondsAlive(2019, 6, 20))
    print("Done! \n------------------------\n")
    
    '''
    # today is 7-14-2022
    print(numberOfSecondsAlive(2022, 7, 13)) # 1 day
    print(numberOfSecondsAlive(2021, 7, 14)) # 1 year = 365 days
    print(numberOfSecondsAlive(2020, 7, 14)) # 2 years (2022 is leap) = 731 days
    print(numberOfSecondsAlive(2022, 6, 20)) # 10 days in june + 14 in july = 24 days
    print(numberOfSecondsAlive(2019, 6, 20)) # googles says it's been 1120 days since
    '''
    print("Running promptBirthday()")
    print(promptBirthday())
    print("Done! \n------------------------\n")



if __name__ == "__main__":
    main()