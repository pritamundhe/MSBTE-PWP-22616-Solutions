dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary
new_dict = {}

# Concatenate dictionaries using update() method
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

# Print the new dictionary
print("Concatenated Dictionary:", new_dict)

'''
op:-
Concatenated Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
