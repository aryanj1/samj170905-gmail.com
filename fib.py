n= int(input("Enter a number: "))  
a = 0
b = 1

if n <= 0:
    print("no,invalid")
elif n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        z = a + b
        a = b
        b = z
        print(z)

 
  
