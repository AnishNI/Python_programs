"""#python programs.
print("Hello")

#Addition in python
print(2 +3)

#String
name = "Alice"
print(name)

#integer
age = 25
print(age)

#Float
height = 5.6
print(height)

#Boolean
is_student =True
print(is_student)

#This is Comment
print("Python is fun!")

#Basic Operations
#Addition 
x = 10
y= 5
sum = x+y
print(sum)

#subtraction
difference= x-y
print(difference)

#Multiplication

product= x*y

print(product)

#Division

product= x/y

print(product)

#modulus
product= x%y

print(product)

#Exponentiation **
print(3**4)

#Floor Division //
print(9 // 2)

#Comparision Operator 
x=10
y=5
print(x>y)
print(x==y)

# how to take input from user
name = input("Enter your name:")

age = int(input("Enter Your Age"))
print(f"Hello {name},your age {age}years old.")

# space difference 
print(117 + 986)
print(199 - 981)
print(3+4+5-6)
print(3+4)
print(3 + 4)


#variables in python variables cant start with number 
spend =3
donated =4
total_amount = spend + donated
print(total_amount)


items = 10 
price = 2
total_price= items * price
print(total_price,items,price)

# Types 
x = 10
y = "10"
z = 10.1 

sum1 = x+x
sum2 = y+y
print(sum1,sum2)
print(type(x),type(y),type(z))

# List in Python
student_grades =[9,8.8,7.5,"hello",[1,2,4,3.3]]
print(student_grades *3)   # it will print list 3 times.
print(student_grades + student_grades) #  

# List in Range
student_grades=list(range(0,11,2))  # statr with 0 to 11 in step of 2 you can have any step here.

print(student_grades)


# Data Types Attributes
to get more data types help in cosole.
dir(list)



#calculate 
student_grades=[1,11,22,2,44,55,66,69]
# Dictonary is pair of key and values
student_grades={"Marry":9.1,"Sim":1,"John":2}

mysum = sum(student_grades)
length=len(student_grades)
mean=mysum/length
max_value = max(student_grades)
print(max_value)
print(mean)



# Tuple are imputable cant change
monday_temp =(1,4,5,6)


#Data types of list

seconds =[1.23,1.45,1.02]
current = 1.01
seconds.append(current)
seconds.remove(1.23)
print(seconds)

def mean(mylist):
    the_mean=sum(mylist)/len(mylist)
    return the_mean

print(mean([1,4,5]))
print(type(sum),type(mean))


def temp(value):
    if value >= 7:
        return "warm"
    else:
        return "cold"  # Fixed indentation

temp_no = int(input("Enter number"))
print(temp(temp_no))


#string length check max 8 lengths
def check_length(name):
    if len(name) >= 8:
        return True
    else:
        return False

user_input = str(input("Enter string"))
print(check_length(user_input))      

#eliif conditions
def check_length(name,k):
    if k == name :
        return "Item is present in store"
    elif name == k:
        return "Item is also present in Store list"

    else:
        return "Item is not present in store"

Item_name={"book":1,"toy":2,"pencil":3}
store_list={"book":1,"toy":2,"pencil":3}
OR 
Item_name=["book","toy","pencil"]
store_list=["book","toy","pencil"]

print(check_length(Item_name[0],store_list[0]))

print(check_length(Item_name["book"],store_list["book"]))


#Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")


#Use the or operator to check if at least one condition is True:

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")


#Check if a value is of a particular type with isinstance:

isinstance("abc", str)
isinstance([1, 2, 3], list)
or directly:

type("abc") == str
type([1, 2, 3]) == lst



#Write if-elif-else conditionals:

message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")



#More String Formatting
#There is also another way to format strings using the "{}".format(variable) form. Here is an example:

name = "John"
surname = "Smith"
 
message = "Your name is {}. Your surname is {}".format(name, surname)
print(message)
#Output: Your name is John. Your surname is Smith


#A Python program can get user input via the input function:


#The input function halts the execution of the program and gets text input from the user:

name = input("Enter your name: ")


#The input function converts any input to a string, but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12


#You can also format strings with:

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
#Output: Hi Sim, you have 1.5 years of experience.


#for loop
#A for loop is used to iterate over a sequence (such as a list, tuple, dictionary
#or set) or other iterable objects (such as strings).
#Here is an example:

colors = [11,12,13,14,15,16,17,18,60,90,88,56,4.0,5.0]

for color in colors:
    if isinstance(color,int):
     if color >50:
        print(color)


#A for loop can also be used to execute a function multiple times. For example, below we are executing celsius_to_kelvin three times since there are three items in the iterating list:



def celsius_to_kelvin(cels):
    return cels + 273.15
 
for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))


#The output of that would be:

# 282.25
# 281.95
# 3.0

#So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).        
#this for dictonary to iterate with loops
student_grades ={"Marry":9.1,"Sim":8.8,"John":7.5}
for grade in student_grades.items():
    print(grade)


 # Dictionary Loop and String Formatting
#Here is an example that combines a dictionary loop with string formatting. The loop iterates over the dictionary and it generates and prints out a string in each iteration:



phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")


#And here is a better way to achieve the same results by iterating over keys and values:

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")


#In both cases, the output is:

#John has as phone number +37682929928

#Marry has as phone number +423998200919   


for i in [1,2,3]:
    print(i)

a = 3

while a > 0:
    print(1)
    print(2) 

#while loop

user_name = ''
while user_name != "pypy":
    user_name = input("Enter your name: ")
    
while True:
    username = input("Enter username:")
    if username == 'pypy':
        break
    else:
        continue
  
      Cheatsheet: Loops
In this section, you learned the following:

A for-loop is useful to repeatedly execute a block of code.

You can create a for-loop like so:

for letter in 'abc':
    print(letter.upper())
Output:

A
B
C

As you can see, the for-loop repeatedly converted all the items of 'abc' to uppercase.

The name after for (e.g. letter) is just a variable name



You can loop over dictionary keys as follows:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
Output:

John Smith
Marry Simpsons

You can loop over dictionary values:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
Output:

+37682929928
+423998200919



You can loop over dictionary items:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
Output: 

John Smith +37682929928
Marry Simpons +423998200919


We also have while-loops. The code under a while-loop will run as long as the while-loop condition is true:

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
The loop above will print out the string inside print() over and over again until the 20th of August, 2090.
          




In this section, you learned that:

A list comprehension is an expression that creates a list by iterating over another container.

A basic list comprehension:

[i*2 for i in [1, 5, 10]]
Output: [2, 10, 20]

List comprehension with if condition:

[i*2 for i in [1, -2, 10] if i>0]
Output: [2, 20]

List comprehension with an if and else condition:

[i*2 if i>0 else 0 for i in [1, -2, 10]]
Output: [2, 0, 20]


              
def foo(lst):
    return [i for i in lst if isinstance(i,int)]    



    In this section, you learned that:

Functions can have more than one parameter:

def volume(a, b, c):
    return a * b * c
Functions can have default parameters (e.g. coefficient):

def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10))
Output: 3.0480370641306997

Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):

def volume(a, b, c):
    return a * b * c
 
print(volume(1, b=2, c=10))
An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:

def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
Output: 1001

A **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
Output: Sim

Here's a summary of function elements:

https://img-c.udemycdn.com/redactor/raw/2019-07-24_19-07-36-0d306e1785ef65d50aeb204567dfb62f.png


myfile = open("read.txt")
print(myfile.read())




Cheatsheet: File Processing
In this section, you learned that:

You can read an existing file with Python:

with open("file.txt") as file:
    content = file.read()
You can create a new file with Python and write some text on it:

with open("file.txt", "w") as file:
    content = file.write("Sample text")
You can append text to an existing file without overwriting it:

with open("file.txt", "a") as file:
    content = file.write("More sample text")
You can both append and read a file with:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()



    In this section, you learned that:

Builtin objects are all objects that are written inside the Python interpreter in C language.

Builtin modules contain builtins objects.

Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

import time
time.sleep(5)
A list of all builtin modules can be printed out with:

import sys
sys.builtin_module_names
Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

Packages are a collection of .py modules.

Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

Third-party libraries can be installed from the terminal/command line:

Windows:

pip install pandas or use python -m pip install pandas if that doesn't work.

Mac and Linux:

pip3 install pandas or use python3 -m pip install pandas if that doesn't work.
"""        

