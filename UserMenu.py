import tkinter as tk
import UserDB
from tkinter import messagebox
import time

db = UserDB.UserData('CustomerLogin.db')
start = time.time()

class UserMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.Reserv_btn = tk.Button(
            self, text="Reserve Slot", width=12, command=self.goReserv)
        self.Reserv_btn.grid(row=0, column=0, pady=20, padx=30)

        # Temp Plate
        self.Plate_text = tk.StringVar()
        self.Plate_label = tk.Label(
            self, text='Temporary Plate', font=('bold', 14))
        self.Plate_label.grid(row=0, column=1, sticky=tk.W)
        self.Plate_entry = tk.Entry(
            self, textvariable=self.Plate_text)
        self.Plate_entry.grid(row=0, column=2)

        self.addtemp_btn = tk.Button(
            self, text="Add temporary plate", width=20, command=self.addtemp_plate)
        self.addtemp_btn.grid(row=1, column=2, padx=30)

        # Temp Card
        self.card_text = tk.StringVar()
        self.card_label = tk.Label(
            self, text='Temporary Card', font=('bold', 14))
        self.card_label.grid(row=2, column=1, pady=10, sticky=tk.W)
        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.card_entry = tk.Entry(
            self, textvariable=self.card_text, validate="key", validatecommand=vcmd)
        self.card_entry.grid(row=2, column=2)

        self.addcard_btn = tk.Button(
            self, text="Add temporary Card", width=20, command=self.addtempCard)
        self.addcard_btn.grid(row=3, column=2, padx=30)

        self.resV_btn = tk.Button(
            self, text="View Reservation", width=12, command=self.goResV)
        self.resV_btn.grid(row=3, column=0, pady=20)

        self.exit_btn = tk.Button(
            self, text="Exit", width=12, command=self.ExitB)
        self.exit_btn.grid(row=4, column=0, pady=20)

    # add temp plate
    def addtemp_plate(self):
        name = self.controller.getUser()[0]
        user_id = db.findUserId(name)[0][0]
        if self.Plate_text.get() == "":
            messagebox.showerror("Error", "Plate field is empty")
            return
        db.addTempPlate(user_id, self.Plate_text.get())
        self.Plate_entry.delete(0, tk.END)

    # add temp card
    def addtempCard(self):
        name = self.controller.getUser()[0]
        user_id = db.findUserId(name)[0][0]
        if self.card_text.get() == "":
            messagebox.showerror("Error", "Card number field is empty")
            return
        db.addTempCard(user_id, self.card_text.get())
        self.card_entry.delete(0, tk.END)

    # validate int
    def validate(self, action, index, value_if_allowed,
    prior_value, text, validation_type, trigger_type, widget_name):
        if(action=='1'):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    def goResV(self):
        self.controller.show_frame("ResView")

    def goReserv(self):
        self.controller.show_frame("Reserv")

    def ExitB(self):
        end = time.time()
        used_time = round((end-start), 2)
        messagebox.showinfo("Time", "Application use time: " + str(used_time) + "s")
        self.controller.destroy()
