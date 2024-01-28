

def userlogin(entered_username, entered_password):
    with open("passwd.txt", "r") as file:
        password_list = []
        user_list = []
        for content in file:
            username, fullname, password = content.strip().split(":")
            user_list.append(username)
            password_list.append(password)

        if (entered_username in user_list):
            userindex = user_list.index(entered_username)
            if (entered_password == password_list[userindex]):
                print("Logged in")
            else:
                print("Credential Error!")   
        else:
            print("Username does not exist!")
        



def main():
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    try:
        userlogin(entered_username, entered_password)
    except ValueError as e:
        print("Error", e)

if __name__ == "__main__":
    main()
    