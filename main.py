from tkinter import messagebox
import json
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def PASSWORD_GENERATOR():
    

    letters= ("a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")

    letter=letters.split(" ")

    numb= ["1", "2", "3", "4", "5", "6", "7" "8", "9", "0"]
    char= ["~","`","!","@","#","$","%","^", "&", "*","(",")","_","+","=",",","<",".",">","/","?",":"," ", ";","'",'"',"[","{","]","}"]

    letter_num=4

    num=3

    char_num=7


    my_password=[" "]
    passwordd=""
    for my_letter in range(1, letter_num+1):
        my_password.append(random.choice(letter))
        
    for my_char in range(1, char_num+1):
        my_password.append(random.choice(char))
        
    for my_num in range(1, num+1):
        my_password.append(random.choice(numb))
        

    random.shuffle(my_password)
    password=passwordd.join(my_password)
    password_entry.insert(0, password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def FIND_PASSWORD():
    web=website_entry.get().title()

    try:
        with open("data.json", "r") as file:
            dat=json.load(file)


        if web in dat:
            email=dat[web]["Email"]
            password=dat[web]["Password"]
            messagebox.showinfo(title="Website Details", message=f"Email:{email}\nPassword:{password}")

        else:
            messagebox.showinfo(title="Error", message=f"Oops...\nWebsite not found!")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"Oops...\nFile not found!")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website=website_entry.get().title()
    email=email_entry.get().lower()
    password=password_entry.get()

    new_data= {website: {
        "Email": email, 
        "Password": password}
        }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please do not leave any Field empty")
    else:
        is_ok=messagebox.askokcancel(title="Website", message=f"These are the details you entered.\n Email: {email}\n Password: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data=json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label= Label(text="Website:")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label=Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry=Entry(width=29)
website_entry.grid(row=1, column=1)
email_entry=Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2) 
email_entry.insert(0, "ezekieloluwadamy@gmail.com")
password_entry=Entry(width=29)
password_entry.grid(row=3, column=1)


#Buttons
add_button= Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
password_button=Button(text="Generate Password", width=14, command=PASSWORD_GENERATOR)
password_button.grid(row=3, column=2)
search_button=Button(text="Search", width=14, command=FIND_PASSWORD)
search_button.grid(row=1, column=2)







window.mainloop()