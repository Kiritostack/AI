user = {
    "username": "admin",
    "password": "1234"
}

print(user.get("username"))
print(user.get("email"))

print(user.get("email", "Email Not Found"))