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


# comprehensions => creating a new list from a list 
# square each index place and store it in squares 
squares = []
for i in range(1000):
    squares.append(i*i)
print(squares)

# comprehensions
squares_copy = [value for value in squares]

# conditional 
# only want large squares in this :
large_squares = [val for val in squares if val >= 10000]
print(large_squares)
