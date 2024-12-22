# list made out of lists

                #0        #1        #2          #3
fruits =     ["apple", "orange", "banana", "coconut"]   #0

vegetables = ["celery", "carrots", "potatoes"]          #1

meats =      ["chicken", "fish", "turkey"]              #2

groceries = [fruits, vegetables,meats]

# print(groceries[0]) # will return the whole fruits list

# row col to access elemetnts
print(groceries[1][2])

# this will only iteratre the rows, but what if we want row, then col?
# for collection in groceries:
#     print(collection)

for collection in groceries:
    for food in collection:
        print(food, end =" ")
    print()

