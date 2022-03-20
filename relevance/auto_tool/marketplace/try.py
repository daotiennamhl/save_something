from dotenv import dotenv_values
config = dotenv_values(".env")
username = config["listuser"]
password = config["listpass"]
print(username.split(" "))
print(password.split(" "))