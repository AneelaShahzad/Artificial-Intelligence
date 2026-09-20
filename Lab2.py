# LAB 2
#------------------------------------------------------------------------#
# -> Iterative structures

#while loop

count=10
while count>5:
    print(count)
    count=count-1

#single statement while block:
count=5
while count>0: print(count);count=count-1

#For-in loop
li=['red','black','purple','pink','blue']
for x in li:
    print(x)

#iterating by index of sequence:
for idx in range(len(li)):
    print(li[idx])

li=[1,2,3,4,5]
for x in li:
    if x==3:
        continue
    print(x)

for x in li:
    if x==3:
        break
    print(x)

#------------------------------------------------------------------------#

# ->Functions

#simple function:
def first_function():
    print("this is my first function!")

#calling function for execution:
first_function()

#function with parameters:
def name_func(n):
    print("name is : ",n)

name_func("Aneela Shahzad")  #Aneela Shahzad
name_func("Arfa")  #Arfa

#function with default parameters:
def city_func(c="Gujranwala"):
    print("I am from ",c)

city_func("Lahore") #Lahore
city_func("Islamabad") #Islamabad
city_func()

#passing list as a parameter
def display_list(li):
    print("full list :",li)
    for idx in range(len(li)):
        print(f'idx {idx} : ',li[idx])

my_favs=["october","purple","tulips","mint"]
display_list(my_favs)

#returning value from a function
def sum(n1,n2):
    return n1+n2

print(sum(2,2))

#arguments with key and value pairs
def children(child1,child2):
    print("child 1 : ",child1,"\nchild 2 : ",child2)

children(child2="Emil",child1="John")


#------------------------------------------------------------------------#
# -> OOP in Python

#Classes:
class student:
    program="Comp Sci"
    def __init__(self,name,cgpa):
        print("I am an init function")
        self.name=name
        self.cgpa=cgpa
    def print_details(self):
        print("my name is",self.name,"I am studying",self.program,"with cgpa of",self.cgpa)

#object or instance of class
s1=student("Aneela Shahzad", 3.94)
print(s1.name)
print(s1.cgpa)
s1.print_details()