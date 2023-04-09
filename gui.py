import os
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END
from tkinter import messagebox
import functions
import pyperclip


class GUI:
    def __init__(self, username):
        self.win = Tk()
        self.win.config(padx=20, pady=20)

        self.canvas = Canvas()
        self.canvas.configure(width=200, height=200)
        self.logo_img = PhotoImage(file=f'{os.path.dirname(__file__)}\\logo.png')
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        self.website_label = Label(text="Website:")
        self.website_label.grid(row=1, column=0)
        self.website_input = Entry(width=33)
        self.website_input.focus()
        self.website_input.grid(row=1, column=1)

        self.username_label = Label()
        self.username_label.config(text="Email/Username:")
        self.username_label.grid(row=2, column=0)
        self.username_input = Entry(width=51)
        self.username_input.insert(0, username)
        self.username_input.grid(row=2, column=1, columnspan=2)

        self.password_label = Label(text="Password:")
        self.password_label.grid(row=3, column=0)
        self.password_input = Entry(width=33)
        self.make_new_password()
        self.password_input.grid(row=3, column=1)
        self.password_button = Button(width=14, text="Generate Password", command=self.make_new_password)
        self.password_button.grid(row=3, column=2)

        self.add_button = Button()
        self.add_button.config(width=43, text="Add", command=self.save_password)
        self.add_button.grid(row=4, column=1, columnspan=2)

        self.search_button = Button()
        self.search_button.config(width=14, text="Search", command=self.find_password)
        self.search_button.grid(row=1, column=2)

    def make_new_password(self):
        password = functions.make_new_password()
        self.password_input.delete(0, END)
        self.password_input.insert(0, password)
        pyperclip.copy(password)

    def save_password(self):
        credentials = self.website_input.get(), self.username_input.get(), self.password_input.get()

        try:
            proceed = functions.save_password(*credentials)
        except ValueError as exc:
            messagebox.showinfo('Oops', exc)
        else:
            is_ok = messagebox.askokcancel(title=credentials[0],
                                           message=f"These are the details entered:\n\n"
                                                   f"Username: {credentials[1]}\n"
                                                   f"Password: {credentials[2]}\n\n"
                                                   f"Is it ok to save?")
            if is_ok:
                proceed()
                self.website_input.delete(0, END)
                self.make_new_password()

    def find_password(self):
        website = self.website_input.get()

        try:
            response = functions.find_password(website)
        except ValueError as exc:
            messagebox.showinfo('Oops', exc)
        else:
            messagebox.showinfo(website, response)

    def main(self):
        self.win.mainloop()


if __name__ == '__main__':
    from config import DEFAULT_USERNAME
    GUI(DEFAULT_USERNAME).main()
