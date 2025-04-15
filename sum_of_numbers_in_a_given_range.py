# sum of N natural Numbers or sum of first N natural Numbers in a given range formula is (n*(n+1))/2
# sum of numbers in a given range of a,b is (b*(b+1))/2 - (a*(a+1))/2 + a
def sum_of_numbers_in_a_given_range(a,b):
    return sum(range(a,b+1))

num1,num2 = map(int,input("Enter two numbers to find the sum of numbers in a given range : ").split(","))
print(sum_of_numbers_in_a_given_range(num1,num2))