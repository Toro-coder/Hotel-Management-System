from tkinter import *
from PIL import Image, ImageTk

from customer import cust_win

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry("1280x800+0+0")
        # ==============================image1==========================================================================
        img1 = Image.open(r"C:\Users\cynthia\PycharmProjects\hotel_management\image4.jpg")
        img1 = img1.resize((1280, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1280, height=140)
        # ============================logo image========================================================================
        logoimg = Image.open(r"C:\Users\cynthia\PycharmProjects\hotel_management\logo1.jpg")
        logoimg = logoimg.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(logoimg)

        lbllogo = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbllogo.place(x=0, y=0, width=230, height=140)

        # ============================= Title===========================================================================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", bd=4, bg="black", font=("Time New Roman", 40,
                                                                                             "bold"), fg="gold",
                          relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1280, height=50)

        # ==========================main frame==========================================================================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1280, height=620)

        # =============================Menu===========================================================================
        lbl_menu = Label(main_frame, text="MENU", bd=4, bg="black", font=("Time New Roman", 20, "bold"), fg="gold",
                         relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ========================button frame=======================================================================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, command=self.cust_details, text="CUSTOMER", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black",
                             fg="gold", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        # ==============================Right image=====================================================================
        img2 = Image.open(r"C:\Users\cynthia\PycharmProjects\hotel_management\image1.jpg")
        img2 = img2.resize((1040, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        lblimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1040, height=590)

        # ==============================Down image=====================================================================
        img3 = Image.open(r"C:\Users\cynthia\PycharmProjects\hotel_management\food1.jpg")
        img3 = img3.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=225, width=230, height=210)

        img4 = Image.open(r"C:\Users\cynthia\PycharmProjects\hotel_management\food2.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img4)

        lblimg = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=420, width=230, height=210)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = cust_win(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
