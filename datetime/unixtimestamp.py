#given a unix.timestamp T (in seconds) for a given point in time, the task is to comverte it into human-readable format

T = 3495497956

#output: DD/MM/YY and time 
#T swaps out the amount of seconds for an actuall date and time

#approach:
# 1. Convert given seconds into days by dividing them by the number of seconds in a day (86400) and store the remaining second.

# 2. alculate the current year keeping the concept of leap years in mind. Start in 1970.
#  If the year is a leap year subtract 366 from days, otherwise subtract 365. Increase year by 1.

# 3. Repeat step 2 until days become less than 365 (can not constitute a year).

# 4.Add 1 to remaining days (extra days after calculating year) because the remaining days will give us days till the previous day,
#  and we have to include the current day for DATE and MONTH calculation.

# 5.Increment the number of months by 1 and keep subtracting the number of days of the month from extra days 
# (keeping in mind that February will have 29 days in a leap year and 28 otherwise).

# 6. Repeat steps 5 until subtracting days of the month from extra days will give a negative result.

# 7. If extra days are more than zero, increment month by 1.

# 8. Now make use of the extra time from step 1.

# 9.Calculate hours by dividing extra time by 3600, minutes by dividing the remaining seconds by 60, and seconds will be the remaining seconds.


# Unix time is in seconds and Humar Readable Formate: DATE:MONTH:YEAR:HOUR:MINUTES:SECONDS,
# start of Unix time:01 JAN 1970, 00:00:00

# Function to convert unix time to human readable format 
ans = ""
def unixTimeToHumanReadable(seconds):
 
    # Save the time in Human
    # readable format
   ans = ""

    # Number of days in month
    # in normal year

daysOfMonth = [31, 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31 ]

(CurrentYear, daysTillNow, extraTime, extraDays, index, date, month, hours, minutes, seconds, flag) =(0, 0, 0, 0, 0, 
                                                                                                      0, 0, 0, 0, 0, 0)
#calculate total days unix time T
daysTillNow = seconds // (24 * 60 * 60)
extraTime = seconds % (24 * 60 * 60)
CurrentYear = 2023

#calculate current year
while (daysTillNow >= 365):
    if (CurrentYear % 400 == 0 or 
        (CurrentYear % 4 == 0 and
        CurrentYear % 100 != 0)):
        if daysTillNow < 366:
            break
        daysTillNow -= 366

    else:
        daysTillNow -= 365

    CurrentYear += 1

     # Updating extradays because it
    # will give days till previous day
    # and we have include current day

    extraDays = daysTillNow + 1

if (CurrentYear % 400 == 0 or
        (CurrentYear % 4 == 0 and
            CurrentYear % 100 != 0)):
        flag = 1
 
    # Calculating MONTH and DATE
month = 0
index = 0
 
if (flag == 1):
        while (True):
 
            if (index == 1):
                if (extraDays - 29 < 0):
                    break
 
                month += 1
                extraDays -= 29
 
            else:
                if (extraDays - daysOfMonth[index] < 0):
                    break
                month += 1
                extraDays -= daysOfMonth[index]

            index += 1


else:
    while (True):
                if (extraDays - daysOfMonth[index] < 0):
                    break
                month += 1
                extraDays -= daysOfMonth[index]

                index += 1

 
    # Current Month
    if (extraDays > 0):
        month += 1
        date = extraDays
 
    else:
        if (month == 2 and flag == 1):
            date = 29
        else:
            date = daysOfMonth[month - 1]

 
    # Calculating HH:MM:YYYY
    hours = extraTime //3600
    minutes = (extraTime % 3600) // 60
    seconds = (extraTime % 3600) % 60

    ans += str(date)
    ans += "/"
    ans += str(month)
    ans += " "
    ans += str(hours)
    ans +=  ":"
    ans += str(minutes)
    ans += ":"
    ans += str(seconds)

    #return the time
    #: return ans
#driver code
if __name__ == "__main__":

    #give unix time
    T = 1595497956

    # Function call to convert unix
    # time to human read able
    ans = unixTimeToHumanReadable(T)
 
    # Print time in format
    # DD:MM:YYYY:HH:MM:SS
    print(ans)
