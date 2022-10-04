import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql


class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1040x550+230+220")
        self.root.resizable(False, False)

        # ==================variables===================================================================
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # ====================Title======================================================================
        lbl_title = Label(self.root, text="ADD CUSTOMERS DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold")
        lbl_title.place(x=0, y=0, width=1040, height=50)

        # =================logo========================================================================
        logo = Image.open(r"C:\Users\cynthia\PycharmProjects\hotel_management\logo1.jpg")
        logo = logo.resize((100, 40), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(logo)

        lblimg = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # =====================labelFrame================================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("arial", 12, "bold"),
                                    padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ===========================labels and entries =============================================
        # customer ref
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, font=("arial", 13, "bold"), width=29,
                              state="readonly")
        entry_ref.grid(row=0, column=1)

        # customer  name
        lbl_cust_name = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)

        entry_cname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, font=("arial", 13, "bold"), width=29)
        entry_cname.grid(row=1, column=1)

        # mother's name
        lbl_mother_name = Label(labelframeleft, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mother_name.grid(row=2, column=0, sticky=W)

        entry_mname = ttk.Entry(labelframeleft, textvariable=self.var_mother, font=("arial", 13, "bold"), width=29)
        entry_mname.grid(row=2, column=1)

        # gender
        lbl_gender = Label(labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27,
                                    state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Postcode
        lbl_postcode = Label(labelframeleft, text="Postcode:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=4, column=0, sticky=W)

        entry_postcode = ttk.Entry(labelframeleft, textvariable=self.var_post, font=("arial", 13, "bold"), width=29)
        entry_postcode.grid(row=4, column=1)

        # mobile
        lbl_mobile = Label(labelframeleft, text="Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=5, column=0, sticky=W)

        entry_mobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29)
        entry_mobile.grid(row=5, column=1)

        # email
        lbl_email = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)

        entry_email = ttk.Entry(labelframeleft, textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        entry_email.grid(row=6, column=1)

        # nationality
        lbl_nationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"),
                                         width=27, state="readonly")
        combo_nationality["values"] = ("Kenya", "America", "British")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # id proof type
        lbl_id_type = Label(labelframeleft, text="Id Proof Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_id_type.grid(row=8, column=0, sticky=W)

        combo_id_type = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"),
                                     width=27, state="readonly")
        combo_id_type["values"] = ("Kenyan ID", "Driving License", "Passport")
        combo_id_type.current(0)
        combo_id_type.grid(row=8, column=1)

        # id number
        lbl_id = Label(labelframeleft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_id.grid(row=9, column=0, sticky=W)

        entry_id = ttk.Entry(labelframeleft, textvariable=self.var_id_number, font=("arial", 13, "bold"), width=29)
        entry_id.grid(row=9, column=1)

        # address
        lbl_address = Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)

        entry_address = ttk.Entry(labelframeleft, textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        entry_address.grid(row=10, column=1)

        # =====================btn frame and the buttons==============================================================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btn_add = Button(btn_frame, command=self.add_data, text="Add", font=("arial", 11, "bold"), bd=4, bg="black",
                         fg="gold", width=10)
        btn_add.grid(row=0, column=0)

        btn_update = Button(btn_frame, command=self.update, text="Update", font=("arial", 11, "bold"), bd=4, bg="black",
                            fg="gold", width=10)
        btn_update.grid(row=0, column=1)

        btn_delete = Button(btn_frame, command=self.xdelete, text="Delete", font=("arial", 11, "bold"), bd=4,
                            bg="black", fg="gold", width=10)
        btn_delete.grid(row=0, column=2)

        btn_reset = Button(btn_frame, command=self.reset, text="Reset", font=("arial", 11, "bold"), bd=4, bg="black",
                           fg="gold", width=10)
        btn_reset.grid(row=0, column=3)

        # ===========================Table========================================================================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                                 font=("arial", 12, "bold"))
        table_frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(table_frame, text="Search By:", font=("arial", 12, "bold"), bg="maroon", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.var_search = StringVar()
        combo_search = ttk.Combobox(table_frame, font=("arial", 12, "bold"), textvariable=self.var_search, width=14,
                                    state="readonly")
        combo_search["values"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.var_txtsearch = StringVar()
        textSearch = ttk.Entry(table_frame, textvariable=self.var_txtsearch, font=("arial", 13, "bold"), width=16)
        textSearch.grid(row=0, column=2, padx=2)

        btn_search = Button(table_frame, command=self.search, text="Search", font=("arial", 11, "bold"), bd=4,
                            bg="black", fg="gold",
                            width=8)
        btn_search.grid(row=0, column=3, padx=1)

        btn_showAll = Button(table_frame, command=self.fetch_data, text="Show All", font=("arial", 11, "bold"), bd=4,
                             bg="black", fg="gold",
                             width=8)
        btn_showAll.grid(row=0, column=4, padx=1)

        # =======================Show Table===========================================================================
        details_table = Frame(table_frame, bd=4, relief=RIDGE)
        details_table.place(x=0, y=50, width=900, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_Details_table = ttk.Treeview(details_table, column=("ref", "name", "mother", "gender", "post",
                                                                      "mobile", "email", "nationality", "idproof",
                                                                      "idnumber", "address"),
                                               xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_Details_table.xview)
        scroll_y.config(command=self.cust_Details_table.yview)

        self.cust_Details_table.heading("ref", text="Refer No")
        self.cust_Details_table.heading("name", text="Name")
        self.cust_Details_table.heading("mother", text="Mother Name")
        self.cust_Details_table.heading("gender", text="Gender")
        self.cust_Details_table.heading("post", text="PostCode")
        self.cust_Details_table.heading("mobile", text="Mobile")
        self.cust_Details_table.heading("email", text="Email")
        self.cust_Details_table.heading("nationality", text="Nationality")
        self.cust_Details_table.heading("idproof", text="Id Proof")
        self.cust_Details_table.heading("idnumber", text="Id Number")
        self.cust_Details_table.heading("address", text="Address")

        self.cust_Details_table["show"] = "headings"

        self.cust_Details_table.column("ref", width=80)
        self.cust_Details_table.column("name", width=80)
        self.cust_Details_table.column("mother", width=80)
        self.cust_Details_table.column("gender", width=80)
        self.cust_Details_table.column("post", width=80)
        self.cust_Details_table.column("mobile", width=80)
        self.cust_Details_table.column("email", width=80)
        self.cust_Details_table.column("nationality", width=80)
        self.cust_Details_table.column("idproof", width=80)
        self.cust_Details_table.column("idnumber", width=80)
        self.cust_Details_table.column("address", width=80)

        self.cust_Details_table.pack(fill=BOTH, expand=1)
        self.cust_Details_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_ref.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error!!", "All fields are required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showerror("success", "customer has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showinfo("Error", f"something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customers")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.cust_Details_table.delete(*self.cust_Details_table.get_children())
            for i in row:
                self.cust_Details_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        row_cursor = self.cust_Details_table.focus()
        content = self.cust_Details_table.item(row_cursor)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]),

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("error!!", "please enter your mobile number", parent=self.root)
        else:
            conn = pymysql.connect(host="localhost", user="root", password="", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customers set name=%s,mother=%s,gender=%s,post=%s,mobile=%s,email=%s,"
                              "nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s", (
                                  self.var_cust_name.get(),
                                  self.var_mother.get(),
                                  self.var_gender.get(),
                                  self.var_post.get(),
                                  self.var_mobile.get(),
                                  self.var_email.get(),
                                  self.var_nationality.get(),
                                  self.var_id_proof.get(),
                                  self.var_id_number.get(),
                                  self.var_address.get(),
                                  self.var_ref.get(),
                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("updated!!", "update successfull", parent=self.root)

    def xdelete(self):
        xdelete = messagebox.askyesno("hotel management system", "do you want to delete this customer?",
                                      parent=self.root)
        if xdelete > 0:
            conn = pymysql.connect(host="localhost", user="root", password="", database="management")
            my_cursor = conn.cursor()
            query = "delete from customers where ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not xdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set("")
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set(""),
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customers where" + str(self.var_search.get()) + "LIKE '%"
                          + str(self.var_txtsearch.get()) + "%'")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.cust_Details_table.delete(*self.cust_Details_table.get_children())
            for i in row:
                self.cust_Details_table.insert("", END, values=i)
                conn.commit()
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = cust_win(root)
    root.mainloop()
