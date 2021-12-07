from dates import *

# runtime for countFirstDaySundaysBetween([1, 1, 1901], [12, 31, 2000]) us 0.378s

# counts sundays on the first day of the month within the date range
# countFirstDaySundaysBetween([startMonth, startDay, startYear], [endMonth, endDay, endYear])
# startDate and endDate included in range
def countFirstDaySundaysBetween(startDate, endDate):
    # first known sunday from problem
    currentSunday = [1, 7, 1900]
    # keep track of days in month
    daysInMonth = getDaysInMonth(currentSunday[0], currentSunday[2])
    # keep count of sundays
    firstDaySundayCount = 0

    #while sunday is before or equal to enddate
    while isEqualBeforeDate([currentSunday[0], currentSunday[1], currentSunday[2]], endDate) == True:

        # if next sunday in same month
        if currentSunday[1] + 7 <= daysInMonth:
            # increment sunday
            currentSunday[1] += 7

            # if sunday is within the date range
            if isAfterDate(currentSunday, startDate) == True:
                # if sunday is the first day of the month
                if currentSunday[1] == 1:
                    # increment count
                    firstDaySundayCount += 1

        # if next sunday in next month
        else:
            # increment sunday to next month
            currentSunday[1] = (currentSunday[1] + 7) % daysInMonth

            # if sunday is within the date range
            if isAfterDate(currentSunday, startDate) == True:
                # if sunday is the first day of the month
                if currentSunday[1] == 1:
                    # increment count
                    firstDaySundayCount += 1

            # if next sunday in next year
            if currentSunday[0] == 12:
                # update year
                currentSunday[2] += 1
                # update month
                currentSunday[0] = 1
            # if next sunday in same year next month
            else:
                # update month
                currentSunday[0] += 1

            #get days in month
            daysInMonth = getDaysInMonth(currentSunday[0], currentSunday[2])

    return firstDaySundayCount
