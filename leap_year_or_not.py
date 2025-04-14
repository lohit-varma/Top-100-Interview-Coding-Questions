def leap_year_or_not(a):
    return "Leap Year" if a%4 == 0 and a%100 != 0 or a%400 ==0 else "Not a Leay Year"

num=int(input("Enter a year to check whether the year is leap year or not : "))
print(leap_year_or_not(num))