from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_input = website_entry.get()
    password_input = password_entry.get()
    email_input = email_entry.get()


    if len(password_input) == 0 or len(website_input) == 0:
        messagebox.showinfo(title="Oops",
                               message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input,
                                       message=f"These are the details entered: \nEmail: {email_input}\npassword: {password_input} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website_input} | {email_input} | {password_input} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")


canva = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=image)
canva.grid(column=1, row = 0)


website = Label(text="Website:", bg="white")
website.grid(column=0, row=1)
email = Label(text="Email/Username:", bg="white")
email.grid(column=0, row=2)
password = Label(text="Password:", bg="white")
password.grid(column=0, row=3)

website_entry = Entry(width=35, highlightthickness=1, highlightbackground="grey", highlightcolor="grey", relief="solid", bd=0)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35, highlightthickness=1, highlightbackground="grey", highlightcolor="grey", relief="solid", bd=0)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "malakettabia00@gmail.com")
password_entry = Entry(width=17, highlightthickness=1, highlightbackground="grey", highlightcolor="grey", relief="solid", bd=0)
password_entry.grid(row=3, column=1)



generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()