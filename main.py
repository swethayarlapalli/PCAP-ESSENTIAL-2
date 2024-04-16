#PYTHON ESSENTIAL -2 PROGRAMS.
#PROGRAM-1
#Import is a keyword
import math
import math
#PROGRAM-2
#Import sys is a key word
import sys
import math, sys
# PROGRAM-2
#Importing a module: continued
math.pi
math.sin
import math
print(math.sin(math.pi/2))
# PROGRAM-3
# We've defined our own pi and sin here.
import math
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))
# PROGRAM-4
#Importing a module
from math import sin, pi
print(sin(pi / 2))
pi = 3.14
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi / 2))
#PROGRAM-5
#Selected functions from the math module
from math import pi, radians, degrees, sin, cos, tan, asin
ad = 90
ar = radians(ad)
ad = degrees(ar)
print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
#PROGRAM-6
#math's functions is formed by functions which are connected with exponentiation
from math import e, exp, log
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
#PROGRAM-7
#general-purpose functions
from math import ceil, floor, trunc
x = 1.4
y = 2.6
print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
#PROGRAM-8
#Selected functions from the random module
from random import random
for i in range(5):
    print(random())
#PROGRAM-9
#The randrange and randint functions
from random import randrange, randint
print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
#PROGRAM-10
#The platform function
from platform import platform
print(platform())
print(platform(1))
print(platform(0, 1))
#The machine function
from platform import machine
print(machine())
#The processor function
from platform import processor
print(processor())
#The system function
from platform import system
print(system())
#The version function
from platform import version
print(version())
#PROGRAM-11
#The python_implementation and the python_version_tuple functions
from platform import python_implementation, python_version_tuple
print(python_implementation())
for atr in python_version_tuple():
    print(atr)
# PROGRAM-12
#Modules
counter = 0
if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

#Example of a python module
""" module.py - an example of a Python module """
__counter = 0
def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum
def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod
if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
#regular value
import sys
for p in sys.path:
    print(p)
#PROGRAM-13
#Strings
# Example 1
word = 'by'
print(len(word))
# Example 2
empty = ''
print(len(empty))
# Example 3
i_am = 'I\'m'
print(len(i_am))
#Multiline strings
multiline = '''Line #1
Line #2'''
print(len(multiline))
#Operations on strings
str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
#PROGRAM-14
#Operations on strings: ord()
char_1 = 'a'
char_2 = ' '  # space
print(ord(char_1))
print(ord(char_2))
#Operations on strings: chr()
print(chr(97))
print(chr(945))
#PROGRAM-15
# Slices
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
#PROGRAM-16
#The in and not in operators
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
#PROGRAM-17
#Operations on strings: continued
alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)
#Operations on strings: min()
# Demonstrating min()
print(min("aAbByYzZ"))
# Demonstrating min()
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
t = [0, 1, 2]
print(min(t))
#Operations on strings: max()
print(max("aAbByYzZ"))
# Demonstrating max() - Examples 1& 2:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))
#Operations on strings: the index() method
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
#PROGRAM-18
#Operations on strings: the list() function
print(list("abcabc"))
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))
#The capitalize() method
print('aBcD'.capitalize())
#The center() method
print('[' + 'alpha'.center(10) + ']')
#The endswith() method
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
#The find() method
print("Eta".find("ta"))
print("Eta".find("mma"))
#The isalnum() method
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())
# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())
# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
#The join() method
print(",".join(["omicron", "pi", "rho"]))
#The lower() method
print("SiGmA=60".lower())
#The lstrip() method
print("[" + " tau ".lstrip() + "]")
#The replace() method
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
#The rfind() method
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
#The rstrip() method
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
#The split() method
# Demonstrating the split() method:
print("phi       chi\npsi".split())
#The startswith() method
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()
# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")
#The swapcase() method
print("I know that I know nothing.".swapcase())
print()
# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())
print()
# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())
#PROGRAM-19
#Sorthing
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
print()
# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
second_greek.sort()
print(second_greek)
#PROGRAM-20
#The Caesar Cipher: encrypting a message
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
print(cipher)
#PROGRAM-21
#The Caesar Cipher: decrypting a message
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)
#PROGRAM-22
#The Numbers Processor
line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")

#PROGRAM-23
# IBAN Validator.
iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

#PROGRAM-24
#Exceptions: continued
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")
print("THE END.")

#Exceptions: continued
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")
print("3")

#Exceptions: continued
try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")
print("THE END.")

#The anatomy of exceptions
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise
try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
#PROGRAM-25
#The stack - the procedural approach
stack = []
def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val
push(3)
push(2)
push(1)
print(pop())
print(pop())
print(pop())
#The stack - the object approach
class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")
stack_object = Stack()  # Instantiating the object.

#The object approach: a stack from scratch
class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
stack_object = Stack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)
print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
#The object approach: a stack from scratch (continued)
class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
#PROGRAM-26
#instance variables:
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val
    def set_second(self, val = 2):
        self.__second = val
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.__third = 5
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
#PROGRAM-27
#Class variables:
class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)
#PROGRAM-28
#Methods in detail
class Classy:
    def method(self):
        print("method")
obj = Classy()
obj.method()

#Methods in detail: continued
class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)
#PROGRAM-29
#The inner life of classes and objects:
class SuperOne:
    pass
class SuperTwo:
    pass
class Sub(SuperOne, SuperTwo):
    pass
def printBases(cls):
    print('( ', end='')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')
printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
#PROGRAM-30
#Investigating classes
class MyClass:
    pass
obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5
def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)
print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

#PROGRAM-31
#Inheritance: issubclass()
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

#Inheritance: isinstance()
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()
for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

#Inheritance: the is operator
class SampleClass:
    def __init__(self, val):
        self.val = val
object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1
print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)
string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"
print(string_1 == string_2, string_1 is string_2)

#PROGRAM-32
#How to build a hierarchy of classes:
import time
class TrackedVehicle:
    def control_track(left, stop):
        pass
    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)
class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass
    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)

#PROGRAM-33
#The diamond problem
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
d = D()

#PROGRAM-34
#Generators - where to find them:
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret
