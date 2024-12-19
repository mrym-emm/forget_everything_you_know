import time
my_time = int(input("Enter time in seconds: "))

## counts till 2s before next line
# time.sleep(2)

for t in reversed(range(1, my_time+1)):
    second = t % 60
    minutes = int(t/60) % 60
    hours = int(t / 3600)


    print(f"{hours}:{minutes:02}:{second:02}")
    time.sleep(1)


print("Happy New Years!!")