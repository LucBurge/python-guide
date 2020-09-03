#In Python 3 print is a function so requires parentheses 
print("Obligatory hello world...")

#Tabs are supported but 4 spaces is the standard indentation
x = 5
if x == 5:
    print("5 is my favourite number!")

#In Python all variables are objects. Types of variable supported are integers, floating point numbers(decimal points), strings and complex numbers
mystring = "So long, and thanks for all the fish!"
myint = 37
myfloat = 5.0
if myint + myfloat == 42.0:
    print(mystring)

#Lists are similar to arrays. They can contain any type of variable.
mylist = []
mylist.append("Riddle's diary")
mylist.append("Gaunt's ring")
mylist.append("Slytherin's locket")
mylist.append("Hufflepuff's cup")
mylist.append("Ravenclaw's diadem")
mylist.append("Nagini")
mylist.append("Harry Potter")
print(mylist[6] + "'s 'to destroy' list:")
for x in mylist:
    print(x)

#Arithmetic operators can be used with numbers +  - / *  (% for remainder, ** for power). + can concatenate strings, * can create repeating strings
a = 2.14
b = 1.00
print(a + b)
if a + b == 3.14:
    print("I'm hungry")

if 2.00 + 1.14 == 3.1399999999999997:
    print("WHYYY!!! Silly binary")

mushroom = "badger"
print(mushroom * 10)

#Loops are repeated steps that have iteration variables that change each time

#reserved words (cannot be used as variables/identifiers) in Python are:
reserved1 = "False, None, True, and, as, assert, break, class, if, def, del, elif, else, except"
reserved2 = "return, for, from, global, try, import, in, is, lambda, while, not, or, pass, raise"
reserved3 = "finally, continue, nonlocal, with, yield"
#built in functions should be treated as reserved words: print() input() type() float() int() 

#string constants use single or double quotes
string = "Mmmmm, stringy" + ' cheeeeese'

#variable names must start with a letter or underscore
good = "burger pancake_time grapes25"
bad = "32brownsauce smoked-fish Beer!"

#type() can be used to return the type of something
meow = "cats like?"
print(meow, type(meow))

#int() and float() can be used to convert numbers to a different type and strings that contain numbers
mole = "6.02214086"
print("Avogadro's constant is:", float(mole), "× 10^23 mol-1")

#int division in Python3 always produces a floating point result
good_Python3 = "Python 3 makes much more sense because Python 2 would return this as 0, DOH!"
print(99/100)

#we can instruct python to wait for a user input using the input() function
print('Enter your name:')
x = input()
print(x, "?! That's a strange name!")

#functions are stored code that take an input and produce an output
print("The most famous function of them all")

#def is used to start a function and stores indented code
def finding():
    print("Dory")
finding()

#loops have iteration variables (n) that change each time through a loop
n = 5
while n > 0:
    print(n)
    n = n - 1
print("BLAST OFF!!!")

#the break statement ends a loop and jumps to the statment following a loop
while True:
    line = input("There is no escape!> ")
    if line == "escape":
        break
    print(line)
print("Done!")

#the continue statement jumps to the top of the loop
#this is an indefinite loop
var = 10
while var > 0:              
   var = var -1
   if var == 4:
      continue
   print('Worthy number:', var)
print("4 is unworthy!")

#definite loops iterate through the members of a set using 'for'
for i in [5, 4, 3, 2, 1] :
    print(i)
print("Blast Off!")

#counting in a loop
belly = 0
for noodles in [3, 6, 9, 12] :
    belly = belly + 1
    print(noodles, belly)

#summing in a loop
belly = 0
for noodles in [3, 6, 9, 12] :
    belly = belly + noodles
    print(noodles, belly)

#finding the average in a loop
belly = 0
intestine = 0
for noodles in [3, 6, 9, 12] :
    belly = belly + 1
    intestine = intestine + noodles
    print(noodles, belly, intestine)
print(intestine / belly)

#filtering a loop
belly = 0
for noodles in [3, 6, 9, 120] :
    if noodles > 100 :
        print("WHAT A LOT OF NOODLES!")
    if noodles < 100 :
        print("EAT MORE NOODLES!")

#searching using a boolean value
found = False
chest = ["pants", "apple", "sword", "pillow", "gold"]
for treasure in chest :
    if treasure == "gold" :
        found = True, "aye, we're gonna be rich matey!"
        print(found)
#it is usually 'safer' to use == instead of 'is' unless using booleans

#characters inside a string can be accessed using an index specified in square brackets
happy = "feet"
penguin = happy[3]
print(penguin)

#looping through strings
lunch = "sandwich"
index = 0
while index < len(lunch) :
    letter = lunch[index]
    print(letter)
    index = index + 1

#there are several built in functions for strings, they do not modify the original string
glitch = "i'm so angry!"
crash = glitch.upper()
print(crash)

#to view available methods for strings:
print(dir("string"))

#the find() function can be used to return the position of a substring, if it does not exist it will return -1
dream = "team"
loser = dream.find("I")
print(loser)

#the replace function is similar to search and replace within word processors
baby = "hyper baby"
phew = baby.replace("hyper", "sleepy")
print(phew)

#whitespace can be removed using lstrip() rstrip() and strip()
hot = "    it's getting hot in here    "
very_hot = hot.strip()
print(very_hot)

#\n gives a new line, it is recognised as a single character

#open() is a function that opens a file

#quit() is a function that allows an error to occur and give control over the error message displayed

#searching a list
vegetables = ["courgette", "aubergine", "carrot", "cabbage"]
is_Veg = "tomato" in vegetables
print(is_Veg)

#.split() converts a string to a list, uses whitespace to split: spaces, new lines, tabs (if you don't use a delimiter)
words = 'this sentence will make you go bang, stop typing'
pieces = words.split()
parts = pieces[8].split('y')
n = parts[1]
print(n)

#collections are variables that can store multiple values in, like lists and dictionaries
#a list is a linear collection of values
#a dictionary is like a bag of values, each with its own label (key)

pond = dict()
birds = ['duck', 'duck', 'duck', 'goose']
for bird in birds :
    if bird not in pond :
        pond[bird] = 1 
    else : 
        pond[bird] = pond[bird] + 1
print(pond) 

#using the .get() method for counting in dictionaries
pond = dict()
birds = ['duck', 'duck', 'duck', 'goose']
for bird in birds :
    pond[bird] = pond.get(bird, 0) + 1
print(pond)

counts = dict()
print("Enter a nucleotide sequence:")
sequence = input(" ")
nucleotides = list(sequence)
for nucleotide in nucleotides :
    counts[nucleotide] = counts.get(nucleotide, 0) + 1
print("Counting nucleotides...", counts)

#you can get a list of keys, values or items (both) from a dictionary using list(), .keys(), .value(), .items()
#to loop through key value pairs you can use 2 iteration variables

#tuples are like lists but use brackets instead of square braces and you CANNOT change their contents
#they are more efficient than lists if you just want to store items
#you can put a tuple on the left hand side of an assignment statement
(pig, cow) = ('piglet', 'calf')
print(pig)
print(('pig', 'cow') < ('piglet', 'calf'))

#the sorted() function can sort a dictionary by its keys using the items() method

syllabus = open('combSci_GCSE_AQA.RTF', 'rb')
counts = dict()
for line in syllabus :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1
lst = list()
for key, val in counts.items() :
    newTup = (val, key)
    lst.append(newTup)
lst = sorted(lst, reverse=True)
for val, key in lst[:15] :
    print(key, val)

#a shorter way to sort
hungry = {'salami': 1, 'swiss cheese': 2, 'watermelon': 3, 'lollipop': 4, 'cake': 5}
print(sorted( [(om,nom) for om, nom in hungry.items()], reverse =True))

#regular expressions are powerful but cryptic
# ^ matches the start of a line
# * any number of times
# . matches any character
# \S matches any non-whitespace character
# \s matches any whitespace character

#re.search() returns a true or false re.findall() extracts a matching string

#example of building a simple web browser
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()

#a function within a class is called a method, as it only exists within the class
class procrastination:
    x = 0
    def time(self):
        self.x = self.x + 1
        print("Time wasted:", self.x, "mins")
zap = procrastination()
zap.time()
zap.time()
zap.time()

#__init__ is a constructor, __del___ is a destuctor
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name, self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()

class Fruit:
    count = 0
    name = ""
    def __init__(self, fruit):
        self.name = fruit
        print(self.name, "constructed")
    def fruitCount(self):
        self.count =  self.count + 1
        print(self.name, self.count)

a = Fruit("Apple")
b = Fruit("Banana")
c = Fruit("Currant")

a.fruitCount()
b.fruitCount()
c.fruitCount()
