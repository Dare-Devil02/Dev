#username validation
#username is not more than 12 characters
#username must not contain spaces
#username must not contain digits
username=input("Enter the username :")
if len(username)<=12:
    if(username.isalpha()):
        print("Username Validated")
    else:
        print("Username contains either spaces or digits")
else:
    print("Username longer than 12 characters")