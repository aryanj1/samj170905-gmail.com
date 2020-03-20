n = input("string:")
m = n[::-1]
if n.lower() == m.lower():
    print("this is a palindrome")
else:
    print("not a palindrome")