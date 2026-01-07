import json


def filter_users_by_name(name):
    """
    Filtering the users by name.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """
    Filtering the users by age.
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    if age < 0:
        print("Age cannot be less than 0!")
    else:
        filtered_users = [user for user in users if user["age"] == age]

        for user in filtered_users:
            print(user)


def filter_users_by_email(email):
    """
    Filtering the users by email.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    """ 
    Main function
    """
    filter_option = input("What would you like to filter by? "
                          "(Currently, only 'name', 'age', 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        while True:
            try:
                age_to_search = int(input("Enter an age to filter users: ").strip())
                filter_users_by_age(age_to_search)
                break
            except ValueError:
                print("Please use a valid integer number as age!")
                continue
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")