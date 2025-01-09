"""
Exception = an event that interrupts the flow of a program
            (zero divisin error, typeerror,valueerror)
            1.try, 2.except, 3. finally
"""


try:
    number = int(input("Enter a number"))
    print(1/number)
except ZeroDivisionError:
    print("You cant dicide by zero!")
except ValueError:
    print("You cant dicide by zero!")

except Exception: # this is bad practice standalone, as we dont know what went wrong
    print("Something went wrong")

# finally will always execute regardless of the exception
finally:
    print("Do some cleanup here")