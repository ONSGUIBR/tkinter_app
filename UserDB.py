import sqlite3

class UserData:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Customer (id INTEGER PRIMARY KEY, username text, password text, First_Name TEXT, Last_Name TEXT,"
                "car_plate text, card_number INTERGER, membership TEXT, temp_Plate TEXT, temp_card_number INTERGER)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Locations (Loc_ID INTEGER PRIMARY KEY, Location_Name text, Membership_Cost REAL)"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Spots (Spot_ID INTEGER PRIMARY KEY, Loct_ID INTEGER, Spot_number INTEGER, Reserved INTEGER, Cost REAL, time_slot_ava text, available INTEGER "
                ", FOREIGN KEY (Loct_ID) REFERENCES Locations (Loc_ID))"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Reservation (Reserv_ID INTEGER PRIMARY KEY, Loc_ID INTEGER, Spot_ID INTEGER, user_id INTERGER, car_plate text, card_number INTERGER, time_slot_start text, time_slot_end,"
                "FOREIGN KEY (Loc_ID) REFERENCES Locations (Loc_ID), FOREIGN KEY (Spot_ID) REFERENCES Spots (Spot_ID),"
                "FOREIGN KEY(user_id) REFERENCES Customer (id))"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Guest (guest_id INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, car_plate text, card_number INTERGER)"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS GuestReserv (Reserv_ID INTEGER PRIMARY KEY, Loc_ID INTEGER, Spot_ID INTEGER, guest_id INTEGER, car_plate text, card_number INTERGER, time_slot_start TEXT, time_slot_end TEXT,"
                "FOREIGN KEY (Loc_ID) REFERENCES Locations (Loc_ID), FOREIGN KEY (Spot_ID) REFERENCES Spots (Spot_ID), FOREIGN KEY(guest_id) REFERENCES Guest (guest_id))"
        )
        self.cur.execute("CREATE TABLE IF NOT EXISTS StoreUser (Username TEXT)")
        self.conn.commit()

    #Guest table functions
    def addGuest(self, firstname, lastname, carplate, cardnumber):
        self.cur.execute("INSERT INTO Guest VALUES (NULL, ?, ?, ?, ?)", (firstname, lastname, carplate, cardnumber))
        self.conn.commit()

    def removeGuest(self):
        self.cur.execute("DELETE FROM Guest")
        self.conn.commit()

    def removeGuestID(self, guest_id):
        self.cur.execute("DELETE FROM Guest WHERE guest_id = ?", (guest_id))
        self.conn.commit()

    def getGuestID(self):
        self.cur.execute("SELECT guest_id FROM Guest ORDER BY guest_id DESC LIMIT 1")
        id = self.cur.fetchall()
        return id

    def fetchGuest(self, guest_id):
        self.cur.execute("SELECT * FROM Guest WHERE guest_id = ?", (guest_id,))
        name = self.cur.fetchall()
        return name

    def fetchGuestName(self):
        self.cur.execute("SELECT Reserv_ID, First_Name, Last_Name, Loc_ID, Spot_ID, GuestReserv.car_plate, GuestReserv.card_number, time_slot_start, time_slot_end "
            "FROM GuestReserv INNER JOIN Guest ON Guest.guest_id = GuestReserv.guest_id")
        guestR = self.cur.fetchall()
        return guestR

    def fetchGuestNameID(self, guest_id):
        self.cur.execute("SELECT Reserv_ID, First_Name, Last_Name, Loc_ID, Spot_ID, GuestReserv.car_plate, GuestReserv.card_number, time_slot_start, time_slot_end "
            "FROM GuestReserv INNER JOIN Guest ON Guest.guest_id = GuestReserv.guest_id WHERE GuestReserv.guest_id = ?", (guest_id,))
        guestR = self.cur.fetchall()
        return guestR

    def addGuestRes(self, locID, spot_id, guest_id, guest_plate, guest_card, start_time, end_time):
        self.cur.execute("INSERT INTO GuestReserv VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (locID, spot_id, guest_id, guest_plate, guest_card, start_time, end_time))
        self.conn.commit()

    # store NAME table functions
    def storeName(self, username):
        self.cur.execute("INSERT INTO StoreUser VALUES (?)", (username,))
        self.conn.commit()

    def delName(self):
        self.cur.execute("DELETE FROM StoreUser")
        self.conn.commit()

    def fetchName(self):
        self.cur.execute("SELECT * FROM StoreUser")
        name = self.cur.fetchone()
        return name

    # Customer table functions
    def fetch(self):
        self.cur.execute("SELECT * FROM Customer")
        rows = self.cur.fetchall()
        return rows

    def insert(self, username, password, FirstName, LastName, car_plate, card_number, membership):
        self.cur.execute("INSERT INTO Customer VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, NULL, NULL)",
                         (username, password, FirstName, LastName, car_plate, card_number, membership,))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM Customer WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, username, password, FirstName, LastName, car_plate, card_number, membership):
        self.cur.execute("UPDATE Customer SET username = ?, password = ?, First_Name = ?, Last_Name = ?, car_plate = ?, card_number = ?, membership = ? WHERE id = ?",
                         (username, password, FirstName, LastName, car_plate, card_number, membership, id))
        self.conn.commit()

    def addTempPlate(self, id, temp_plate):
        self.cur.execute("UPDATE Customer SET temp_Plate = ? WHERE id = ?", (temp_plate, id))
        self.conn.commit()

    def addTempCard(self, id, temp_car):
        self.cur.execute("UPDATE Customer SET temp_card_number = ? WHERE id = ?", (temp_car, id))
        self.conn.commit()

    def updateExit(self, username):
        self.cur.execute("UPDATE Customer SET temp_card_number = NULL, temp_Plate = NULL WHERE username = ?",(username))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def findUserId(self, username):
        self.cur.execute("SELECT id FROM Customer WHERE username = ?", (username,))
        ID = self.cur.fetchall()
        return ID

    def find_name(self):
        self.cur.execute("SELECT username FROM Customer")
        rows = self.cur.fetchall()
        return rows

    def find_user_pass(self):
        self.cur.execute("SELECT username, password FROM Customer")
        rows = self.cur.fetchall()
        return rows

    def find_plate(self, username):
        self.cur.execute("SELECT car_plate, temp_Plate FROM Customer WHERE username = ?", (username,))
        plates = self.cur.fetchall()
        return plates

    def find_card(self, username):
        self.cur.execute("SELECT card_number, temp_card_number FROM Customer WHERE username = ?", (username,))
        card = self.cur.fetchall()
        return card

    def getMember(self, username):
        self.cur.execute("SELECT membership FROM Customer WHERE username = ?", (username,))
        memb = self.cur.fetchall()
        return memb


    # Spots and Locations tables functions

    def fetchLoc(self):
        self.cur.execute("SELECT Location_Name FROM Locations")
        loc = self.cur.fetchall()
        return loc

    def fetchLocations(self):
        self.cur.execute("SELECT Spot_ID, Location_Name, Spot_number, Reserved, Cost, time_slot_ava FROM Spots INNER JOIN Locations ON Spots.Loct_ID = Locations.Loc_ID")
        rows = self.cur.fetchall()
        return rows

    def fetchallLoc(self):
        self.cur.execute("SELECT * FROM Spots")
        rows = self.cur.fetchall()
        return rows

    def fetchSpots(self, location_id):
        self.cur.execute("SELECT Spot_ID, Spot_number, Cost, time_slot_ava FROM Spots WHERE Loct_ID = ? AND available = 0", (location_id,))
        spots = self.cur.fetchall()
        return spots

    def fetchNonSpots(self, location_id):
        self.cur.execute("SELECT Spot_ID, Spot_number, Cost, time_slot_ava FROM Spots WHERE Loct_ID = ? AND Reserved = 0 AND available = 0", (location_id,))
        spots = self.cur.fetchall()
        return spots

    def fetchSpotsRes(self, location_id, reserved):
        self.cur.execute("SELECT Spot_ID, Spot_number, Cost, time_slot_ava FROM Spots WHERE Loct_ID = ? AND Reserved = ?", (location_id, reserved))
        spots = self.cur.fetchall()
        return spots

    def addLoc(self, loc, Membership_Cost):
        self.cur.execute("INSERT INTO Locations (Location_Name, Membership_Cost) VALUES (?, ?)",
                         (loc, Membership_Cost))
        self.conn.commit()

    def removeLoc(self, Loc_name):
        self.cur.execute("DELETE FROM Locations WHERE Location_Name=?", (Loc_name,))
        self.conn.commit()

    def addSpots(self, Loc_ID, Spot_num, Reserved, Cost, time_slot_ava, available):
        self.cur.execute("INSERT INTO Spots VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (Loc_ID, Spot_num, Reserved, Cost, time_slot_ava, available))
        self.conn.commit()

    def removeSpots(self, id):
        self.cur.execute("DELETE FROM Spots WHERE Spot_ID=?", (id,))
        self.conn.commit()

    def updateSpots(self, id, Spot_num, Cost, time_slot_ava):
        self.cur.execute("UPDATE Spots SET Spot_number = ?, Cost = ?, time_slot_ava = ? WHERE Spot_ID = ?", (Spot_num, Cost, time_slot_ava, id))
        self.conn.commit()

    def updateSpots(self, id, available):
        self.cur.execute("UPDATE Spots SET available = ? WHERE Spot_ID = ?", (available, id))
        self.conn.commit()

    def findLocId(self,locname):
        self.cur.execute("SELECT Loc_ID FROM Locations WHERE Location_Name = ?", (locname,))
        locID = self.cur.fetchall()
        return locID

    def occupied(self, Spot_ID):
        self.cur.execute("UPDATE Spots SET available = 1 WHERE Spot_ID = ?", (Spot_ID,))
        self.conn.commit()

    # Reservation table functions
    def addReserve(self, Loc_ID, Spot_ID, user_id, car_plate, card_number, time_slot_start, time_slot_end):
        self.cur.execute("INSERT INTO Reservation VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
            (Loc_ID, Spot_ID, user_id, car_plate, card_number, time_slot_start, time_slot_end))
        self.conn.commit()

    def fetchReserv(self):
        self.cur.execute("SELECT * FROM Reservation")
        reser = self.cur.fetchall()
        return reser

    def fetchResNames(self):
        self.cur.execute("SELECT Reserv_ID, Location_Name, Spot_number, First_Name, Last_Name, Reservation.car_plate, Reservation.card_number, time_slot_start, time_slot_end FROM Reservation "
            "INNER JOIN Locations ON Locations.Loc_ID = Reservation.Loc_ID INNER JOIN Spots ON Spots.Spot_ID = Reservation.Spot_ID "
            "INNER JOIN Customer ON Customer.id = Reservation.user_id")
        every = self.cur.fetchall()
        return every

    def fetchResNamesUser(self, user_id):
        self.cur.execute("SELECT Reserv_ID, Location_Name, Spot_number, First_Name, Last_Name, Reservation.car_plate, Reservation.card_number, time_slot_start, time_slot_end FROM Reservation "
            "INNER JOIN Locations ON Locations.Loc_ID = Reservation.Loc_ID INNER JOIN Spots ON Spots.Spot_ID = Reservation.Spot_ID "
            "INNER JOIN Customer ON Customer.id = Reservation.user_id WHERE Reservation.user_id = ?", (user_id,))
        every = self.cur.fetchall()
        return every

    def removeRes(self, Reserv_ID):
        self.cur.execute("DELETE FROM Reservation WHERE Reserv_ID = ? ", (Reserv_ID,))
        self.conn.commit()
