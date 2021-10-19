import tkinter as tk
import UserDB
from tkinter import messagebox

CustomerDB = UserDB.UserData('CustomerLogin.db')

class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Parking")
        self.controller.geometry("750x450")
        self.create_widgets()
        self.selected_item = 0
        # self.populate_list()

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
        self.password_label.grid(row=0, column=2, sticky=tk.W)
        self.password_entry = tk.Entry(
            self, show='*', textvariable=self.password_text)
        self.password_entry.grid(row=0, column=3)
        # First Name
        self.FirstN_text = tk.StringVar()
        self.FirstN_label = tk.Label(
            self, text='First Name', font=('bold', 14), pady=20)
        self.FirstN_label.grid(row=1, column=0, sticky=tk.W)
        self.FirstN_entry = tk.Entry(self, textvariable=self.FirstN_text)
        self.FirstN_entry.grid(row=1, column=1)
        # Last Name
        self.LastN_text = tk.StringVar()
        self.LastN_label = tk.Label(
            self, text='Last Name', font=('bold', 14))
        self.LastN_label.grid(row=1, column=2, sticky=tk.W)
        self.LastN_entry = tk.Entry(
            self, textvariable=self.LastN_text)
        self.LastN_entry.grid(row=1, column=3)
        # car plate
        self.carplate_text = tk.StringVar()
        self.carplate_label = tk.Label(
            self, text='Car Plate', font=('bold', 14))
        self.carplate_label.grid(row=2, column=0, sticky=tk.W)
        self.carplate_entry = tk.Entry(
            self, textvariable=self.carplate_text)
        self.carplate_entry.grid(row=2, column=1)
        # card number
        self.card_number = tk.StringVar()
        self.card_number_label = tk.Label(
            self, text='Card Number', font=('bold', 14), pady=20)
        self.card_number_label.grid(row=2, column=2, sticky=tk.W)
        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.card_number_entry = tk.Entry(self, textvariable=self.card_number, validate="key", validatecommand=vcmd)
        self.card_number_entry.grid(row=2, column=3)

        # membership
        self.membership = tk.IntVar()
        self.membership_label = tk.Label(
            self, text='Membership', font=('bold', 14))
        self.membership_label.grid(row=3, column=0, stick=tk.W)
        self.yesMember = tk.Radiobutton(self, text='Yes', variable=self.membership, value=1)
        self.yesMember.grid(row=3, column=1)
        self.noMember = tk.Radiobutton(self, text='No', variable=self.membership, value=0)
        self.noMember.grid(row=3, column=2)

        # Buttons
        self.add_btn = tk.Button(
            self, text="Register", width=12, command=self.Register_User)
        self.add_btn.grid(row=4, column=0, pady=20)

        self.exit_btn = tk.Button(
            self, text="Clear Input", width=12, command=self.clear_text)
        self.exit_btn.grid(row=4, column=1)

        self.remove_btn = tk.Button(
            self, text="Cancel", width=12, command=self.cancel_reg)
        self.remove_btn.grid(row=4, column=3)

        # DEBUG SECTION

    #     self.list_name = tk.Button(
    #         self, text='List Name', width=12, command=self.listName)
    #     self.list_name.grid(row=3, column=4)
    # #
    # def listName(self):
    #     count = 0
    #     for row in db.fetch():
    #         # self.username_text.get() == user_data[1] and self.users_list.get(count)[0] != user_data[0]
    #         # print(self.selected_item)
    #         print(self.users_list.get(count)[0], row[0])
    #         if self.users_list.get(count)[0] != row[0]:
    #             print("oi")
    #
    #         # print(self.username_text.get(), row[1])
    #         count += 1


    #     for names in db.find_name():
    #         print(self.username_text.get(), names[0])
    #         if self.username_text.get() == names[0]:
    #             print("equal")
    #         # messagebox.showerror("Username", "Username already exist")
    #         else:
    #             print("not")
    #             register_name = self.username_text.get()

        # NomeUser = []
        # for rows in db.find_name():
        #     print(rows[0])
        # if NomeUser[0][0] == "asdasda":
        #     print(NomeUser[0][0])
        #     print("correct")
        # else:
        #     print(NomeUser[0][0])
        #     print("wrong")

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

    def Register_User(self):
        for names in CustomerDB.find_name():
            if self.username_text.get() == names[0]:
                messagebox.showerror("Username", "Username already exist")
                return
                break
            elif self.username_text.get() == '' or self.password_text.get() == '' or self.FirstN_text.get() == '' or self.LastN_text.get() == '' or self.carplate_text.get() == '' or self.card_number.get() == '':
                messagebox.showerror(
                    "Required Fields", "Please include all fields")
                return
                break

        CustomerDB.insert(self.username_text.get(), self.password_text.get(), self.FirstN_text.get(), self.LastN_text.get(),
                  self.carplate_text.get(), self.card_number.get(), self.membership.get())
        # Clear list
        # self.users_list.delete(0, tk.END)
        # Insert into list
        # self.users_list.insert(tk.END, (self.username_text.get(), self.password_text.get(
        # ), self.carplate_text.get(), self.card_number.get(), self.membership.get()))
        self.clear_text()
        # self.populate_list()
        messagebox.showinfo("Register successful", "Back to Login")
        self.controller.show_frame("Login")

    # Clear all text fields
    def clear_text(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.FirstN_entry.delete(0, tk.END)
        self.LastN_entry.delete(0, tk.END)
        self.carplate_entry.delete(0, tk.END)
        self.card_number_entry.delete(0, tk.END)


    def cancel_reg(self):
        self.controller.show_frame("Login")
