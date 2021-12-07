# determines if a year is a leap year
def isLeapYear(year):
    # possibly a leap year if year % 4 == 0
    if year % 4 == 0:
        # always a leap year if year % 4 == 0 and year % 400 == 0
        if year % 400 == 0:
            return True
        # never a leap year if year % 4 == 0 and year % 400 != 0 and year % 100 == 0
        if year % 100 == 0:
            return False
        # always a leap year if year % 4 == 0 and year % 100 != 0
        if year % 100 != 0:
            return True
    # never a leap year if year % 4 != 0
    else:
        return False

# determines how many days in a month
def getDaysInMonth(monthNumber, year):
    # return False if number is invalid
    if monthNumber not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        return 0
    # return 31 for april, june, september, november
    if monthNumber in [4, 6, 9, 11]:
        return 30
    # return 30 for january, march, may, july, august, october, december
    if monthNumber in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # if month is february check if year is a leap year
    if monthNumber == 2:
        # return 29 if a leap year
        if isLeapYear(year) == True:
            return 29
        # otherwise return 28
        else:
            return 28

# check if a date is the startdate / before the startdate
def isEqualBeforeDate(currentSunday, startDate):
    # return True if currentSunday is earlier year than startdate
    if currentSunday[2] < startDate[2]:
        return True
    # if currentSunday is same year as startDate
    if currentSunday[2] == startDate[2]:
        # return True if currentSunday is earlier month than startdate
        if currentSunday[0] < startDate[0]:
            return True
        # if currentSunday is same month as startdate
        if currentSunday[0] == startDate[0]:
            # return True if currentSunday is equal/earlier day than startdate
            if currentSunday[1] <= startDate[1]:
                return True

    # return False if not the startdate / before the startdate
    return False

#check if a date is after the enddate
def isAfterDate(currentSunday, endDate):
    # return True if currentSunday is later year than enddate
    if currentSunday[2] > endDate[2]:
        return True
    # if currentSunday is same year as endDate
    if currentSunday[2] == endDate[2]:
        # return True if currentSunday is later month than enddate
        if currentSunday[0] > endDate[0]:
            return True
        # if currentSunday is same month as enddate
        if currentSunday[0] == endDate[0]:
            # return True if currentSunday is later day than enddate
            if currentSunday[1] > endDate[1]:
                return True

    # return False if not after the enddate
    return False
