def is_palindrome(a):
    if a == a[::-1]:
        return True
    return False
n=input("Enter a number to check whether the number id palindrome or not : ")
print(is_palindrome(n))