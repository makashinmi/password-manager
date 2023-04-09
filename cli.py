import functions
import pyperclip


class CLI:
    def __init__(self):
        pass

    def make_new_password(self):
        password = functions.make_new_password()
        pyperclip.copy(password)
        return password

    def save_password(self, website, username, password):
        credentials = website, username , password

        try:
            functions.save_password(*credentials)()
        except ValueError as exc:
            print(exc)
        else:
            return f'Password was copied to clipboard!'

    def find_password(self, website):
        try:
            response = functions.find_password(website)
        except ValueError as exc:
            print(exc)
        else:
            return response

    def main(self):
        command = input('1. Generate a new password\n'
                        '2. Search for a password\n'
                        '3. Exit\n\n'
                        'Enter command number [1-3]: ')

        match command:
            case '1':
                website = input('Website: ')
                username = input('Username (Enter to use default): ')
                password = self.make_new_password()
                print('Password:', password)
                response = self.save_password(website, username, password)
                print(response)
            case '2':
                website = input('Website to look up a password for: ')
                result = self.find_password(website)
                print(result)
            case '3':
                pass
            case _:
                self.main()

    def quick(self, website, username):
        password = self.make_new_password()
        return self.save_password(website, username, password)
