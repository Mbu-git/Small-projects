from tkinter import *
import csv
from tkinter import messagebox
import random
from tkinter.messagebox import showinfo

import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    new_chars = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    new_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = new_letters + new_chars + new_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)
    pyperclip.paste()
    messagebox.showinfo(title="Password generated", message= f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().title()
    email = email_input.get().title()
    password = password_input.get().title()
    new_data ={
        website:{
            "email": email,
            "password": password,
        }
    }

    if password == "" or email == "":
        messagebox.showerror(title="Oops..", message="Please fill in all fields before adding.")
        return
    else:
        try:
            with open("password_data.json", mode="r") as p_data:
                #Reading old data
                data = json.load(p_data)
        except FileNotFoundError:
            #File doesn't exist, so create file with new data
            with open("password_data.json", mode="w") as p_data:
                # Saving update data
                json.dump(new_data, p_data, indent=4)
        else:
            #File exists:
            # Updating old data
            data.update(new_data)
            with open("password_data.json", mode="w") as p_data:
                #Saving update data
                json.dump(data, p_data, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    website = website_input.get().title()
    try:
        with open("password_data.json", mode="r") as p_data:
            data = json.load(p_data)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="No data file found.")
    else:
        if website in data:
            email_found = data[website]["email"]
            password_found = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email ={email_found}\n Password: {password_found}")
            password_input.delete(0,END)
            password_input.insert(0,data[website]["password"])
            email_input.delete(0,END)
            email_input.insert(0,data[website]["email"])
        else:
            messagebox.showerror(title="Key Error", message=f"No data found for {website}.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx= 50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100, image=logo_img, anchor= "center")
canvas.grid(column =1, row= 0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Inputs
website_input = Entry(width=35)
website_input.grid(column=1,row=1,columnspan=2,sticky="we")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row= 2, columnspan=2, sticky="we")
email_input.insert(0, "example@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="we")

#Buttons
gen_pass = Button(text="Generate Password", command= password_generator)
gen_pass.grid(column=2,row=3, sticky="w")

add_button = Button(text="Add",width=36, command= save_password)
add_button.grid(column=1,row=4, columnspan=2,sticky="we")

search_button = Button(text="Search",command=search_data)
search_button.grid(column= 2, row=1, sticky="we")


window.mainloop()