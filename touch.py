#The year can be evenly divided by 4, is a leap year The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400 then it is a leap year
def is_leap(year):
    leap = False
    if(year % 4 == 0 and year % 100 != 0): 
        leap = True
    if(year % 400 == 0):
        leap = True
    return leap
year = int(input())
print(is_leap(year))