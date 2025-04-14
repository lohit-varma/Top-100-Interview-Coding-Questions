def even_or_odd(a):
    return "even" if a%2 == 0 else "odd"
num=int(input("Enter a number to check whether the number is Even or Odd : "))
print(even_or_odd(num))