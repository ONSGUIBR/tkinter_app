import tkinter as tk
from tkinter import messagebox
import SignUp
import Login
import UserMenu
import guestLogin
import ReservMenu
import guestReserv
import ViewRes
import guestView

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.saveUser = []
        self.saveGuest = []

        self.frames = {}
        for F in (Login.Login, SignUp.Register, UserMenu.UserMenu, guestLogin.Guest, ReservMenu.Reserv, guestReserv.GuestRes, ViewRes.ResView, guestView.guestView):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def save (self, username):
        self.saveUser.append(username)

    def getUser(self):
        return self.saveUser

    def saveGuest (self, username):
        self.saveGuest.append(username)

    def getGuest(self):
        return self.saveGuest

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()

    app.mainloop()
