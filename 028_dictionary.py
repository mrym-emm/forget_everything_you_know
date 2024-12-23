""""
dictionary = a collection of {key: value} pairs
            ordered and changeable, NO duplicates
"""

capitals = { "USA": "Washington",
             "India": "New Delhi",
            "China" : "Beijing",
             "Malaysia" : "KL"
             }

# # attributes
# print(dir(capitals))
# print(help(capitals))

print(capitals.get("Japan", "That capital doesnt exist"))

capitals.update({"Germany": "Berlin"})

print(capitals)

# update the existing values or add
capitals.update({"Germany": "Moscow"})

# remove keyvalue
capitals.pop("China")

# removes the latest key value inseretd
# capitals.popitem()

# clear item
# capitals.clear()

# get keys
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

# get values
values = capitals.values()
print(values)

for value in values:
    print(value)

# get items, a tuple of key,values
items = capitals.items()

for key, value in items:
    print(f"{key}: {value}")