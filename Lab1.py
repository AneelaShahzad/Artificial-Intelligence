#comments in puthon:
#comments in oython begin with hash # character

#this is a comment


#multiple statements on a single line can be written by sepasating them using a semi colon
#eg:
print("Aneela ");print("Shahzad")



#Indentation:
#python uses indentation for defining blaocks of code as some other languages like c++, js use brackets{}
x=10

#no indentation:
# if x>5:
# print("this will give an error!")

#single space indentation:
if x>5:
 print("this is with single space indentation, no error!")
#single tab indentation:

if x>5:
    print("this is a statemnet with single tab indentation!")


#python practices:
#- use 4 spaces indentation and no tabs


#Reserved words
#python have some reserved words that cannot be used as ordinary identifiers
#eg : if, else, True, False, is, return, try, assert etc


# datatypes in python:
# python has following datatypes:

# int -> define integers values (include both negative and positive numbers with 0 as well)
# eg:
a=4
print(a)  #4 
print(type(a))  #<class 'int'>


# float -> define folating point numbers like numbers with fractional parts
# eg:
b=4.247130
print(b)  # 4.247130
print(type(b))  #<class 'float'>


# complex -> define complex numbers in maths i.e. numbers having real and imaginary parts
# eg:
c=complex(6,12)
print(c)  #(6+12j)
print(type(c))  #<class 'complex'>


#bool -> define two states either True or False
# eg:
d=4
print(d==4) #True
print(d==8) #False
h=d==8
print(type(h)) #<class 'bool'>


# strings -> for the characters , words and sentences
# eg:
name="Aneela Shahzad Ahmad"
print(name)
print(type(name))  #<class 'str'>

# special characters -> special characters with some purposes like \n, \t, \\
# eg:
print('this is a newline \n character')
print('this is a tab \t character')
print('this is a \'single quote character\'')
print('this is a \"double quote character\"')

#STRINGS

#strings follow indices practice to access any of the single character in them
#indexing can be positive(from left) and negative(from right ) as well

#positive indexing
#indices start from 0 and end at len(string)-1
# eg:
str="I love shopping"
print(str[0]) #output : I
print(str[1]) #output : 
print(str[14]) #output : g

#negative indexing
#starts from -1 and ends at - len(string)

str="I love shopping"
print(str[-1]) #output : g
print(str[-2]) #output : n
print(str[-15]) #output : I

#string slicing:
#slicing is string method in oytgon to cut a piece of string from it
#eg:
n="Aneela"
print(n[2:4]) #ee

#STRINGS ARE IMMUTABLE IN PYTHON

#LISTS
#A list is a container which holds comma-separated values between square brackets where Items or elements need not all have the same type. 
#eg:
li=["purple","october","tulips","wind"]
print(li) # it will print all elements of list


# indexing in lists
# lists elements can be accessed using indexing
# indexing can be both negative as well as positive
print(li[0]) #purple
print(li[-3]) #october

#List slicing
# lists can also be sliced as:
print(li[1:4]) #  ['october', 'tulips', 'wind']


# Conditional Statements in python:

#python follows following logical conditions:

# Equals: a == b 
num=99
if num == 99:
   print("equal to 99")

# Not Equals: a != b 
if num != 99:
   print("not equal to 99")

# Less than: a < b 
num=10
if num<20:
   print("less than 20")

# Less than or equal to: a <= b 
num=100
if num <= 100:
   print("less than or equal to 100")

# Greater than: a > b 
num=10
if num>20:
   print("greater than 20")

# Greater than or equal to: a >= b 
num=30
if num>=20:
   print("greater than or equal to 20")
