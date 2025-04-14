def pos_or_neg(a):
    return "zero" if a == 0 else ("Positive" if a%2 == 0 else "Negative")

num = int(input("Enter a number to check whether the number is +ve or -ve : "))
print(pos_or_neg(num))