# Dictionary full of info
stored_info = {"Name": "Rob",
               "Age": 59,
               "Hobbies": ["Motorcycle riding",
                          "RC airplanes",
                          "Gaming"],
                "wake_up": {
                    "Monday": 5,
                    "Saturday": 9,
                    "Sunday": 10
                    }
}

# Print out results stored in the dictionary
print(f"I am {stored_info['Name']} and I'm {stored_info['Age']} years old.")
print(f"My favorite hobbies is {stored_info['Hobbies'][0]}")
print(f"I'm usually up for work by {stored_info['wake_up']["Monday"]}")

# Use a loop to print out the key-value pairs in the dictionary
for item in about_me.items():

    print(f'My {item[0]} is {item[1]}')


for key,value in about_me.items():

    print(f'My {key} is {value}')

# Use a loop to print out the keys of the wake-up dictionary


# Use a loop to print out the values of the wake-up dictionary
