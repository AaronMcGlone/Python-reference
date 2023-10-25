#In Python, isupper() is a built-in method used for string handling. This method returns “True” if all characters in the string are uppercase, otherwise, returns “False”. 

#It returns “True” for whitespaces but if there is only whitespace in the string then returns “False”.
#It does not take any arguments, Therefore, It returns an error if a parameter is passed.
#Digits and symbols return “True” but if the string contains only digits and numbers then returns “False”
#This function is used to check if the argument contains any uppercase characters such as:

string = 'GEEKFORGEEK'

Input: string = 'GEEKSFORGEEKS'
#Output: True
#Syntax of isupper()
Syntax: string.isupper() 

#isupper() does not take any parameters 
#Returns: True- If all characters in the string are uppercase. False- If the string contains 1 or more non-uppercase characters.


#In this code string variable contain value “GEEKSFORGEEKS”- 
# . String consist of only uppercase letters. When this call the “isupper”method on string ,
#  It will return “True” and when it checks the other string “GeeksforGeeks” that is mix of upper and lower string it will return “False“.


string = 'GEEKSFORGEEKS' # Define a string containing only uppercase letters 
print(string.isupper())  # Check if all characters in the string are uppercase and print the result 
  
string = 'GeeksforGeeks'# Define a string with a mix of uppercase and lowercase letters 
print(string.isupper()) # Check if all characters in the string are uppercase and print the result 

#Output:True False

#islower() is a built-in method used for string handling. The islower() method returns True if all characters in the string are lowercase, otherwise, returns “False”. 
# 1.It returns “True” for whitespaces but if there is only whitespace in the string then returns “False”.
# 2.It does not take any arguments, Therefore, It returns an error if a parameter is passed.
# 3.Digits and symbols return “True” but if the string contains only digits and numbers then returns “False”.

string = 'geeksforgeeks' #output: true

Sintax: string.islower()
#parameter: islower() doesn't take any params
# will return true if all characters in the sring are lowercase
# will return false if any characters are in the string uppercase

string = 'geeksforgeeks'# Define a string containing only lowercase letters 
print(string.islower()) # Check if all characters in the string are lowercase and print the result 
  
string = 'GeeksforGeeks' # Define a string with a mix of uppercase and lowercase let 
print(string.islower())  # Check if all characters in the string are lowercase and print the result 

#The lower() method returns the lowercased string from the given string-
#  It converts all uppercase characters to lowercase python. If no uppercase characters exist, it returns the original string. 

#It does not take any arguments, Therefore, It returns an error if a parameter is passed.
#Digits and symbols return are returned as it is, Only an uppercase letter is returned after converting to lowercase in Python.

string = 'GEEKSFORGEEKS' #output = 'geeksforgeeks'

#lower() doesn't take any params it converts the given string into lowercase and returns the string

# Checking for lowercase characters 
string = 'GEEKSFORGEEKS' #Define a string that contains only uppercase. 
print(string.lower()) #convert into lower case 
  
string = 'GeeksforGeeks' #Define a string that contains noth uppercase and lowercase. 
print(string.lower()) #convert into lower case.

# both output geeksforgeeks

#lower() is a built-in method used for string handling. The lower() method returns the lowercased string from the given string.
#  It converts all uppercase characters to lowercase python. If no uppercase characters exist, it returns the original string. 

#It does not take any arguments, Therefore, It returns an error if a parameter is passed.
# Digits and symbols return are returned as it is, Only an uppercase letter is returned after converting to lowercase in Python.

string = 'GEEKFORGEEK'
#output: geekforgeek

#lower() does not take any parameters
#Returns: It converts the given string in into lowercase and returns the string.


# Checking for lowercase characters 
string = 'GEEKSFORGEEKS' #Define a string that contains only uppercase. 
print(string.lower()) #convert into lower case 
  
string = 'GeeksforGeeks' #Define a string that contains noth uppercase and lowercase. 
print(string.lower()) #convert into lower case.

#upper() is a built-in method used for string handling. The upper() method returns the uppercased string from the given string. 
# It converts all lowercase characters to uppercase. If no lowercase characters exist, it returns the original string. 

#It does not take any arguments, Therefore, It returns an error if a parameter is passed.
#Digits and symbols return are returned as it is, Only a lowercase letter is returned after converting to uppercase.
Input: string = 'geeksforgeeks'
#Output: GEEKSFORGEEKS

#Syntax of upper()
Syntax: string.upper()

#upper() does not take any parameters
#Returns: It converts the given string in into uppercase and returns the string.

#In this code use upper() method to convert the strings to uppercase. Firstly take lowercase string”geeksforgeeks” that is converted to uppercase() with the help of string.upper()
#  function. Same we will try with the string that contains both upper and lower case “My name is ayush” then function will convert this to lower case.


# checking for uppercase characters 
string = 'geeksforgeeks' #Define a string that contains only lowercase() 
print(string.upper()) #Convert into uppercase 
  
string = 'My name is ayush' #Define a string that contains only lower case 
print(string.upper()) #convert into uppercase. 
#Output:
#GEEKSFORGEEKS
#MY NAME IS AYUSH
#Count uppercase, lowercase letters, and spaces
#Given a string, the task is to write a Python Program to count a number of uppercase letters, lowercase letters, and spaces in a string and toggle case the given string (convert lowercase to uppercase and vice versa).

Input : string = 'GeeksforGeeks is a computer Science portal for Geeks'
#Output : Uppercase - 4
         #Lowercase - 41
         #spaces - 7
         #gEEKSFORGEEKS IS A COMPUTER sCIENCE PORTAL FOR gEEKS