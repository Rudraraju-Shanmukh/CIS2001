def ask_for_users_name():
    name = input("What is your name?")
    return name


def print_greeting():
    print("Hello class!")
    print("How is your day?")


print_greeting()
users_name = ask_for_users_name()

print(f"Hi there {users_name}")

