import json
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# logic to generate random passsword
def generate_password():
    import random
    import string
    password_entry.delete(0, END)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# logic to save passwords in data.json
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD FUNCTION ------------------------------- #

# Función para buscar la contraseña en data.json
def search_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

# Configuración de la interfaz de usuario
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Entrada para sitio web, correo electrónico, contraseña y botón de agregar
website_label = Label(text="Website:", padx=5, pady=5)
website_label.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(row=1, column=2)
email_label = Label(text="Email/Username:", padx=5, pady=5)
email_label.grid(row=2, column=0)
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "alessandrodp2222@gmail.com")
password_label = Label(text="Password:", padx=5, pady=5)
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33)
add_button.grid(row=4, column=1, columnspan=2)

add_button.config(command=save_password)
password_button.config(command=generate_password)

window.mainloop()