import json


def filter_users_by_name(name):
    """Function to filter by user name, print the user data as dictionary"""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(age):
    """Function to filter by age, print the user data as dictionary"""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_by_email(email):
    """Function to filter by email, print the user data as dictionary"""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


def main():
    """The main function to filter user dada from json file.
    Filter function by name, age or email"""

    filter_option = input("What would you like to filter by ('name', 'age' or 'email'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()