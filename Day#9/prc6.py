print("Grade Calculator")
M = int(input("Enter Ur Marks:"))

g1 = M>=90
g2 = M>=80
g3 = M>=70
g4 = M>=60
g5 = M>=50
g6 = M<50

if (g1):
    print(f"Your Grade Is \"Ex\"")
elif(g2):
    print("Your Grade Is \"B\"")
elif(g3):
    print("Your Grade Is \"C\"")
elif(g4):
    print("Your Grade Is \"D\"")
elif(g5):
    print("Your Grade Is \"E\"")
elif(g6):
    print("Your Grade Is (Padai krle)")