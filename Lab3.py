import random
# #1
for x in range(1500,2701,1):
    if(x%7==0 and x%5==0):
        print(x)


#--------------------------------------------------------------------------

# #2
def celcius_to_fahrenheit(c):
    return c*9/5+32
def fahrenheit_to_celcius(f):
    return (f-32)* 5/9
c=60
f=45
print(f'{c} is {round(celcius_to_fahrenheit(c))} F in fahrenheit and {f} is {round(fahrenheit_to_celcius(f))} C in Fahrenheit')

#--------------------------------------------------------------------------


# #3:
num=int(input("Guess a number between 1 to 9: "))
number = random.randint(1, 9)

while (num!=number):
    num=int(input("Wrong! Guess again : "))

print("Well guessed!")

#--------------------------------------------------------------------------

#4
for x in range(1,10):
    if x<6:
        for m in range(1,x+1):
            print("*",end="")
        print("")
    else:
        for m in range(1,11-x):
            print("*",end="")
        print("")

#--------------------------------------------------------------------------


#5
word=input("enter a word : ")
l=len(word)-1
w2=""

for x in range(0,len(word)):
    # print(word[x])
    w2=w2+word[l]
    l=l-1

print(word)
print(w2)

#--------------------------------------------------------------------------


#6
li=[12,34,55,78,90,30,60,37]
print("series : ",li)
even=0
odd=0
for x in li:
    if x%2==0:
        even=even+1
    else:
        odd=odd+1

print(f'number of even numbers : {even} \n number of odd numbers : {odd}')

#--------------------------------------------------------------------------


#7
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],{"class":"V","section":'A'}]
for x in datalist:
    print(x, type(x))

#--------------------------------------------------------------------------


#8
for x in range(0,7):
    if x==3 or x==6:
        continue
    print(x,end=" ")

#--------------------------------------------------------------------------


#9

a=0
b=1

while b<=50:
    print(b,end=" ")
    a=b
    b=a+b

#additional task

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

#--------------------------------------------------------------------------


#10
rows=int(input("enter rows : "))
cols=int(input("enter columns : "))
li=[]
for x in range(rows):
    r=[]
    for y in range(cols):
        r.append(x*y)
    li.append(r)

print(li)

#--------------------------------------------------------------------------


#11
lines = []
while True:
    line = input("Enter a line: ")

    if line == "":
        break
    lines.append(line)

print("Output:")

for line in lines:
    print(line.lower())

#--------------------------------------------------------------------------


#12

#--------------------------------------------------------------------------

#13
str=input("enter a string : ")
letters=0
digits=0
for x in str:
    if x.isdigit():
        digits=digits+1
    if x.isalpha():
        letters=letters+1

print(f'string : {str}')
print(f'no. of letters : {letters} \nno. of digits : {digits}')


#--------------------------------------------------------------------------



#14
password = input("Enter password: ")
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "$#@" for c in password)
if (len(password)>=6 and  len(password)<= 16 and
        has_lower and has_upper and has_digit and has_special):
    print("Valid password")
else:
    print("Invalid password")
    