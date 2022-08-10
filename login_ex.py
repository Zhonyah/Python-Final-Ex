from tkinter import *
from tkinter import messagebox
import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate(
    'D:\Python-Final-Ex\Friebase\project-python-final-ex-firebase-adminsdk-gz60r-f79d9c41fa.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-python-final-ex-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def login():  # ฟังก์ชั่นการตรวจสอบการ Login

    ref_id = db.reference('Users/id_users')
    user_id = ref_id.get()
    ref_passoword = db.reference('Users/password_users')
    user_password = str(ref_passoword.get())

    user = username.get()
    code = password.get()

    if user == user_id and code == user_password:
        toplevel()
    elif user == "" and code == "":
        messagebox.showerror("Invalid", "Please Enter Username and Password")
    elif user == "":
        messagebox.showerror("Invalid", "Please Enter Username")
    elif user != user_id and code != user_password:
        messagebox.showerror("Invalid", "Invalid Username and Password")
    elif user != user_id:
        messagebox.showerror("Invalid", "Please Enter Username")
    elif code != user_password:
        messagebox.showerror("Invalid", "Please Enter Password")

def toplevel():
    scr_menu = Toplevel()
    scr_menu.title("MENU")
    scr_menu.geometry("1280x720+150+80")
    scr_menu.configure(bg="#2f3136")
    scr_menu.resizable(False, False)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1280x720+150+80")
    root.resizable(False, False)
    root.configure(bg="#2f3136")

    # icon
    image_icon = PhotoImage(file="Pic\login.png")
    root.iconphoto(False, image_icon)
    root.title("Login System")
    lblTitle = Label(text="Welcome Back", font=(
        "Gudea", 42, "bold"), fg="#ffffff", bg="#2f3136")
    lblTitle.pack(pady=50)
    lblTitle2 = Label(text="We’re so excited to see you agian!", font=(
        "Gudea", 10, "bold"), fg="#ffffff", bg="#2f3136")
    lblTitle2.pack(pady=1)

    # GUI
    Label(root, text="id", font=("Gudea", 14, "bold"),
        fg="#99AAB5", bg="#2f3136").place(x=140, y=240)
    Label(root, text="Passowrd", font=("Gudea", 14, "bold"),
        fg="#99AAB5", bg="#2f3136").place(x=140, y=380)
    Label(root, text="Passowrd", font=("Gudea", 14, "bold"),
        fg="#99AAB5", bg="#2f3136").place(x=140, y=380)

    #Sringvar
    username = StringVar()
    password = StringVar()

    #entry gui
    entry_username = Entry(root, textvariable=username,
                        width=23, bd=2, font=("Gudea", 24))
    entry_username.place(x=140, y=277)
    entry_password = Entry(root, textvariable=password,
                        width=23, bd=2, font=("Gudea", 24), show="*")
    entry_password.place(x=140, y=420)

    Button(root, text="Login", font=("Gudea", 14, "bold"), height=2,  # ปุ่มกดเรียกใชังานฟังก์ชั่น Login
        width=43, bg="#7289DA", fg="#ffffff", command=login).place(x=140, y=520)



    root.mainloop()
