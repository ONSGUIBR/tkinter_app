import tkinter as tk
from tkinter import messagebox
import UserDB

db = UserDB.UserData('CustomerLogin.db')

class LocationADM(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
        self.selected_loc = 0
        self.selected_spot = 0
        self.populate_loc()
        self.populate_spot()

    def create_widgets(self):
        # location Name
        self.Location_txt = tk.StringVar()
        self.Location_label = tk.Label(
            self, text='Location', font=('bold', 14), pady=20)
        self.Location_label.grid(row=0, column=0, sticky=tk.W)
        self.Location_entry = tk.Entry(self, textvariable=self.Location_txt)
        self.Location_entry.grid(row=0, column=1)

        # Locaiton drop down menu
        LocationList = self.dropMenuLoc()
        self.location_name = tk.StringVar()
        self.Location_label = tk.Label(
            self, text='Location', font=('bold', 14))
        self.Location_label.grid(row=1, column=0, sticky=tk.W)
        self.location_name.set(LocationList[0])
        self.location_drop = tk.OptionMenu(self, self.location_name, *LocationList)
        self.location_drop.grid(row=1, column=1)

        # Spot number
        self.Spot_numb = tk.StringVar()
        self.Spot_numb_label = tk.Label(
            self, text='Number of Spots', font=('bold', 14), pady=20)
        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.Spot_numb_label.grid(row=3, column=0, sticky=tk.W)
        self.Spot_numb_entry = tk.Entry(self, textvariable=self.Spot_numb, width=8, validate="key", validatecommand=vcmd)
        self.Spot_numb_entry.grid(row=3, column=1)

        # cost
        self.Cost_numb = tk.StringVar()
        self.Cost_numb_label = tk.Label(
            self, text='Cost', font=('bold', 14), pady=20)
        self.Cost_numb_label.grid(row=4, column=0, sticky=tk.W)
        self.Cost_numb_entry = tk.Entry(self, textvariable=self.Cost_numb, width=8)
        self.Cost_numb_entry.grid(row=4, column=1)

        # Date
        self.Date = tk.StringVar()
        self.Date_label = tk.Label(
            self, text='Date', font=('bold', 14), pady=20)
        self.Date_label.grid(row=3, column=2, sticky=tk.W)
        self.Date_entry = tk.Entry(self, textvariable=self.Date, width=20)
        self.Date_entry.grid(row=3, column=3)

        # Reserved
        self.Reserved = tk.IntVar()
        self.Reserved_label = tk.Label(
            self, text='Reserved', font=('bold', 14))
        self.Reserved_label.grid(row=4, column=2, stick=tk.W)
        self.yesReserv = tk.Radiobutton(self, text='Yes', variable=self.Reserved, value=1)
        self.yesReserv.grid(row=4, column=3)
        self.noReserv = tk.Radiobutton(self, text='No', variable=self.Reserved, value=0)
        self.noReserv.grid(row=4, column=4)

        # User list (listbox)
        self.loc_list = tk.Listbox(self, height=8, width=30, border=0)
        self.loc_list.grid(row=0, column=4, columnspan=3,
                             rowspan=3, pady=20, padx=20)
        # Create scrollbar
        self.yscrollbar = tk.Scrollbar(self, orient='vertical', command=self.loc_list.yview)
        self.yscrollbar.grid(row=0, column=7)
        self.xscrollbar = tk.Scrollbar(self, orient='horizontal', command=self.loc_list.xview)
        self.xscrollbar.grid(row=2, column=5)
        # Set scrollbar to parts
        self.loc_list.configure(yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)
        # self.scrollbar.configure(command=self.users_list.yview)

        # Bind select
        self.loc_list.bind('<<ListboxSelect>>', self.selected_loc)


        # Spot number
        self.Spot_number = tk.StringVar()
        self.Spot_number_label = tk.Label(
            self, text='Number of Spot', font=('bold', 14), pady=20)
        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.Spot_number_label.grid(row=7, column=3, sticky=tk.W)
        self.Spot_number_entry = tk.Entry(self, textvariable=self.Spot_number, width=8, validate="key", validatecommand=vcmd)
        self.Spot_number_entry.grid(row=7, column=4)

        # cost
        self.Cost_numb_up = tk.StringVar()
        self.Cost_numb_up_label = tk.Label(
            self, text='Cost', font=('bold', 14), pady=20)
        self.Cost_numb_up_label.grid(row=8, column=3, sticky=tk.W)
        self.Cost_numb_up_entry = tk.Entry(self, textvariable=self.Cost_numb_up, width=8)
        self.Cost_numb_up_entry.grid(row=8, column=4)

        # time slot
        self.time_slot_text = tk.StringVar()
        self.time_slot_label = tk.Label(
            self, text='time-slot', font=('bold', 14), pady=20)
        self.time_slot_label.grid(row=9, column=3, sticky=tk.W)
        self.time_slot_entry = tk.Entry(self, textvariable=self.time_slot_text, width=20)
        self.time_slot_entry.grid(row=9, column=4)


        self.spot_list = tk.Listbox(self, height=8, width=50, border=0)
        self.spot_list.grid(row=7, column=0, columnspan=3,
                             rowspan=3, pady=10, padx=10)
        # Create scrollbar
        self.yscrollbar = tk.Scrollbar(self, orient='vertical', command=self.spot_list.yview)
        self.yscrollbar.grid(row=7, column=2, padx=(60,0))
        self.xscrollbar = tk.Scrollbar(self, orient='horizontal', command=self.spot_list.xview)
        self.xscrollbar.grid(row=11, column=0)
        # Set scrollbar to parts
        self.spot_list.configure(yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)
        # self.scrollbar.configure(command=self.users_list.yview)

        # Bind select
        self.spot_list.bind('<<ListboxSelect>>', self.selected_spot)

        # # car plate
        # self.carplate_text = tk.StringVar()
        # self.carplate_label = tk.Label(
        #     self, text='Car Plate', font=('bold', 14))
        # self.carplate_label.grid(row=1, column=0, sticky=tk.W)
        # self.carplate_entry = tk.Entry(
        #     self, textvariable=self.carplate_text)
        # self.carplate_entry.grid(row=1, column=1)

        # Buttons
        self.add_btn = tk.Button(
            self, text="Add Locaiton", width=12, command=self.addLoc)
        self.add_btn.grid(row=0, column=3, padx=20, pady=20)

        self.remove_btn = tk.Button(
            self, text="Remove Location", width=12, command=self.removeLoct)
        self.remove_btn.grid(row=1, column=8, pady=10)

        self.addloc_btn = tk.Button(
            self, text="Add Spots", width=12, command=self.addSpots)
        self.addloc_btn.grid(row=5, column=0)

        self.removeSpot_btn = tk.Button(
            self, text="Remove Spot", width=12, command=self.removeSpot)
        self.removeSpot_btn.grid(row=12, column=0, pady=10)

        self.clear_btn = tk.Button(
            self, text="Clear Fields", width=12, command=self.clear_text)
        self.clear_btn.grid(row=12, column=2)

        self.update_spot_btn = tk.Button(
            self, text="Update Spot", width=12, command=self.update_spot)
        self.update_spot_btn.grid(row=12, column=4)

        self.back_btn = tk.Button(
            self, text="Back", width=12, command=self.BackMenu)
        self.back_btn.grid(row=12, column=6)


    def selected_loc(self, event):
        try:
            # Get index
            index = self.loc_list.curselection()[0]
            # Get selected item
            self.selected_loc = self.loc_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            self.Location_entry.delete(0, tk.END)
            self.Location_entry.insert(tk.END, self.selected_loc[1])

        except IndexError:
            pass

    def populate_loc(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.loc_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetchLoc():
            # Insert into list
            self.loc_list.insert(tk.END, row)

    def selected_spot(self, event):
        try:
            # Get index
            index = self.spot_list.curselection()[0]
            # Get selected item
            self.selected_spot = self.spot_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            self.Spot_number_entry.delete(0, tk.END)
            self.Spot_number_entry.insert(tk.END, self.selected_spot[2])
            self.Cost_numb_up_entry.delete(0, tk.END)
            self.Cost_numb_up_entry.insert(tk.END, self.selected_spot[4])
            self.time_slot_entry.delete(0, tk.END)
            self.time_slot_entry.insert(tk.END, self.selected_spot[5])

        except IndexError:
            pass

    def populate_spot(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.spot_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetchLocations():
            # Insert into list
            self.spot_list.insert(tk.END, row)
            # self.loc_list.insert(tk.END, row)

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

    def addLoc(self):
        for names in db.fetchLoc():
            if self.Location_txt.get() == names[0]:
                messagebox.showerror("Username", "Username already exist")
                return
                break
            elif self.Location_txt.get() == '':
                messagebox.showerror(
                    "Required Fields", "Location is empty")
                return
                break
        db.addLoc(self.Location_txt.get(), 20)
        self.clear_text()
        self.populate_loc()

    def dropMenuLoc(self):
        list = []
        for name in db.fetchLoc():
            list.append(name[0])
        if len(list) == 0:
            list.append('None')
            return list
        else:
            return list

    def update_spot(self):
        if self.Spot_number.get() == '' or self.Cost_numb_up.get() == '' or self.time_slot_text.get() == '':
            messagebox.showerror(
                "Required Fields", "Please include all fields")
            return

        db.updateSpots(self.selected_spot[0], self.Spot_number.get(), self.Cost_numb_up.get(), self.time_slot_text.get())
        self.populate_spot()
        self.clear_text()

    def removeLoct(self):
        db.removeLoc(self.selected_loc[0])
        self.populate_loc()
        self.populate_spot()

    def removeSpot(self):
        db.removeSpots(self.selected_spot[0])
        self.populate_spot()

    def addSpots(self):
        if self.Spot_numb.get() == '' or self.Cost_numb.get() == '' or self.Date.get() == '':
            messagebox.showerror(
                "Required Fields", "Please include Spot numbers, Cost and Date")
            return
        location_id = db.findLocId(self.location_name.get())[0][0]
        for i in range(int(self.Spot_numb.get())):
            db.addSpots(location_id, i+1, self.Reserved.get(), self.Cost_numb.get(), self.Date.get(), 0)
        self.populate_spot()

    def ExitB(self):
        self.controller.destroy()

    def BackMenu(self):
        self.controller.show_frame("MenuADM")

    def clear_text(self):
        self.Location_entry.delete(0, tk.END)
        self.Spot_numb_entry.delete(0, tk.END)
        self.Cost_numb_entry.delete(0, tk.END)
        self.Spot_number_entry.delete(0, tk.END)
        self.Cost_numb_up_entry.delete(0, tk.END)
        self.time_slot_entry.delete(0, tk.END)
