# user input 

try:
    # indent anything that could throw an error
    num = int(input("enter a number "))
    num += 5
    print(num)
except:
    print("you did not enter a valid number")


# reading from file
with open("movies.txt") as file:
    for line in file:
        print(line.strip()) # get rid of the ln


# heights: firstname lastname age 
# split looks for a space in the string to split it 
with open("heights.txt")as file:
    for line in file:
        stripped_line = line.strip()
        tokens = stripped_line.split()
        #print(tokens)
        print(tokens[0], tokens[1], "is" ,int(tokens[2]), "inches")
