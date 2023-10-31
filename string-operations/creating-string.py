#Stirngs in python can be created using single quotes or double quotes or even triple quotes (' ', " ", ''' ''').
#example
#create a string using single quotes (' '), double quotes (" "), and triple double quotes (''' '''). The triple quotes can be used to declare multiline strings in Python.

#python program for creation of string

#creating a string with single quotes
String1 = 'Welcome to Content+Cloud'
print("String with the use of Single Quotes: ")
print(String1)

#creating a string with double quotes 
String1 = "C+C"
print("\nString with the use of Double Quotes: ")
print(String1)

#creating a string with triple quotes
String1 = '''Content+Cloud aslo C+C'''
print("\nString with the use of triple quotes: ")
print(String1)

#creating string with triple quotes allows for multiple lines 
String1 = '''Content
                +
                Cloud'''
print("\nCreating a multiline String: ")
print(String1)

#output: 
# string with the use of Single Quotes: 
#Welcome to Content+Cloud

# String with the use of Double Quotes: 
#C+C

# String with the use of triple quotes: 
#Content+Cloud aslo C+C

# Creating a multiline String:
#                Content
 #               +
  #              Cloud


##Example:
# define a string in Python and access its characters using positive and negative indexing.
#The 0th element will be the first character of the string whereas the -1th element is the last character of the string.

#python program to access characters of strings
String1 = "Content + Cloud"
print("Initial String: ")
print(String1)

# printing first character
print("\nFirst character of String is: ") 
print(String1[0])

# printing last character
print("\nLast character of String is: ")
print(String1[-1])
#output: 
# Initial String: Content + Cloud

#First character of String is: C

#Last character of String is: d

#Example:

#use the string-slicing method to extract a substring of the original string. 
# The [3:12] indicates that the string slicing will start from the 3rd index of the string to the 12th index, 
# (12th character not including). We can also use negative indexing in string slicing.

#Python program to demonstrate string sclicing
# creating a string
String1 = "Content&Cloud"
print("Initial String: ")
print(String1)

# printing 3rd to 13th character
print("\nSlicing characters from 3-13: ")
print(String1[3:13])

#printing characters between 3rd and 2nd last character
print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print(String1[3:-2])
#output: 
# Initial String: Content&Cloud

#Slicing characters from 3-13: tent&Cloud

#Slicing characters between 3rd and 2nd last character: tent&Clo