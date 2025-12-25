Name = input("Enter UR name:")
Age = input("Enter Ur AGe:")

letter = '''Hello <Name>,\nYou are <age> years old.'''
replacement = letter.replace("Name", Name).replace("age",Age)
print(replacement)