# Sets and Dictionaries

# inserting and removing from sets is fast, in is also fast in sets.

# Dictionaries are good for lookup


data = {
    109201: "Thing",
    298439: "Thing2"
}

print(data[109201])

# data is mutable

data[109201] = "THINGGG"

print(data[109201])

# can also add new keys

data[10010101] = "AAAAA"

print(data[10010101])

# Keys have to be immutable
# if duplicate key then it will access the latest entry, only 1 will be returned
# use del (thing) to delete
# can only check if keys are in dictionaries

# For loops in dictionaries

for x in data.keys(): # loops through the keys
    print(x)


# Combine dicts with {**d, **d2} or d | d2