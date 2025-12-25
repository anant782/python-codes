a = input("Enter Ur Name")
Date = "12/20/25"

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("Name", a,).replace("Date",Date))