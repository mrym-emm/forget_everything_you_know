# simple compound interest calculator --> A = P(1+ r/n)**t
# A is final amount
# P is initial principal alance
# r = interest rate
# t = num of time periods lapsed

# program will prompt user to insert value above 0

principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Please input principle amount: "))
#
#     if principle <=0:
#         print("principle cant be less than or equal to 0")
#
# while rate <= 0:
#     rate = float(input("Please input rate amount: "))
#
#     if rate <=0:
#         print("rate cant be less than or equal to 0")
#
# while time <= 0:
#     time = int(input("Please input time amount: "))
#
#     if time <=0:
#         print("time cant be less than or equal to 0")

# print(principle)
# print(rate)
# print(time)


# another way of writing it, so tht cn include 0

while True:
    principle = float(input("Please input principle amount: "))

    if principle <0:
        print("principle cant be less than 0")
    else:
        break # breaks out of loop

while True:
    rate = float(input("Please input rate amount: "))

    if rate <0:
        print("rate cant be less than or equal to 0")
    else:
        break # breaks out of loop

while True:
    time = int(input("Please input time amount: "))

    if time <0:
        print("time cant be less than or equal to 0")
    else:
        break # breaks out of loop
# total = principle * (1 + (rate/100))**time
total = principle * pow(1 + (rate/100),time)
print(f"Balance after {time} years: ${total:.2f}")
