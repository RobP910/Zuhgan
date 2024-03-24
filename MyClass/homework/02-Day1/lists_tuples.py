# Create a variable and set it as a list
joes_list = ["Joe", 40, "Salt Lake City", True]

print(joes_list)

## Methods for accessing parts of a list
# Slides ->
# Return the value of a list at a given index
joes_list[2]
joes_list[-1] # reference from the end
joes_list[-2]

joes_list[1:3]

num_list = list(range(15))
num_list

num_list[3:9]
num_list[9:12]
num_list[0:10:2]

num_list[0:14:9]

len(num_list)
num_list[0:len(num_list)]

numbers_to_5 = list(range(1,6))
print(numbers_to_5)

num_list[3:]

# Return a list slice [index_start:index_end]


## Methods for modifying a list
# Slides ->
# Add an element onto the end of a list
joes_list
joes_list.append(11.0)

print(joes_list)

# Return the index of the first object with a matching value
joes_list.append('Virgin Islands')
print(joes_list)
location_index = joes_list.index('Virgin Islands')
print(location_index)

# Change a specified element within a list at the given index
joes_list[location_index] = 'Salt Lake City'
joes_list

# Remove a specified object from a list
joes_list.remove(11.0)
print(joes_list)

# Remove the object at the index specified
joes_list.pop(location_index)
joes_list

eleven_list =  [11,1,11,12]
eleven_list.remove(11)
print(eleven_list)

joes_list
joes_list = joes_list[0:2]+["hat"]+joes_list[2:]
joes_list

# Functions for accessing information about a list
# Define a list named scores
scores = [92, 87, 68, 75, 96]

# Return the max (or highest value) item in a list
max(scores)

# Return the min (or lowest) item in a list
min(scores)

# Return the sum of the items in a list
sum(scores)

# Return the length of the list
len(scores)

# Use sum and len to calculate average
avg_score = sum(scores)/len(scores)
print(avg_score)

# Create a tuple, a sequence of immutable Python objects that cannot be changed
jaimes_tuple = ('Jaime', 35, "Herriman, UT")
jaimes_tuple[0] = 'Jason'

# Information functions also work on tuples, provided they contain valid data
# types
jaimes_tuple[0:2]

jaimes_tuple.append("blue shirt")