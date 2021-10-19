import tkinter as tk
import UserDB
from tkinter import messagebox

CustomerDB = UserDB.UserData('CustomerLogin.db')

class Guest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
        self.selected_item = 0

    def create_widgets(self):
        # username
        self.firstName_text = tk.StringVar()
        self.firstName_label = tk.Label(
            self, text='First Name', font=('bold', 14), pady=20)
        self.firstName_label.grid(row=0, column=0, sticky=tk.W)
        self.firstName_entry = tk.Entry(self, textvariable=self.firstName_text)
        self.firstName_entry.grid(row=0, column=1)
        # password
        self.lastname_text = tk.StringVar()
        self.lastname_label = tk.Label(
            self, text='Last Name', font=('bold', 14))
        self.lastname_label.grid(row=0, column=2, sticky=tk.W)
        self.lastname_entry = tk.Entry(
            self, textvariable=self.lastname_text)
        self.lastname_entry.grid(row=0, column=3)
        # car plate
        self.carplate_text = tk.StringVar()
        self.carplate_label = tk.Label(
            self, text='Car Plate', font=('bold', 14))
        self.carplate_label.grid(row=1, column=0, sticky=tk.W)
        self.carplate_entry = tk.Entry(
            self, textvariable=self.carplate_text)
        self.carplate_entry.grid(row=1, column=1)
        # card number
        self.card_number = tk.StringVar()
        self.card_number_label = tk.Label(
            self, text='Card Number', font=('bold', 14), pady=20)
        self.card_number_label.grid(row=1, column=2, sticky=tk.W)
        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.card_number_entry = tk.Entry(self, textvariable=self.card_number, validate="key", validatecommand=vcmd)
        self.card_number_entry.grid(row=1, column=3)

        # Buttons
        self.reserv_btn = tk.Button(
            self, text="Go Reserve", width=12, command=self.guestReg)
        self.reserv_btn.grid(row=3, column=0, pady=20)

        self.clear_btn = tk.Button(
            self, text="Clear Input", width=12, command=self.clear_text)
        self.clear_btn.grid(row=3, column=1)

        self.cancel_btn = tk.Button(
            self, text="Cancel", width=12, command=self.cancel_reg)
        self.cancel_btn.grid(row=3, column=3)

    # Validate card number
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

    def guestReg(self):
        # for names in CustomerDB.find_name():
        #     if self.firstName_text.get() == names[0]:
        #         messagebox.showerror("Username", "Username already exist")
        #         return
        #         break
        if self.firstName_text.get() == '' or self.lastname_text.get() == '' or self.carplate_text.get() == '' or self.card_number.get() == '':
            messagebox.showerror(
                "Required Fields", "Please include all fields")
            return
            # break

        # self.controller.saveGuest(self.firstName_text.get())

        CustomerDB.addGuest(self.firstName_text.get(), self.lastname_text.get(),
                  self.carplate_text.get(), self.card_number.get())
    #     # Clear list
    #     # self.users_list.delete(0, tk.END)
    #     # Insert into list
    #     # self.users_list.insert(tk.END, (self.username_text.get(), self.password_text.get(
    #     # ), self.carplate_text.get(), self.card_number.get(), self.membership.get()))
        self.controller.show_frame("GuestRes")
    #     # self.populate_list()
    #     messagebox.showinfo("Register successful", "Back to Login")
    #     self.controller.show_frame("Login")

    # Clear all text fields
    def clear_text(self):
        self.firstName_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.carplate_entry.delete(0, tk.END)
        self.card_number_entry.delete(0, tk.END)


    def cancel_reg(self):
        self.controller.show_frame("Login")
