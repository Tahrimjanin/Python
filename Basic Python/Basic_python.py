print("Hello world")

#indentation
if 10 > 5 :
    print("ten is greater than five!")
    
print(bool("Hello"))
print(bool(15))
    
#variable
x = 5 
y = "hello"

print(x)
print(y)

x = 4 
x = "Sally"
print(x) #overwrite the previous value.so x holds the string.

#legel variable
myvar = "Jeny" 
my_var = "Jeny" 
_my_var = "Jeny"
myVar = "Jeny"
MYVAR = "Jeny"
myvar2 = "Jeny"

x,y,z = "a" ,"b", "c"
print(x,y,z)


x = y ="ABC" #one value in multipale variable
print(x)
print(y)

#unpack a collection

letter =["A","B","C"]
x,y,z = letter 
print(x,y,z)


#casting
x= str(7)
y=int(7)
Z=float(7)
print(x,y,z)

#Type Conversion
#int to complex
A= 3 
B = complex(A)
print(B)

#type function
x = 10
print(type(x))

#sum
x=7
y=5
z=2
print(x + y + z)

#global function
#create variable inside a function

x= "town" #global variable

def function():
 x="sirajgonj" #local variable
 print(x + " is awesome")

function()
print("This is a "+ x)

# create  a outsite variable

x="tahrim janin"
def function():
    print("My name is "+ x)
function()

#global keyword

def function():
    global x
    x= "janin"
function()
print("My name is "+ x)
 
#Data type

a= complex(7j)
b=list(("AB","CD","EF"))
c=tuple(("AB","CD","EF"))
d=range(7)
e=dict(name="Jeny", age=21) #dict= dictonary
f=set(("ab", "bc", "cd"))
g= frozenset(("a", "b", "c"))
h=bool(0) 
i=bytes(7)
j=bytearray(7)
k=memoryview(bytes(5))

print(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}')

#Random Number
import random
print(random .randrange(1,9))

#string are array
x="jeny"
print(x[0])

#string looping

for x in "tahrim":
  print(x)
  
#String Length
a= "tahrim"
print(len(a))

#Check String
txt = "tahrim janin!"
print("janin" in txt)

#check string using if state.
txt = "tahrim janin!"
if "tahrim" in txt:
  print("Yes, 'tahrim' is present.")

#check string using if not .
txt = "janin!"
print("tahrim" not in txt)

txt = "janin!"
if "tahrim" not in txt:
  print("TRUE.")
  
  #Slicing
  
A= "bangladesh"
print(A[2:7]) #2 to 7

A= "bangladesh"
print(A[:7])

A= "bangladesh"
print(A[2:])  

A= "bangladesh"
print(A[-2:-7]) 

#Upper ,lower case and remove whitespace 
A= "Bangla desh"
print (A.upper())
print (A.lower())
print (A.strip())

#Replace and Split String
a = "Home!"
print(a.replace("H", "J")) #replace H with J
print(a.split("!")) #split the string into list

#Str_concat
a = "Tahrim"
b = "Janin"
c = a + " "+ b
print(c)

#Str format
age = 21
txt = "My name is Jeny, I am " + str(age)
print(txt)

#F-Str
age = 21
txt = f"My name is Jeny, I am {age}"
print(txt)

#Placeholders and Modifiers
price = 100
txt = f"The price is {price} tk"
print(txt)

txt = f"The price is {price:.2f} tk"
print(txt)

#Escape Characters
print('1. Single Quote: I\'m jeny')
print("2. Double Quote: she said, \"Hello!\"")
print("3. This is a backslash: \\")

print("4. New Line:\nThis text appears on a new line")
print("5. Tab Space:\tThis text is tabbed")
print("6. Backspace: Helloo\b!")  # removes last 'o'

print("7. Carriage Return: Hello\rWorld")  # replaces Hello with World
print("8. Form Feed: Hello\fWorld")  # form feed (mostly visual in editors)

print("9. Bell Sound (Beep): \a")  # may make a beep sound (if supported)

# Octal and Hexadecimal ASCII values
print("10. Octal Value \\101: \101")  # A (octal 101 = ASCII 'A')
print("11. Hex Value \\x41: \x41")    # A (hex 41 = ASCII 'A')


#bool
# bool() func returns False :

print(bool(False))     
print(bool(None))      
print(bool(0))         
print(bool(""))        
print(bool([]))        
print(bool(()))        
print(bool({}))        

# __len__ function
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# bool() func returns True :
def myFunction():
  return True
print(myFunction())

#isinstance() func
x = 7
print(isinstance(x, int))

