


# Goal: create a list of the squares of num_list
num_list = [10,20,30,40,50]

# simple example new list from other list, applying some function
squared_numbers = []
for num in num_list:
    squared_numbers.append(num*num)

print(squared_numbers)

squared_comprehension = [num*num for num in num_list]

squared_comprehension



# only operate for some subset of members - multiples of 20
squared_numbers = []
for num in num_list:
    if (num%20)==0:
        squared_numbers.append(num*num)
squared_numbers

squared_comprehension = [num*num for num in num_list if (num % 20) ==0]
squared_comprehension

