import tkinter as tk
import UserDB
from tkinter import messagebox

db = UserDB.UserData('CustomerLogin.db')

class Reserv(tk.Frame):

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

        plateList = ["Plate", "Temporary Plate"]
        self.plate_name = tk.StringVar()
        self.plate_label = tk.Label(
            self, text='plate', font=('bold', 14))
        self.plate_label.grid(row=1, column=0, sticky=tk.W)
        self.plate_name.set(plateList[0])
        self.plate_drop = tk.OptionMenu(self, self.plate_name, *plateList)
        self.plate_drop.grid(row=1, column=1, padx=(0,120))

        card_list = ["Card", "Temporary Card"]
        self.card_name = tk.StringVar()
        self.card_label = tk.Label(
            self, text='Card', font=('bold', 14))
        self.card_label.grid(row=2, column=0, sticky=tk.W)
        self.card_name.set(card_list[0])
        self.card_drop = tk.OptionMenu(self, self.card_name, *card_list)
        self.card_drop.grid(row=2, column=1, padx=(0,120))

        # Spot list
        self.spot_list = tk.Listbox(self, height=8, width=50, border=0)
        self.spot_list.grid(row=3, column=0, columnspan=3,
                             rowspan=3, pady=10, padx=10)
        # Create scrollbar
        self.yscrollbar = tk.Scrollbar(self, orient='vertical', command=self.spot_list.yview)
        self.yscrollbar.grid(row=3, column=3)
        self.xscrollbar = tk.Scrollbar(self, orient='horizontal', command=self.spot_list.xview)
        self.xscrollbar.grid(row=6, column=0)
        # Set scrollbar to parts
        self.spot_list.configure(yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)
        # self.scrollbar.configure(command=self.users_list.yview)
        # Bind select
        self.spot_list.bind('<<ListboxSelect>>', self.selected_spot)

        self.add_btn = tk.Button(
            self, text="Find Spots", width=12, command=self.populate_spot)
        self.add_btn.grid(row=0, column=3, padx=20, pady=20)

        self.res_btn = tk.Button(
            self, text="Reserve", width=12, command=self.Res_Spot)
        self.res_btn.grid(row=7, column=0, padx=20, pady=20)

        self.ext_btn = tk.Button(
            self, text="Back", width=12, command=self.backMenu)
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
        user = self.controller.getUser()[0]
        member = db.getMember(user)[0][0]
        if member == '1':
            locID = int(db.findLocId(self.location_name.get())[0][0])
            self.spot_list.delete(0, tk.END)
            # # Loop through records
            for row in db.fetchSpots(locID):
                self.spot_list.insert(tk.END, row)
        else:
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
        plate = []
        card = []
        Res_plate = ""
        Res_card = ""
        user = self.controller.getUser()[0]
        for name in db.find_plate(user):
            plate.append(name)
        for row in db.find_card(user):
            card.append(row)
        Res_plate = plate[0][0]
        Res_card = card[0][0]
        if self.plate_name.get() == "Temporary Plate" or self.card_name.get() == "Temporary Card":
            if plate[0][1] == None or card[0][1] == None:
                messagebox.showerror("Error", "No temporary card or plate")
                return
            elif self.plate_name.get() == "Temporary Plate" and self.card_name.get() != "Temporary Card":
                Res_plate = plate[0][1]
            elif self.card_name.get() == "Temporary Card" and self.plate_name.get() != "Temporary Plate":
                Res_card = card[0][1]
            elif self.plate_name.get() == "Temporary Plate" and self.card_name.get() == "Temporary Card":
                Res_card = card[0][1]
                Res_plate = plate[0][1]

        try:
            index = self.spot_list.curselection()[0]
            self.selected_spot = self.spot_list.get(index)
        except IndexError:
            pass

        user_id = db.findUserId(user)[0][0]
        spot_id = self.selected_spot[0]
        locID = int(db.findLocId(self.location_name.get())[0][0])
        start_time = self.selected_spot[3]
        db.addReserve(locID, spot_id, user_id, Res_plate, Res_card, start_time, start_time)
        db.occupied(spot_id)

        messagebox.showinfo("Spot Reserved" , "Spot Reserved, back to menu")
        self.controller.show_frame("UserMenu")

    def backMenu(self):
        self.controller.show_frame("UserMenu")
