import tkinter as tk
from tkinter import messagebox

class MenuADM(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.goSignUp = tk.Button(
            self, text="Register Menu", width=12, command=self.goSignUpADM)
        self.goSignUp.grid(row=0, column=0, pady=20, padx=30)

        self.Loc_btn = tk.Button(
            self, text="Location Meun", width=12, command=self.goLocADM)
        self.Loc_btn.grid(row=1, column=0)

        self.Reserved_btn = tk.Button(
            self, text="Reservations", width=12, command=self.GoReservation)
        self.Reserved_btn.grid(row=2, column=0, pady=20)

        self.exit_btn = tk.Button(
            self, text="Exit", width=12, command=self.ExitB)
        self.exit_btn.grid(row=3, column=0)

    def ExitB(self):
        self.controller.destroy()

    def goSignUpADM(self):
        self.controller.show_frame("RegisterADM")

    def goLocADM(self):
        self.controller.show_frame("LocationADM")

    def GoReservation(self):
        self.controller.show_frame("Reserved")
