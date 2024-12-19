# for loops = execute a block of code a FIXED number of times
# You can iterate over a range, string, sequence etc

for x in (range(1,11,2)):
    print(x)

print("Happy New Year!")

credit_card = "1234-23532-2325-2"

for x in credit_card:
    print(x)

for x in range(1,21):
    if x ==13:
        continue #will keep on counting
        # break - will escape loop
    else:
        print(x)

for x in range(1,21):
    if x ==13:
        break
    else:
        print(x)