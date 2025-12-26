marks = int(input("Enter Ur Marks:"))
f = marks<33
p = marks>=33
if marks>=101:
    print("Invalid Marks")
elif p:
    print("Result: Pass")
elif f:
    print("Result: Fail")