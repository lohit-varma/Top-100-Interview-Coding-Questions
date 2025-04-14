def sum_of_numbers_in_a_given_range(a,b):
    return sum(range(a,b+1))

num1,num2 = map(int,input("Enter two numbers to find the sum of numbers in a given range : ").split(","))
print(sum_of_numbers_in_a_given_range(num1,num2))