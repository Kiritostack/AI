password="pyth123"
attempt=3
while attempt>0:
    user_input=input("Enter the password:")
    if user_input==password:
        print("✅ Access granted")
        break
    else:
        attempt=attempt-1
        print(f"❌ Wrong,you have {attempt} left.")

if attempt==0:
    print("🔒 Account locked") 
       
