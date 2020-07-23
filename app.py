while True:
    access_to_site = input("Do you want to login or join? > ")

    if access_to_site == "login":
        username = input("Name: ")
        password = input("Password: ")

        print(username)
        print(password)
        break
    elif access_to_site == "join":
        username = input("Name: ")
        password = input("Password: ")

        print(username)
        print(password)
        break
    else:
        print("Action not supported")