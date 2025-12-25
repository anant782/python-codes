Student = {
    "Shaurya": {
        "Hindi":46,
        "Math":65
    },
    "Jerry":{
        "Hindi":34,
        "Math":96       
    }}


print('''Total Student:
Shaurya
Jerry
''')
a = input("Choose One:")
output = Student[a]
total = output["Hindi"] + output["Math"]
print("Total Marks of", a, "Is", total)
print("Total Marks of",a,"Is",output)