import tkinter as tk
import UserDB
from tkinter import messagebox
import time

db = UserDB.UserData('CustomerLogin.db')
start = time.time()

class GuestRes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
        self.selected_spot = 0

    def create_widgets(self):
        # Locaiton drop down menu
        LocationList = self.dropMenuLoc()
        self.location_name = tk.StringVar()
        self.Location_label = tk.Label(
            self, text='Location', font=('bold', 14))
        self.Location_label.grid(row=0, column=0, sticky=tk.W)
        self.location_name.set(LocationList[0])
        self.location_drop = tk.OptionMenu(self, self.location_name, *LocationList)
        self.location_drop.grid(row=0, column=1, padx=(0,120))

        # Spot list
        self.spot_list = tk.Listbox(self, height=8, width=50, border=0)
        self.spot_list.grid(row=1, column=0, columnspan=3,
                             rowspan=1, pady=10, padx=10)
        # Create scrollbar
        self.yscrollbar = tk.Scrollbar(self, orient='vertical', command=self.spot_list.yview)
        self.yscrollbar.grid(row=1, column=2)
        self.xscrollbar = tk.Scrollbar(self, orient='horizontal', command=self.spot_list.xview)
        self.xscrollbar.grid(row=4, column=0)
        # Set scrollbar to parts
        self.spot_list.configure(yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)
        # self.scrollbar.configure(command=self.users_list.yview)
        # Bind select
        self.spot_list.bind('<<ListboxSelect>>', self.selected_spot)

        self.add_btn = tk.Button(
            self, text="Find Spots", width=12, command=self.populate_spot)
        self.add_btn.grid(row=0, column=2, padx=20, pady=20)

        self.res_btn = tk.Button(
            self, text="Reserve", width=12, command=self.Res_Spot)
        self.res_btn.grid(row=7, column=0, padx=20, pady=20)

        self.resV_btn = tk.Button(
            self, text="View Reservations", width=12, command=self.goView)
        self.resV_btn.grid(row=7, column=1)

        self.ext_btn = tk.Button(
            self, text="Exit", width=12, command=self.backMenu)
        self.ext_btn.grid(row=7, column=2, padx=20, pady=20)

    def selected_spot(self, event):
        try:
            # Get index
            index = self.spot_list.curselection()[0]
            # Get selected item
            self.selected_spot = self.spot_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            # self.Spot_number_entry.delete(0, tk.END)
            # self.Spot_number_entry.insert(tk.END, self.selected_spot[0])
            # self.Cost_numb_up_entry.delete(0, tk.END)
            # self.Cost_numb_up_entry.insert(tk.END, self.selected_spot[1])
            # self.time_slot_entry.delete(0, tk.END)
            # self.time_slot_entry.insert(tk.END, self.selected_spot[2])

        except IndexError:
            pass

    def populate_spot(self):

        locID = int(db.findLocId(self.location_name.get())[0][0])
        self.spot_list.delete(0, tk.END)
        # # Loop through records
        for row in db.fetchNonSpots(locID):
            self.spot_list.insert(tk.END, row)

    def dropMenuLoc(self):
        list = []
        for name in db.fetchLoc():
            list.append(name[0])
        if len(list) == 0:
            list.append('None')
            return list
        else:
            return list

    def Res_Spot(self):
        guest_id = db.getGuestID()[0][0]
        guest_plate = db.fetchGuest(guest_id)[0][3]
        guest_card = db.fetchGuest(guest_id)[0][4]
        try:
            index = self.spot_list.curselection()[0]
            self.selected_spot = self.spot_list.get(index)
        except IndexError:
            pass

        spot_id = self.selected_spot[0]
        locID = int(db.findLocId(self.location_name.get())[0][0])
        start_time = self.selected_spot[3]
        db.addGuestRes(locID, spot_id, guest_id, guest_plate, guest_card, start_time, start_time)
        db.occupied(spot_id)
        self.populate_spot()
        #
        # messagebox.showinfo("Spot Reserved" , "Spot Reserved, back to menu")
        # self.controller.show_frame("UserMenu")

    def goView(self):
        self.controller.show_frame("guestView")

    def backMenu(self):
        end = time.time()
        used_time = round((end-start), 2)
        messagebox.showinfo("Time", "Application use time: " + str(used_time) + "s")
        self.controller.destroy()
