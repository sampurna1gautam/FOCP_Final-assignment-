


def useradd(new_username, new_fullname, new_password):
    with open ("passwd.txt", "r+") as file:
        user_list = []
        for content in file:
            each_username = content.strip().split(":")[0]
            user_list.append(each_username)

        if new_username in user_list:
            print("Cannot add. Most likely username already exists.")
        else:
            file.write(f"\n{new_username}:{new_fullname}:{new_password}")
            print("User added successfully!")

        

def main():
    new_username = input("Enter your username: ")
    new_fullname = input("Enter your full name: ")
    new_password = input("Enter your password: ")

    try:
        useradd(new_username, new_fullname, new_password)
    except ValueError as e:
        print("Error!", e)

if __name__ == "__main__":
    main()