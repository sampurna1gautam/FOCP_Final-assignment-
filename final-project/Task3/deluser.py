
def userdelete(entered_username, entered_password):
    with open("passwd.txt", "r+") as file:
        content_list = []
        user_list = []
        password_list = []
        for content in file:
            content_list.append(content)
            username, fullname, password = content.strip().split(":")
            user_list.append(username)
            password_list.append(password)

        if (entered_username in user_list):
            userindex = user_list.index(entered_username)
            if (entered_password == password_list[userindex]):
                content_list.pop(userindex)
                file.seek(0)
                file.truncate()
                file.writelines(content_list)
            else:
                print("Credential Error!")   
        else:
            print("Username does not exist!")


def main():
    entered_username = input("Username to delete: ")
    entered_password = input("Enter password: ")

    try:
        userdelete(entered_username, entered_password)
    except ValueError as e:
        print("Error!", e)

if __name__ == "__main__":
    main()