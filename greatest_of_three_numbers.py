def greatest_of_three_numbers(a,b,c):
    return a if a>b and a>c else ( b if b>a and b>c else c)

num1,num2,num3 = map(int,input("Enter 3 numbers to print the greatest of 3 numbers : ").split(","))
print(greatest_of_three_numbers(num1,num2,num3))