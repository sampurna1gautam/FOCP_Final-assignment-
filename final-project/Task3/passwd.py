
def passwordchange(entered_username, entered_password, new_password):
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

                line = content_list[userindex].strip().split(":")
                line[2] = new_password
                newline = ":".join(line)
                content_list[userindex] = newline
                file.seek(0)
                file.truncate()
                file.writelines(content_list)
                print("Password updated successfully!")
        else:
            print("Username does not exist!")




def main():
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    new_password = input("Enter new password: ")

    try:
        passwordchange(entered_username, entered_password, new_password)
    except ValueError as e:
        print("Error!", e)

if __name__ == "__main__":
    main()