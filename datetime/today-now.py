#a module named DateTime can be imported to work with the date as well as time. Datetime module comes built into Python, so there is no need to install it externally. 
# To get both current date and time datetime.now() function of DateTime module is used. This function returns the current local date and time.

# Get current date and time using now().

# importing datetime module for now().
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now()
print("Time now at greenwich meridian is:",current_time)

#timedate.now() have different attributes, same as attributes of time such as year, month date, hour, minute, and second

#Python3 code to demonstrate
# attributes of now()

#importing datatime module for now()
import datetime

#using now() to get current time
current_time = datetime.datetime.now()

#printing attributes of now().
print("the attributes of now() are : ")

print("year :", current_time.year)

print("month : ", current_time.month)

print("day : ", current_time.day)

print("hour : ", current_time.hour)

print("minute : ", current_time.minute)

print("second : ", current_time.second)

print("microsecond : ", current_time.microsecond)

#The attributes of now() are :
#year : 2023
#month :  10
#day :  25
#hour :  14
#minute :  12
#second :  55
#microsecond :  305049

# To get the date and time for a particular timezone now() takes timezone as input to give timezone-oriented output time. But these time zones are defined in pytz library. 

# for now()
import datetime
 
# for timezone()
import pytz
 
# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
 
# printing current time in india
print("The current time in india is :", current_time)
#output: he current time in india is : 2023-10-25 14:29:09.026207


#Coordinated Universal Time, These times are useful when you are dealing with Applications that have a global user for logging the events.
#  You can get the current time in UTC by using the datetime.utcnow() method

from datetime import datetime
 
print("UTC Time: ", datetime.utcnow())
#output: UTC Time:  2023-10-25 13:30:47.974722

#isoformat() method is used to get the current date and time in the following format: It starts with the year, followed by the month, the day, the hour, the minutes, seconds, and milliseconds.

from datetime import datetime as dt
 
x = dt.now().isoformat()
print('Current ISO:', x)

 #The Python time module, allows you to work with time in Python. It provides features such as retrieving the current time, pausing the program’s execution, and so on. So, before we begin working with this module, we must first import it.

#Get the current time using the time 
#Here, we are getting the current time using the time module.

import time
 
current_time = time.strftime("%H:%M:%S", time.localtime())
 
print("Current Time is :", current_time)
#Output:
#Current Time is : 16:19:13

#Get Current Time In Milliseconds using time 
#Here we are trying to get time in milliseconds by multiplying time by 1000.

import time
 
millisec = int(round(time.time() * 1000))
 
print("Time in Milli seconds: ", millisec)
#Output:
#Time in Milli seconds:  1655722337604

# get time in nanoseconds using time.ns() method.

import time
 
curr_time = time.strftime("%H:%M:%S", time.localtime())
 
print("Current Time is :", curr_time)
 
nano_seconds = time.time_ns()
 
print("Current time in Nano seconds is : ", nano_seconds)

#Output:
#Current Time is : 16:26:52
#Current time in Nano seconds is :  1655722612496349800


#Green Mean Time, which is also known as GMT can be used by using time.gmtime() method in python just need to pass the time in seconds to this method to get the GMT 

import time
 
# current GMT Time
gmt_time = time.gmtime(time.time())
 
print('Current GMT Time:\n', gmt_time)

#Output:
#Current GMT Time:
 #time.struct_time(tm_year=2022, tm_mon=6, tm_mday=20, 
 #tm_hour=11, tm_min=24, tm_sec=59, tm_wday=0, tm_yday=171, tm_isdst=0)

#Get Current Time In Epoch using time 
#It is mostly used in file formats and operating systems. We can get the Epoch current time by converting the time.time() to an integer.


import time
 
print("Epoch Time is : ", int(time.time()))

#output: Epoch Time is :  1655723915