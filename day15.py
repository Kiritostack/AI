User_database={
    "Kunal Kumar":"Kunal@99",
    "Ayu":"IJK32"
}
user_name=input("Enter username:")
password=input("Enter the password:")
if user_name in User_database:
    if password == User_database[user_name]:
        print("login successfull")
    else:
        print("password incorrect")
else:
    print("user not found")        