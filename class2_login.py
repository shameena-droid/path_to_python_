"""As a user,
I want to log in to a system using my credentials,
so that I can access secure features only if I am authorized"""
"""Hints:
- user logical operators
- Data type selection
- Also checks user role for authorization"""
#create a dict containing list of several usres ,usernames and  their passwords
#read the user login details- username and password-theyre case sensitive
#iterate the list of users and check whether the details match with input 

import getpass #from chatgpt
user_db = {
    "users" : [ {"id": 101, "name": "Abuharis", "username": "admin","password":"abuharis","role":"admin"},
                {"id":102,"name":"Batool","username":"batool","password":"batool","role":"user"},
                {"id":103,"name":"Mariyam","username":"mariyam","password":"mariyam","role":"user"} ]
    }
#print(user_db.get("users"))
#define a function to login
def ulogin(data,uname,pswd):
    for i in data["users"]:
        if i.get("username")==uname and i.get("password")==pswd:
            if i.get("role")=="admin":
                print("welcome, Admin!")
            #else:
               # print(f"welcome,{i.get("name")}!PRINT OF ELSE")
            return f"welcome {i.get("name")}!"
    return f"invalid username or password"
#lets read the data
username=input("Enter your username :")
password=getpass.getpass("Enter your password: ")
#calling function
print(ulogin(user_db,username,password))