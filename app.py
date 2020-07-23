while True:
    intent = input("Do you want to login or join? > ")

    if intent == "login":
        username = input("Name: ")
        password = input("Password: ")

        print(username)
        print(password)
        break
    elif intent == "join":
        username = input("Name: ")
        password = input("Password: ")

        print(username)
        print(password)
        break
    else:
        print("Action not supported")