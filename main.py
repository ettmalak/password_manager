from cProfile import label
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_input = website_entry.get()
    password_input = password_entry.get()
    email_input = email_entry.get()
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



pass_button = Button(text="Generate Password")
pass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()