# List of lists of birds
birds_list = [
    ["Magpie", "Cockatoo", "Hummingbird", "Ostrich", "Bald Eagle", 
     "Emperor Penguin", "Lyrebird", "Peacock", "Toucan", "Helmeted Hornbill"],
    [60, 70, 10, 270, 100, 129, 90, 105, 60, 120],
    [210, 900, 5, 136000, 26000, 112000, 5200, 28600, 4180, 2900], # weight
    [3.5, 45, 5, 40, 30, 20, 30, 15, 20, 30]
]


# Use a loop to print out the data about the fourth bird in `birds_list`.
# cycle through the attributes 
for attribute in birds_list:
    # find the 4th element in the attribute list 
    print(attribute[3])

# * Calculate the total weight (kg) of all the birds in the `birds_list` and print the result to three decimal places.
bird_weights = birds_list[2]
sum(birds_list[2])





# List of bird dictionaries
birds_dictionaries = [
    {
        "name": "Magpie",
        "size (cm)": 60,
        "weight (g)": 210,
        "lifespan": 3.5
    },
    {
        "name": "Cockatoo",
        "size (cm)": 70,
        "weight (g)": 900,
        "lifespan": 45
    },
    {
        "name": "Hummingbird",
        "size (cm)": 10,
        "weight (g)": 5,
        "lifespan": 5
    },
    {
        "name": "Ostrich",
        "size (cm)": 270,
        "weight (g)": 136000,
        "lifespan": 40
    },
    {
        "name": "Bald Eagle",
        "size (cm)": 100,
        "weight (g)": 26000,
        "lifespan": 30
    },
    {
        "name": "Emperor Penguin",
        "size (cm)": 129,
        "weight (g)": 112000,
        "lifespan": 20
    },
    {
        "name": "Lyrebird",
        "size (cm)": 90,
        "weight (g)": 5200,
        "lifespan": 30
    },
    {
        "name": "Peacock",
        "size (cm)": 105,
        "weight (g)": 28600,
        "lifespan": 15
    },
    {
        "name": "Toucan",
        "size (cm)": 60,
        "weight (g)": 4180,
        "lifespan": 20
    },
    {
        "name": "Helmeted Hornbill",
        "size (cm)": 120,
        "weight (g)": 2900,
        "lifespan": 30
    }
]



# Loop through the birds_dictionaries list
for bird in birds_dictionaries:
    # Print the names of the birds and their lifespans from the birds_dictionary
    print(bird['name'])
    print(bird['lifespan'])

    # Calculate and print out the size to weight ratio
    print(bird['size (cm)']/bird['weight (g)'])

better_bird_dict = {}
for bird in birds_dictionaries:
    better_bird_dict[bird['name']] = bird

for bird_name in better_bird_dict:
    better_bird_dict[bird_name]['size/weight ratio'] = better_bird_dict[bird_name]['size (cm)']/better_bird_dict[bird_name]['weight (g)']

from pprint import pprint

pprint(better_bird_dict)

pprint(better_bird_dict['Toucan'])

# dictionary maps weights-> bird names
weight_dictionary = {}
for bird_name in better_bird_dict.keys():
    # print(bird_name)
    size = better_bird_dict[bird_name]['size (cm)']
    weight = better_bird_dict[bird_name]['weight (g)']
    weight_ratio = size/weight

    # use the weight_ratio as the key in our weight dictionary
    # have it point to the bird_name
    weight_dictionary[weight_ratio] = bird_name


# Highest size to weight ratio: 


# Lowest size to weight ratio: 
lightest_weight = min(weight_dictionary.keys())
print(lightest_weight)
lightest_bird = weight_dictionary[lightest_weight]
print(lightest_bird)



# birds_list - comprehensions
sizes = []
for bird in better_bird_dict:
    sizes.append(better_bird_dict[bird]['size (cm)'])

sizes = [better_bird_dict[bird]['size (cm)'] for bird in better_bird_dict]


ratios = {better_bird_dict[bird]['size/weight ratio']:bird for bird in better_bird_dict}
ratios

names = tuple((name.lower() for name in better_bird_dict.keys()))
print(names)