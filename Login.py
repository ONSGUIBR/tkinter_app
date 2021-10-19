import tkinter as tk
import UserDB
from tkinter import messagebox
import time

CustomerDB = UserDB.UserData('CustomerLogin.db')
start = time.time()

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # username
        self.username_text = tk.StringVar()
        self.username_label = tk.Label(
            self, text='Username', font=('bold', 14), pady=20)
        self.username_label.grid(row=0, column=0, sticky=tk.W)
        self.username_entry = tk.Entry(self, textvariable=self.username_text)
        self.username_entry.grid(row=0, column=1)
        # password
        self.password_text = tk.StringVar()
        self.password_label = tk.Label(
            self, text='Password', font=('bold', 14))
        self.password_label.grid(row=1, column=0, sticky=tk.W)
        self.password_entry = tk.Entry(
            self, show='*', textvariable=self.password_text)
        self.password_entry.grid(row=1, column=1)

        self.login_btn = tk.Button(
            self, text="Login", width=12, command=self.user_login)
        self.login_btn.grid(row=2, column=1, pady=20)

        self.Register_btn = tk.Button(
            self, text="Register", width=12, command=self.user_register)
        self.Register_btn.grid(row=3, column=1)

        self.guest_btn = tk.Button(
            self, text="Guest", width=12, command=self.guest_login)
        self.guest_btn.grid(row=5, column=1, pady=20)

        self.exit_btn = tk.Button(
            self, text="Exit", width=12, command=self.ExitB)
        self.exit_btn.grid(row=6, column=1)

    def ExitB(self):
        end = time.time()
        used_time = round((end-start), 2)
        messagebox.showinfo("Time", "Application use time: " + str(used_time) + "s")
        self.controller.destroy()

    def user_login(self):
        check_login = []
        login_True = False
        for username_pass in CustomerDB.find_user_pass():
            check_login.append(username_pass)

        for i in range(len(check_login)):
            if check_login[i][0] == self.username_text.get() and check_login[i][1] == self.password_text.get():
                login_True = True
        if login_True:
            CustomerDB.storeName(self.username_text.get())
            self.controller.save(self.username_text.get())
            self.controller.show_frame("UserMenu")
        else:
            messagebox.showerror("Login Error", "Username or password is wrong")

    def user_register(self):
        self.controller.show_frame("Register")

    def guest_login(self):
        self.controller.show_frame("Guest")
