import tkinter as tk
import UserDB
from tkinter import messagebox

db = UserDB.UserData('CustomerLogin.db')

class Reserved(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
        self.selected_reserv = 0
        self.populate_reserv()
        self.selected_guest = 0
        self.populate_guest()

    def create_widgets(self):

        # Reserv List
        self.Reserv_label = tk.Label(
            self, text='Reservation', font=('bold', 14), pady=20)
        self.Reserv_label.grid(row=0, column=0, sticky=tk.W)

        self.Reserv_lits = tk.Listbox(self, height=8, width=100, border=0)
        self.Reserv_lits.grid(row=1, column=0, columnspan=3,
                             rowspan=1, pady=10)
        # Create scrollbar
        self.yscrollbar = tk.Scrollbar(self, orient='vertical', command=self.Reserv_lits.yview)
        self.yscrollbar.grid(row=1, column=1)
        self.xscrollbar = tk.Scrollbar(self, orient='horizontal', command=self.Reserv_lits.xview)
        self.xscrollbar.grid(row=4, column=0)
        # Set scrollbar to parts
        self.Reserv_lits.configure(yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)
        self.Reserv_lits.bind('<<ListboxSelect>>', self.selected_reserv)


        # Guest List
        self.Guest_label = tk.Label(
            self, text='Guest', font=('bold', 14), pady=20)
        self.Guest_label.grid(row=5, column=0, sticky=tk.W)

        self.Guest_list = tk.Listbox(self, height=8, width=100, border=0)
        self.Guest_list.grid(row=6, column=0, columnspan=3,
                             rowspan=1, pady=10)
        # Create scrollbar
        self.yscrollbar = tk.Scrollbar(self, orient='vertical', command=self.Guest_list.yview)
        self.yscrollbar.grid(row=6, column=1)
        self.xscrollbar = tk.Scrollbar(self, orient='horizontal', command=self.Guest_list.xview)
        self.xscrollbar.grid(row=9, column=0)
        # Set scrollbar to parts
        self.Guest_list.configure(yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)
        self.Guest_list.bind('<<ListboxSelect>>', self.selected_guest)

        # self.test_btn = tk.Button(
        #     self, text="Remove", width=12, command=self.populate_guest)
        # self.test_btn.grid(row=10, column=2)
        #
        # self.test_btn = tk.Button(
        #     self, text="Remove", width=12, command=self.populate_guest)
        # self.test_btn.grid(row=10, column=2)

        self.test_btn = tk.Button(
            self, text="View", width=12, command=self.populate_guest)
        self.test_btn.grid(row=10, column=2)

        self.cancel_btn = tk.Button(
            self, text="Back", width=12, command=self.backMenu)
        self.cancel_btn.grid(row=10, column=0, padx=300, pady=20)

    def selected_reserv(self, event):
        try:
            # Get index
            index = self.Reserv_lits.curselection()[0]
            # Get selected item
            self.selected_reserv = self.Reserv_lits.get(index)
            # print(selected_item) # Print tuple

        except IndexError:
            pass

    def populate_reserv(self):
        self.Reserv_lits.delete(0, tk.END)
        # # Loop through records
        for row in db.fetchResNames():
            self.Reserv_lits.insert(tk.END, row)


    def selected_guest(self, event):
        try:
            # Get index
            index = self.Guest_list.curselection()[0]
            # Get selected item
            self.selected_reserv = self.Guest_list.get(index)
            # print(selected_item) # Print tuple

        except IndexError:
            pass

    def populate_guest(self):
        self.Guest_list.delete(0, tk.END)
        # # Loop through records
        for row in db.fetchGuestName():
            self.Guest_list.insert(tk.END, row)

    def backMenu(self):
        self.controller.show_frame('MenuADM')
