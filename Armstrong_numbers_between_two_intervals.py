n1,n2 = map(int,input("Enter the 2 numbers to find the armstrong numbers in the given range : ").split(","))
li=[]
for n in range(n1,n2+1):
    l = len(str(n))
    s=0
    for i in str(n):
        s=s + (int(i)**l)
    if s == n:
        li.append(n)
print(li)