# a number which divides by 1 and itself is called as prime number
# For a number to be called as a prime number, it must have only two positive factors. Now, for 1, the number of 
# positive divisors or factors is only one i.e. 1 itself. So, number one is not a prime number.
# 1 is neither prime or composite

n=int(input("Enter a number to check the given number is prime or not : "))
count = 0
if n>=2:
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            count = 1
            break
if count == 1:
    print("Given number is not a prime.")
else:
    print("Given number is a prime.")
