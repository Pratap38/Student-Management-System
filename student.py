from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql


class std():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        
        self.root.config(bg="#2c3e50")

        title = Label(self.root, text="Student Record System", font=("times new roman", 40, "bold"), bg="#e25454", fg="#9EDECF", bd=4, relief=RIDGE)
        title.pack(side=TOP, fill=X)

        option_frame = Frame(self.root, bd=5, relief="ridge", bg=self.clr(230, 150, 200))

        option_frame.place(x=50, y=100, width=self.width / 3, height=self.height - 180)

        self.detail_frame = Frame(self.root, bd=5, relief=RIDGE, bg=self.clr(150, 230, 120))
        self.detail_frame.place(x=self.width / 3 + 100, y=100, width=self.width / 2 + 50, height=self.height - 180)

        buttn_1 = Button(option_frame, text="Add Student", command=self.add_frame_func, font=("times new roman", 20, "bold"), bg="purple", activebackground="#c0392b", width=20, fg="light gray", bd=3, relief="raised")
        buttn_1.grid(row=0, column=0, padx=30, pady=23)


        buttn_2 = Button(option_frame, text="Search Student", command=self.search_frame_func, font=("times new roman", 20, "bold"), bg="purple", activebackground="#c0392b", width=20, fg="light gray", bd=3, relief="raised")
        buttn_2.grid(row=1, column=0, padx=30, pady=23)

        buttn_3 = Button(option_frame, text="Update Student",command=self.update_data, font=("times new roman", 20, "bold"), bg="purple", activebackground="#c0392b", width=20, fg="light gray", bd=3, relief="raised")
        buttn_3.grid(row=2, column=0, padx=30, pady=25)

        buttn_4 = Button(option_frame, text="Delete Student",command=self.remove_student, font=("times new roman", 20, "bold"), bg="purple", activebackground="#c0392b", width=20, fg="light gray", bd=3, relief="raised")
        buttn_4.grid(row=3, column=0, padx=30, pady=25)

        buttn_5 = Button(option_frame, text="showall", command=self.showll, font=("times new roman", 20, "bold"), bg="purple", activebackground="#c0392b", width=20, fg="light gray", bd=3, relief="raised")
        buttn_5.grid(row=4, column=0, padx=30, pady=25)

        record_detail = Label(self.detail_frame, text="Record Details", font=("times new roman", 30, "bold"), bg=self.clr(150, 230, 120), fg="black")
        record_detail.pack(side=TOP, fill=X)
        self.tab_function()

    def tab_function(self):
        tab_frame = Frame(self.detail_frame, bd=5, relief="sunken", bg="Brown")
        tab_frame.place(x=23, y=80, width=self.width / 2, height=self.height - 280)

        x_scroll = Scrollbar(tab_frame, orient=HORIZONTAL)
        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll = Scrollbar(tab_frame, orient=VERTICAL)
        y_scroll.pack(side=RIGHT, fill=Y)
        self.table = Treeview(tab_frame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, columns=("Roll", "Name", "Fname", "Sub", "Grade"), height=10)
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)
        self.table.heading("Roll", text="Roll No")
        self.table.heading("Name", text="Name")
        self.table.heading("Fname", text="Father Name")
        self.table.heading("Sub", text="Subject")
        self.table.heading("Grade", text="Grade")
        self.table["show"] = "headings"
        self.table.pack(fill=BOTH, expand=1)

    def add_frame_func(self):
        self.add_frame = Frame(self.root, bd=5, relief=RIDGE, bg=self.clr(150, 230, 120))
        self.add_frame.place(x=self.width / 3 + 80, y=100, width=self.width / 3, height=self.height - 220)

        title = Label(self.add_frame, text="Add Student Details", font=("times new roman", 25, "bold"), bg=self.clr(150, 230, 120), fg="black")
        title.grid(row=0, column=0, columnspan=2, pady=10)

        label1 = Label(self.add_frame, text="Roll No", font=("times new roman", 20, "bold"), bg=self.clr(150, 230, 120), fg="black")
        label1.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.roll_no = Entry(self.add_frame, font=("times new roman", 18), bd=3, relief=RIDGE,width=17)
        self.roll_no.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        label2 = Label(self.add_frame, text="Name", font=("times new roman", 20, "bold"), bg=self.clr(150, 230, 120), fg="black")
        label2.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.name = Entry(self.add_frame, font=("times new roman", 18), bd=3, relief=RIDGE,width=17)
        self.name.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        label3 = Label(self.add_frame, text="Father Name", font=("times new roman", 20, "bold"), bg=self.clr(150, 230, 120), fg="black")
        label3.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.father_name = Entry(self.add_frame, font=("times new roman", 18), bd=3, relief=RIDGE)
        self.father_name.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        label4 = Label(self.add_frame, text="Subject", font=("times new roman", 20, "bold"), bg=self.clr(150, 230, 120), fg="black")
        label4.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.subject = Entry(self.add_frame, font=("times new roman", 18), bd=3, relief=RIDGE)
        self.subject.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        label5 = Label(self.add_frame, text="Grade", font=("times new roman", 20, "bold"), bg=self.clr(150, 230, 120), fg="black")
        label5.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.grade = Entry(self.add_frame, font=("times new roman", 18), bd=3, relief=RIDGE)
        self.grade.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        save_btn = Button(self.add_frame, text="Save", command=self.save_data, font=("times new roman", 20, "bold"), bg="green", fg="white", bd=3, relief=RAISED)
        save_btn.grid(row=6, column=0, columnspan=2, pady=20)

        exit_btn=Button(self.add_frame,text="X",width=1,command=self.destory_Add,font=("times new roman",20,"bold"),bg="green",fg="black",relief=RAISED,bd=1)
        exit_btn.grid(row=0,column=5)

    def search_frame_func(self):
        self.add_frame = Frame(self.root, bd=5, relief=RIDGE, bg=self.clr(150, 230, 120))
        self.add_frame.place(x=self.width / 3 + 80, y=100, width=self.width / 3, height=self.height - 350)

        label11 = Label(self.add_frame, text="Select:", font=("times new roman", 20, "bold"), bg=self.clr(150, 230, 120), fg="black")
        label11.grid(row=0, column=0, padx=20, pady=20)
        self.combo = Combobox(self.add_frame, font=("times new roman", 18), width=17, values=("rollNo", "name", "fname", "subject"))
        self.combo.set("select option")
        self.combo.grid(row=0, column=1, padx=10, pady=30)

        value2 = Label(self.add_frame, text="Value (rollno, name)", font=("times new roman", 20, "bold"), width=18, bg=self.clr(150, 230, 120), fg="black")
        value2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.value = Entry(self.add_frame, font=("times new roman", 18), width=17,bd=3, relief=RIDGE)
        self.value.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        save_btn = Button(self.add_frame, text="Search", command=self.search_function, font=("times new roman", 20, "bold"), bg="green", fg="white", bd=3, relief=RAISED)
        save_btn.grid(row=3, column=0, columnspan=2, pady=20)

    def search_function(self):
        search_by = self.combo.get()
        value = self.value.get()

        if not search_by or value == "" or search_by == "select option":
            messagebox.showerror("Error", "Please select a valid field and provide a value to search.")
            return

        try:
            self.database_func()

            if search_by == "rollNo":
                try:
                    value = int(value)  
                except ValueError:
                    messagebox.showerror("Error", "Roll number must be an integer.")
                    return

                query = f"SELECT * FROM student WHERE {search_by} = %s"
                self.cursor.execute(query, (value,))
            else:
                query = f"SELECT * FROM student WHERE {search_by} = %s"
                self.cursor.execute(query, (value,))

            rows = self.cursor.fetchall()
            self.connection.close()

            if rows:
                self.table.delete(*self.table.get_children())
                for row in rows:
                    self.table.insert("", "end", values=row)
                self.destory_Add()
            else:
                messagebox.showinfo("No Results", "No matching records found.")

        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def save_data(self):
        roll = self.roll_no.get()
        name = self.name.get()
        father = self.father_name.get()
        subject = self.subject.get()
        grade = self.grade.get()

        if roll == "" or name == "" or father == "" or subject == "" or grade == "":
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            roll = int(roll)
            self.database_func()
            self.cursor.execute("INSERT INTO student (rollNo, name, fname, subject, grade) VALUES (%s, %s, %s, %s, %s)", (roll, name, father, subject, grade))
            self.connection.commit()
            messagebox.showinfo("Success", f"Student {name} with Roll No {roll} added successfully")

            self.cursor.execute("SELECT * FROM student WHERE rollNo=%s", (roll,))
            rows = self.cursor.fetchone()
            self.table.insert("", "end", values=rows)
            self.connection.close()
            self.destory_Add()

        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")
    def update_data(self):
        self.add_frame = Frame(self.root, bd=5, relief=RIDGE, bg=self.clr(150, 230, 120))
        self.add_frame.place(x=self.width / 3 + 80, y=100, width=self.width / 3, height=self.height - 300)

        label111 = Label(self.add_frame, text="Select:", font=("times new roman", 20, "bold"), bg=self.clr(150, 230, 120), fg="black")
        label111.grid(row=0, column=0, padx=20, pady=20)
        self.combo = Combobox(self.add_frame, font=("times new roman", 18), width=17, values=( "name",  "subject","grade"))
        self.combo.set("select option")
        self.combo.grid(row=0, column=1, padx=10, pady=30)

       

        value23 = Label(self.add_frame, text="New value", font=("times new roman", 20, "bold"), width=16, bg=self.clr(150, 230, 120), fg="black")
        value23.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.value = Entry(self.add_frame, font=("times new roman", 18), width=17,bd=3, relief=RIDGE)
        self.value.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        value22 = Label(self.add_frame, text="RollNo:", font=("times new roman", 20, "bold"), width=16, bg=self.clr(150, 230, 120), fg="black")
        value22.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.rol = Entry(self.add_frame, font=("times new roman", 18), bd=3,width=17, relief=RIDGE)
        self.rol.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        

        save_btn = Button(self.add_frame, text="update", command=self.update_function, font=("times new roman", 20, "bold"), bg="green", fg="white", bd=3, relief=RAISED)
        save_btn.grid(row=3, column=0, columnspan=2, pady=25,padx=20)

        
        
    def update_function(self):
        options=self.combo.get()
        val=self.value.get()
        rl= int(self.rol.get())
        try:
            self.database_func()
            self.cursor.execute(f"UPDATE student SET {options} = %s WHERE rollNo = %s", (val, rl))  
            self.connection.commit()
            messagebox.showinfo("Success", f"Student with Roll No {rl} updated successfully")
            self.destory_Add()
            self.cursor.execute("SELECT * FROM student WHERE rollNo=%s", (rl,))
            rows = self.cursor.fetchone()
            self.table.delete(*self.table.get_children())
            self.table.insert("", "end", values=rows)
            self.connection.close()



        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")


            return
        

    def showll(self):
        try:
            self.database_func()
            self.cursor.execute("SELECT * FROM student")
            rows = self.cursor.fetchall()
            self.connection.close()

            if rows:
                self.table.delete(*self.table.get_children())
                for row in rows:
                    self.table.insert("", "end", values=row)
                self.destory_Add()
            else:
                messagebox.showinfo("No Results", "No records found.")



        
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def remove_student(self):

        self.add_frame = Frame(self.root, bd=5, relief=RIDGE, bg=self.clr(150, 230, 120))
        self.add_frame.place(x=self.width / 3 + 80, y=100, width=self.width / 3, height=self.height - 400)

        

        label1 = Label(self.add_frame, text="Roll No", font=("times new roman", 20, "bold"), bg=self.clr(150, 230, 120), fg="black")
        label1.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.roll_no = Entry(self.add_frame, font=("times new roman", 18), bd=3, relief=RIDGE)
        self.roll_no.grid(row=1, column=1, padx=20, pady=10, sticky="w")

       
        save_btn = Button(self.add_frame, text="Save", command=self.remove_funct, font=("times new roman", 20, "bold"), bg="green", fg="white", bd=3, relief=RAISED)
        save_btn.grid(row=4, column=0, columnspan=2, pady=20)
    def remove_funct(self):
        rolll= int(self.roll_no.get())
        try:
            self.database_func()
            self.cursor.execute("delete from student where rollNo=%s",rolll)
            self.connection.commit()
            messagebox.showinfo("sucess",f"student with rollno{rolll}")
            self.destory_Add()
            self.connection.commit()


        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")

        

    def destory_Add(self):
        if hasattr(self, 'add_frame'):
            self.add_frame.destroy()

    def database_func(self):
        self.connection = pymysql.connect(host="localhost", user="root", password="****", database="students")
        self.cursor = self.connection.cursor()

    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"


root = Tk()
obj = std(root)
root.mainloop()
