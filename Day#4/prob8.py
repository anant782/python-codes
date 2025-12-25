email_data = input("Enter UR Email:")
extract = email_data.find("@")
username = email_data[:extract]
print(username)