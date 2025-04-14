def greatest_of_two_numbers(a,b):
    return a if a>b else b

num1,num2 = map(int,input("Enter two numbers to check the greatest of two numbers : ").split(","))
print(greatest_of_two_numbers(num1,num2))