#DateTime to unix timestamp

#For converting python DateTime to unix timestamp, I;ve imported a module called datetime and time in this example,
#and the variable date_time has been declared and assigned datetiime. time/date (2023, 10, 30, 10, 54).-YYYY, MM, DD, HH, MM

# importing datetime module
import datetime 
import time

# assigned regular python date&time
date_time = datetime.datetime(2023, 10, 30, 10, 54)

# print regular string date
print("date_time =>",date_time)

# displaying unix timestamp after conversation
print("unix_timestamp => ",
       (time.mktime(date_time.timetuple())))

# output: date_time => 2023-10-30 10:54:00
# unix_timestamp =>  1698663240.0


#Explanation:

#Date and time manipulation classes are provided by the datetime module. The inverse function of local time is mktime().
#  It accepts a struct time or a full 9-tuple as an argument and returns a floating-point number to be compatible with time (). 
# It is also used to convert a datetime to a Unix timestamp.

#The timetuple() method of datetime.date objects return a time object.struct time.
#  The struct time object is a named tuple that may be retrieved using either an index or by name. The year, month, and day fields of the named tuple returned by the 
# timetuple() function will be set according to the date object, while the hour, minutes, and seconds fields will be set to zero

##DateTime to Unix timestamp with 13 digits
# to obtain the current time, use satetime.now(). The timetuple() function of the datetime class returns the datetime's properties as a named tuple. The timestamp with 13 digits must
#be multiplied by 1000

import time
import datetime

presentDate = datetime.datetime.now()
unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
print(unix_timestamp)
#output: 1698664439018.491

##DateTime to Unix timestamp in UTC Timezone
#The calendar module provides helpful calendar-related functions. The utc.now function returns the current time in the UTC timezone. 
# In the time module, the timegm function returns a Unix timestamp.
#The timetuple() function of the datetime class returns the datetime’s properties as a named tuple. To obtain the Unix timestamp, use print(UTC).

import calendar
import datetime

date = datetime.datetime.utcnow()
utc_time = calendar.timegm(date.utctimetuple())
print(utc_time)
#output: 1698665294

##Datetime.date to Unix timestamp
# time.date() is a function that accepts just dates. In this case, 2023 is the year, 10 is the month, and 30 is the day. mktime() is a
#time mthod that is the inverse function of local time; it is used to convert dates to Unix timestamps.

import datetime
import time

my_datetime = datetime.date(2023, 10, 30)
print("Unix_Time: ",
      (time.mktime(my_datetime.timetuple())))
#output: Unix_Time:  1698624000.0

##DateTime string to Unix timestamp
# the date and time are supplied in string format in this case. Here, 10 is the month, 30 is the day, 2023 is the year, 11 is the hour, 35 is the minute, and 8 is the second.strptime()
# is a datetime module method that is used to convert strings to datetime and time objects. The timestamp() function returns the current location.

import datetime

date_example = "10/30/2023, 11:35:8"
date_format = datetime.datetime.strptime(date_example,
                                         "%m/%d/%Y, %H:%M:%S")
unix_time = datetime.datetime.timestamp(date_format)
print(unix_time)
#output: 1698665708.0

##Unix timestamp to python DateTime
# The DateTime module in python is used to deal with date and time-related issues in Python. The fromtimestamp() method is one of the functions included in this module. 
# The date class's function fromtimestamp() computes and returns the date corresponding to a specified timestamp. 
# The allowed timestamp range extends from 1970 to 2038. If there are any leap seconds in the timestamp, the fromtimestamp() function ignores them.

#To begin with, import the datetime class from the datetime module. The UNIX value object is then stored in a variable.
# Then use the datetime.fromtimestamp() method to retrieve the time and date. 

#The strftime() function is another function within the datetime module. This function aids in the return of a DateTime in a particular format.
#This function is used to convert date and time objects to string representations. 
# The format codes in the above code are %d, %m, %Y, %H, %M, and %S, which indicate days, months, years, hours, minutes, and seconds, respectively.

# importing datetime module 
import datetime

# assigned unix time
unix_time = Unix_Time = 1698667772

date_time = datetime.datetime.fromtimestamp(unix_time)

# print unix time stamp
print("Unix_Time =>",unix_time)

# displaying date and time in a regular string format
print("Date & Time =>" ,
      date_time.strftime( '%Y-%m-%d %H:%M:%S'))
#output: Unix_Time => 1627334400
#Date & Time => 2023-10-30 12:09:32
