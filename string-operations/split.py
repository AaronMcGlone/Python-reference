#Python String split() method in Python split a string into a list of strings after breaking the given string by the specified separator.
#more infomation at: https://www.geeksforgeeks.org/python-string-split/
#Syntax: str.split(separator,maxsplit)

#Parameters:
# separator: This is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.
# maxsplit: It is a number, which tells us to split the string into maximum of provided number of times. If it is not provided then the default is -1 that means there is no limit.

# Returns : Returns a list of strings after breaking the given string by the specified separator.

string = "one,two,three"
word = string.split(',')
print(word)
#output: ['one','two','three']

#using the Python String split() function to split different Strings into a list, separated by different characters in each case.

text = 'geeks for geeks'

#splits at space
print(text.split())
#words: ['geeks', 'for', 'geeks']

#splits at ','
#print(word.split(','))
#word = 'geeks:for:geeks'

# Splitting at ':' 
#print(word.split(':'))
#word: 'CatBatSatFatOr'

#The maxsplit parameter is used to control how many splits to return after the string is parsed-
#  Even if there are multiple splits possible, it’ll only do maximum that number of splits as defined by maxsplit parameter.

word = 'geeks, for, geeks, pawan'

#maxsplit: 0
print(word.split(',',0))

# maxsplit:4
print(word.split(',',4))

#maxsplit: 1
print(word.split(',',1))
#output: 
# ['geeks, for, geeks, pawan']
# ['geeks', 'for', 'geeks', 'pawan']
# ['geeks', 'for, geeks, pawan']
