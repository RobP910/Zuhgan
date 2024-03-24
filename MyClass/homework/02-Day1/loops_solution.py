# Loop through a range of numbers (0 through 4)
for x in range(5):
    print(x)

print("-" * 40)

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not
# including, 7)
for x in range(2, 7):
    print(x)

print("-" * 40)

# Loop through a range of numbers (0 through 4) without using the value in the
# range
num_of_people = 1
for _ in ["joe","jaime","gavin"]:
    # Add 2 to the value of y
    num_of_people += 1
    print(num_of_people)

# using a for loop to create 
line = ''
for _ in range(0,40):
    line += '-'

print(line)

# print("-" * 40)

# Iterate through letters in a string
word = "Peace"
for letter in word:
    print(letter)

print("-" * 40)

# Iterate through a list
zoo = ["cow", "dog", "bee", "zebra"]
for animal in zoo:
    print(animal.upper())

print("-" * 40)

# Make changes to each item in a list
numbers = [9, 6, 4, 9]
size = len(numbers)
size
for i in range(size):
    # Add 1 to the list item
    numbers[i] += 1
    print(numbers[i])

print(numbers)

print("-" * 40)

# Loop while a condition is being met
run = "y"

# run.lower() means the condition will be met if run = "y" or run = "Y"
while run.lower() == "y":
    print("Hi!")
    run = input("To run again. Enter 'y': ")

value = 0
while value<10:
    print(f'Value is less than 10. Value is: {value}')
    value += 1

# initialize empty data 
data = []
# while response contains data 
    # add new data to my list 
    # request more data 

# While loop with a Boolean variable
keep_looping = True

while keep_looping:
    print("Hi!")
    keep_looping = bool(input("Press enter to exit and anything else to continue. "))
