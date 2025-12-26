s1 = "Make a lot of money"
s2 = "buy now"
s3 = "subscribe this"

print(f"Availble Spams:")
print(f"{s1}\n{s2}\n{s3}")
user_input = input("Enter Any Spams:")

if (user_input is s1 or s2 or s3):
    print(f"Spam Detected \"{user_input}\"")
else:
    print("Spam Not Detected")