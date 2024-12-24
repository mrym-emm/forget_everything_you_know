""""
Match case statement (switch): An alternative to using many 'elif' statments
                                Execute some if a value matches a 'case'
                                Benefits: cleaner and syntax more readeable
                                In python 3.10
"""

def day_of_week(day):

    match day:
        case 1:
            return "It is sunday"
        case 2:
            return "It is monday"

        case 3:
            return "It is tuesday"

        # this is wildcard, very similar to 'else'
        case _:
            return "It is not a valid day"

def is_weekend(day):

    match day:
        case "Sat" | "Sun":
            return True
        case "Mon" | "Tues" | "Wed" | "Thurs" | "Fri":
            return False

        # this is wildcard, very similar to 'else'
        case _:
            return False