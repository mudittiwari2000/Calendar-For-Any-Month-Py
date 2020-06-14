from utility import clear       #* Made my own module named utility, it has a function called clear, that clears the console for a cleaer output
import sys                      #* To end the program if an error/exception occurs
from time import sleep          #* To pause the console for a certain amount of time
from simple_colors import *

clear ()                        #* To clear the console

monthdict = {
a
    1: 0, 2: 3, 3: 3,  4: 6,  5: 1,  6: 4,
    7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5            
}

month_in_word = {

    1: 'January',   2: 'February',   3: 'March',        4: 'April',     5: 'May',       6: 'June',
    7: 'July',      8: 'August',     9: 'September',   10: 'October',  11: 'November', 12: 'December'
    
}
monthDaysDict = {

    1: 31, 2: 28, 3: 31,  4: 30,  5: 31,  6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
}

def get_month ():
    
    terminate = 1

    while terminate:

        global month
        try:
            month = int (input ("Enter the month, which you want the calendar of (1-12): "))
        except ValueError:
            print (f"\n** ERROR: You were supposed to enter an integer, not a string **\n")
            continue

        if month not in monthdict:
            try_again = input ("Sorry, I don't think that counts as a Month, would you like to try again? (Y/N): ")
            if try_again.upper() == 'Y':
                pass
            else:
                sys.exit("Alright, have fun!")
        
        else:
            terminate = 0

def get_year () :

    terminate = 1

    while terminate:

        global year
        try:
            year = int(input ("Enter the year (1800 - 2099), as well please: "))
        except ValueError:
            print (f"\n** ERROR: You were supposed to enter an integer, not a string **\n")
            continue

        if year < 1800 or year > 2099:
            try_again = input (f"\n** Sorry, I don't think that {year} is within the range (1800, 2100) , would you like to try again? (Y/N): ")
            if try_again.upper() == 'Y':
                pass
            else:
                sys.exit("Alright, have fun!")

        else:
            terminate = 0


def get_monthCode ():
    if month == 1 and ((year%4 == 0) and (year%100 != 0) or (year%400 == 0)):
        return 6
    elif month == 2 and ((year%4 == 0) and (year%100 != 0) or (year%400 == 0)):
        return 2
    else: 
        return monthdict[month]

def get_yearCode ():
    yc = int (year%100)
    yc = int (yc + yc/4)
    return yc%7

def get_centuryCode ():
    cc = int (year/100)
    cc = int (cc%4)
    if cc == 0:
        return 6
    elif cc == 1:
        return 4
    elif cc == 2:
        return 2
    elif cc == 3:
        return 0
    

def calendarPerimeter () :

    clear ()
    print ()
    print (f"\n\n\t\t\t\t\t\t\t\t\t\t\t\t   ", end='')
    print (cyan(month_in_word[month], 'bright'), end=' ')
    print (cyan(str(year),'bold'), end='')
    print (cyan("'s Calendar:", 'bright'))
    print (f"\n\t\t\t\t\t\t\t+---------------------------------------------------------------------------------------------------------------+")
    print (f"\t\t\t\t\t\t\t|\t SUN \t|\t MON \t|\t TUE \t|\t WED \t|\t THU \t|\t FRI \t|\t SAT \t|", end='')
    print (f"\n\t\t\t\t\t\t\t|\t     \t|\t     \t|\t     \t|\t     \t|\t     \t|\t     \t|\t     \t|",end='')

def calendarContent ():

    num = 1
    lastline = 0

    if month == 2 and ((year%4 == 0) and (year%100 != 0) or (year%400 == 0)):
            monthDaysDict[2] = 29

    for k in range (0, 7):

        if lastline == 1:
            print(f"\n\t\t\t\t\t\t\t+---------------------------------------------------------------------------------------------------------------+\n ")
            sleep (5)
            return 0

        if num <= monthDaysDict[month]:
            print (f"\n\t\t\t\t\t\t\t----------------------------------------------------------------------------------------------------------------- ")
            print (f"\t\t\t\t\t\t\t|\t ", end='')

        for i in range (0, 7):
        
            if num > monthDaysDict[month]:

                if i == 6:
                    lastline = 1
                    print (f"\t|\t",end=' ')
                    break
                
                elif i == 0:
                    lastline = 1
                    break

                else:
                    print (f"\t|\t",end=' ')
                    continue

            if k == 0 and i < DC:
                print (f"\t|\t",end=' ')
                continue

            else:
                print (num, end=" \t|\t ")
                num += 1
        
    
# Driver Function
if __name__ == '__main__':
    
    get_month ()                        #* To take the input for month from the user
    get_year ()                         #* To take the input for year from the user
    MC = get_monthCode ()               #* To get the month code (MC) from the monthDict
    YC = get_yearCode ()                #* To get the year code (YC)
    CC = get_centuryCode ()             #* To get the century code (CC)
    DC = int ( (MC+YC+CC+1)%7 )         #* Calculating the dayCode (DC) from MC, YC, CC, and 1 (for the 1st day of any given month)
    calendarPerimeter ()                #* To print the perimeter/outline for the calendar
    calendarContent ()                  #* To print the contents in the calendar