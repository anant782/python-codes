n1 = int(input("Enter Number:"))
n2 = int(input("Enter Number:"))
n3 = int(input("Enter Number:"))
n4 = int(input("Enter Number:"))

large = n1
if n2>large:
    large=n2
if n3>large:
    large=n3
if n4>large:
    large = n4
print(f"Largest Is {n4}")
