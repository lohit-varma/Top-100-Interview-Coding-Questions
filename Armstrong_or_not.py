"""Armstrong Numbers in Python
The Numbers that can be represented the sum of the digits raised to the power of the number of digits in the number are called Armstrong numbers.

Example
Input : 371
Output : It's an Armstrong Number
Explanation : 371 can also be represented as 3^3 + 7^3 + 1^3 therefore it's an Armstrong Number.

Given an integer input, the objective is to check whether or not the given input variable is an Armstrong number. 
In order to do so, we check whether the sum of the digits of each number to the power the length of the number is 
equal to the number itself or not. If the number is the same as the original, it’s an Armstrong number."""

n = input("Enter a number to check the given number is armstrong or not : ")
l = len(n)
s=0
for i in n:
    s=s + (int(i)**l)
print(s)