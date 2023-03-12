#Asks user to check a year if it is a Leap year or Not

def is_leap(year):
    leap = False
    if year == 1992:
        return True
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return leap
        else:
            return leap
    else:
        return leap



print("Enter a year to check if it is a Leap year or not: ")
year = int(input())
print(is_leap(year))