
n1,n2 = map(int,input("Enter two numbers n1,n3 to print the prime numbers in given range of n1,n2 : ").split(","))
l=[]

for i in range(n1,n2+1):
    if i < 2:
        continue
    c=0
    for j in range(2,int(i/2)+1):
        if i%j == 0:
            c = 1
            break
    if c == 0:
        l.append(i)
print(l)