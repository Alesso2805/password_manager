from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# logic to generate random passsword
def generate_password():
    import random
    import string
    password_entry.delete(0, END)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# logic to save passwords
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            passwords.insert(END, f"{website} | {email} | {password}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Entry for website, email, password and button of Add
website_label = Label(text="Website:", padx=5, pady=5)
website_label.grid(row=1, column=0)
website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2)
email_label = Label(text="Email/Username:", padx=5, pady=5)
email_label.grid(row=2, column=0)
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password:", padx=5, pady=5)
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33)
add_button.grid(row=4, column=1, columnspan=2)

# List of saved passwords
passwords_label = Label(text="Saved Passwords")
passwords_label.grid(row=5, column=1)
passwords = Listbox(width=45)
passwords.grid(row=6, column=1, columnspan=2)
scrollbar = Scrollbar()
scrollbar.grid(row=6, column=3)
passwords.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=passwords.yview)

add_button.config(command=save_password)

password_button.config(command=generate_password)


window.mainloop()