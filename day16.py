user_data={
    "admin":"kunal99"
}
def login(user,password):
    if user in user_data and user_data[user]==password:
     print(f"Welcome {user}")
    else:
       print("Error")

user=input("enter your name:")
password=input("enter password:")
login(user,password)
       



