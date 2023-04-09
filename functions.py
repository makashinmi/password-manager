from random import choice, randint, shuffle
import pyperclip
import json

from config import OUTPUT_FILENAME


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def make_new_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(12, 14))]
    password_list += [choice(numbers) for _ in range(randint(4, 6))]
    password_list += [choice(symbols) for _ in range(randint(4, 6))]
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(website, username, password):
    new_data = {
        website: {
            "Username": username,
            "Password": password
        }
    }

    if website == "" or password == "":
        raise ValueError("Please, don't leave any fields empty!")
    else:
        def proceed():
            try:
                with open(OUTPUT_FILENAME, "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(OUTPUT_FILENAME, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            except json.JSONDecodeError:
                with open(OUTPUT_FILENAME, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open(OUTPUT_FILENAME, "w") as data_file:
                    json.dump(data, data_file, indent=4)
        return proceed


# ---------------------------- SEARCHING FOR A PASSWORD ------------------------------- #
def find_password(website):
    if website:
        try:
            with open(OUTPUT_FILENAME, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            raise ValueError("No Data File Found")
        except json.JSONDecodeError:
            raise ValueError("It appears that file exists, but is empty.\n\n"
                             "Try simply deleting it or adding new data.")
        else:
            if website in data:
                username = data[website]['Username']
                password = data[website]['Password']
                response = f"Username: {username}\nPassword: {password}\n\nPassword was copied to clipboard!"
                pyperclip.copy(password)
            else:
                response = "No details for the website exist"

            return response
