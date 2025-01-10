import datetime

# year, month, dd
date = datetime.date(2025, 1,2)

today = datetime.date.today()
time = datetime.time(12,30,0)
now = datetime.datetime.now()

# formatting
now = now.strftime("%H:%M:%S %m-%d-%Y")

print(date)
print(today)
print(time)
print(now)

target_datetime =datetime.datetime(2020, 7, 4, 9 , 2)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("target date has NOT passed")