import re
a=input("Enter your password:")
res=re.search("(?=.\d)(?=.[a-z])(?=.[!@#$%^&])(?=.*[A-Z]).{8,}",a)
if res:
    print("password is srong")
else:
    print("password is weak")
    
    
# import re

# def check_password_strength(password):
#     if len(password) < 8:
#         return "Password is too short. It should be at least 8 characters."
#     if not re.search(r"\d", password):
#         return "Password should contain at least one digit."
#     if not re.search(r"[A-Za-z]", password):
#         return "Password should contain at least one letter."
#     if not re.search(r"[A-Z]", password):
#         return "Password should contain at least one uppercase letter."
#     return "Password is strong!"