from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

root = Tk()
root.geometry("1000x712")
root.title("Admin")
root.iconbitmap(r'D:/amal garage/x.png')
b = ImageTk.PhotoImage(file="D:/amal garage/car2.png")
leb = Label(root, image=b)
leb.place(x=10, y=10, relwidth=1, relheigh=1)

# my_img= ImageTk.PhotoImage(Image.open(""))


class Main:
    def __init__(self, master):
        f1 = Frame(master, borderwidth=5)
        f1.pack(side=TOP)

        def hide_all_frames():
            for tem in f1.winfo_children():
                tem.destroy()
            f1.pack_forget()

        def Print():

            print(emailentry)
            usr = emailentry.get()
            pwd = passentry.get()
            print(usr, pwd)

            if (usr == username and pwd == paswrd):
                hide_all_frames()
                Employee(master)
                Services(master)
                Appointments(master)
                Payments(master)



            else:
                messagebox.showerror("Sign in ", "Invalid Pass or email")
                # Label(f1, text="Invalid email or password").grid(row=7, column=5)
                emailentry.delete(0, END)
                passentry.delete(0, END)

        username = StringVar()
        passward = StringVar()
        username = "a"
        paswrd = "a1"
        l1 = Label(f1, fg="black", text="Admin Panel")
        l1.grid(row=0, column=3, padx=5, pady=10 )
        l2 = Label(f1, fg="blue", text="Sign in")
        l2.grid(row=3, column=5, padx=10, pady=10)
        l3 = Label(f1, fg="blue", text="Email")
        l3.grid(row=4, column=5, padx=10, pady=10)
        l4 = Label(f1, fg="blue", text="Password")
        l4.grid(row=5, column=5, padx=10, pady=10)
        sigbtn = Button(f1, bg="grey", fg="black", text="Sign in", command=Print)
        sigbtn.grid(row=8, column=5, padx=10, pady=10)





        email = StringVar()
        pswrd = StringVar()
        emailentry = Entry(f1, textvariable=email)
        passentry = Entry(f1, textvariable=pswrd)
        emailentry.grid(row=4, column=6, padx=10, pady=10)
        passentry.grid(row=5, column=6, padx=10, pady=10)


m = Main(root)


class Employee:
    def insertdata(self):
        conn = sqlite3.connect("employee data")
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE addresses(
        Name text,
        Cnic integer,
        Experience integer,
        Specification text
        )
        """)
        cur.execute("INSERT INTO addresses VALUES(:self.n_e,:self.n_ex,:self.n_ec, :self.n_es)",
                    {
                        'self.n_e': self.n_e.get(),
                        'self.n_ex': self.n_ex.get(),
                        'self.n_ec': self.n_ec.get(),
                        'self.n_es': self.n_es.get()
                    })
        conn.connect()

    def enterdata(self):
        self.c_win = Toplevel(self.newwindow)
        self.c_win.title("Register or update Employee")
        self.c_win.geometry("733x377")

        self.c_f = Frame(self.c_win)
        self.c_f.grid()

        self.n_leb = Label(self.c_win, text="Enter name:")
        self.n_leb.grid(row=2, column=2, padx=10, pady=10)
        self.n_e = Entry(self.c_win)
        self.n_e.grid(row=2, column=3, padx=10, pady=10)

        self.n_lebex = Label(self.c_win, text="Enter experience:")
        self.n_lebex.grid(row=3, column=2, padx=10, pady=10)
        self.n_ex = Entry(self.c_win)
        self.n_ex.grid(row=3, column=3, padx=10, pady=10)

        self.n_lebc = Label(self.c_win, text="Enter CNIC:")
        self.n_lebc.grid(row=4, column=2, padx=10, pady=10)
        self.n_ec = Entry(self.c_win)
        self.n_ec.grid(row=4, column=3, padx=10, pady=10)

        self.n_lebs = Label(self.c_win, text="Enter specifacation:")
        self.n_lebs.grid(row=5, column=2, padx=10, pady=10)
        self.n_es = Entry(self.c_win)
        self.n_es.grid(row=5, column=3, padx=10, pady=10)

        self.addbtn = Button(self.c_win, text="Add record", command=self.insertdata)
        self.addbtn.grid(row=6, column=4)

    def update(self):
        self.up["state"] = DISABLED
        self.nic = StringVar()
        self.leb = Label(self.f, text="Enter CNIC: ").grid(row=3, column=3, padx=10, pady=10)
        self.cnic = Entry(self.f, textvariable=self.nic)
        self.cnic.grid(row=3, column=4, padx=10, pady=10)
        self.b_cnic = Button(self.f, text="OK", command=self.enterdata)
        self.b_cnic.grid(row=3, column=5, padx=10, pady=10)
        # self.up["state"]= NORMAL

    def create(self):
        self.b_c["state"] = DISABLED
        self.enterdata()

        # self.crebtn= Button(self.c_win, text="OKAY" , command=self.enterdata)
        # self.crebtn.grid(row= 2, column=3)

        print("cre")

        self.b_c["state"] = NORMAL

    def dele(self):
        self.dele["state"] = DISABLED
        print("dek")

        self.nic_d = StringVar()
        self.leb_d = Label(self.f, text="Enter CNIC: ").grid(row=4, column=3, padx=10, pady=10)
        self.cnic_d = Entry(self.f, textvariable=self.nic_d)
        self.cnic_d.grid(row=4, column=4, padx=10, pady=10)
        self.b_d = Button(self.f, text="Delete")
        self.b_d.grid(row=4, column=5, padx=10, pady=10)

        self.dele["state"] = NORMAL

    def viewrec(self):
        self.view["state"] = DISABLED
        print(self.view)
        self.view["state"] = NORMAL

    def nw(self, master):
        self.newwindow = Toplevel(master)
        self.newwindow.title("Employees")
        self.newwindow.geometry("733x377")
        self.f = Frame(self.newwindow)
        self.f.grid()

        self.b_c = Button(self.f, text="Create", command=self.create)
        self.b_c.grid(row=2, column=2, pady=20)
        self.up = Button(self.f, text="Update", command=self.update)
        self.up.grid(row=3, column=2, pady=20)
        self.dele = Button(self.f, text="Delete", command=self.dele)
        self.dele.grid(row=4, column=2, pady=20)
        self.view = Button(self.f, text="View record", command=self.viewrec)
        self.view.grid(row=5, column=2, pady=20)

        Button(self.f, text="Exit", command=self.f.quit).grid(row=6, column=2, pady=20)

    def abas(self):
        self.nw(root)
        self.b["state"] = DISABLED

    def __init__(self, master):
        self.my_frame = Frame(master)
        self.my_frame.pack()
        self.b = Button(master, text="Employee", command=self.abas)
        self.b.pack(pady=20)


class Services:

    def nw(self, master):
        self.s_win = Toplevel(master)
        self.s_win.title("Services")
        self.s_win.geometry("733x377")
        self.f = Frame(self.s_win)
        self.f.pack()

        self.s_btn = Button(self.s_win, text="VIEW", command=view)
        self.s_btn.pack(padx=10, pady=10)

    def abas(self):
        self.nw(root)

    def __init__(self, master):
        Button(master, text="Services", command=self.abas).pack(pady=20)


def view():
    print("ABBAS")


class Payments:
    def __init__(self, master):
        my_me = Frame(master).pack()
        Button(my_me, text="Payments").pack(pady=20)


class Appointments:
    def __init__(self, master):
        Button(master, text="Appointments").pack(pady=20)


root.mainloop()
