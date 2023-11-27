# abby donoghue python notes 

########################################################
# variables 
x = 10 
print(x)
y = 11.5
x = "this is a string"
print(x)
########################################################

# math operators
x = 100
y = 10 
result = x/y
result = int(x/y)
print(result)

# built in functions
min_val = min(10,2)
print(min_val)
raised = pow(2,4)
raised = 2**4

########################################################
x = -1
if x < 0:
    print(" x is negative")
    x +=1
print("outside the if")

count = 0
while count < 10:
    count +=1
    print(count)

alist = [1,2,3,4,5]
for value in alist:
    print(value)

for i in range(len(alist)):
    print("i is: ", i, "and value is: ", alist[i])

for i, val, in enumerate(alist):
    print(i, val)


def say_hello(name = "friend"):
    print("hello", name)
say_hello()

########################################################

alist = [10,20,30,40,50]
# add values
alist.append(5) # could put a list instead of one val ([1,2,3,])
alist.append(6)
alist.append(7)
print(alist)

# remove the value at index place 1
# if you dont specify which index it will pop the last automatically 
alist.pop(1)   # could also use .remove 
print(alist)

# add values between 6 and 30 from alist to empty 
empty=[]
for value in alist:
    if value >= 6 and value <= 30:
       empty.append(value)
print(empty)
empty.sort()
print(empty)

empty = []
# a list of 10 0's 
empty = [0] * 10
# adding a 10 in for index 8 
empty[8] = 10
print(empty)

dog = "dog"
dogs = dog * 3
print(dogs)

########################################################
# comprehensions => creating a new list from a list 
# square each index place and store it in squares 
squares = []
for i in range(1000):
    squares.append(i*i)
print(squares)

# comprehensions
squares_copy = [value for value in squares]
# or 
for value in squares:
    squares_copy.append(value)

# conditional 
# only want large squares in this :
large_squares = [val for val in squares if val >= 10000]
print(large_squares)

# comprehension of squares
squares = [i*i for i in range(1000)]
print(squares)
########################################################
# sets 
# sets cant have duplicate values and are unordered
aset = {1,2,3}
print(aset)

dups = [1,2,2,2,2,3,3,4,5]
# easy way to remove duplicate values is to create a set with it 
no_dups = set(dups)
print(no_dups)

# if you want a list can convert it back to og 
do_dups = list(dups)
print(do_dups)
########################################################

# dictionaries 
# collection of data that has a key and a value 
# useful to look up values, count occurances, store a record of related values 
# keys must be unique no duplicates 

cities = {}
cities[19333]= "Devon"
        #key
city = cities[19333]
              # key
fav_foods = {"kathleen" : "pizza", "abby" : "hamburger", "caroline" : "chicken tenders", "dominic" : "sushi"}
caroline_ff = fav_foods["caroline"]
print(caroline_ff)  # this will print out chicken tenders

# iterate throiuogh keys
for key in fav_foods:
    print(key, "favorite food is ", fav_foods[key]) # makes a list of each fav food for each person 
# prints out the values as well (same thing)
for key, value in fav_foods.items():
    print(key, "fav food is ", value)

if "kim" in fav_foods:
    kim = fav_foods["kim"]
else: 
    fav_foods["kim"] = "cereal"
print(fav_foods)

########################################################

# classes

