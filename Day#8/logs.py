username = input("Enter UserName:")
em = input("Enter Ur Email:")
pas = input("Enter Ur password:")
pasl = len(pas)


if(em == "" or pas == ""):
    print("Field Can't Be Empty")
elif (pasl<=8):
    print("!!! Please Enter Strong Password !!!")
elif (".com" not in em):
    print("Invalid Emai l!!")
else:
    print("Login Success!!!")
