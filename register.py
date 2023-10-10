from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\project2\Images_GUI\bgReg.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=100,y=80,width=900,height=580)
        

        # img1=Image.open(r"C:\Users\Admin\Desktop\project2\Images_GUI\reg1.png")
        # img1=img1.resize((600,100),Image.)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=300,y=100, width=500,height=100)
        

        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=130)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=225,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your bestfriends name ","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=100,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=445,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=350)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=375,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=445,width=270)
        
        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=300,y=510,width=270,height=35)


        

    def validate_string(self, string):
        if string.isalpha():
            return True
        else:
            return False
    def reg(self):
        error_messages = []

        if (
            self.var_fname.get() == ""
            or self.var_lname.get() == ""
            or self.var_cnum.get() == ""
            or self.var_email.get() == ""
            or self.var_ssq.get() == "Select"
            or self.var_sa.get() == ""
            or self.var_pwd.get() == ""
            or self.var_cpwd.get() == ""
        ):
            error_messages.append("All Fields Required!")
        if self.var_pwd.get() != self.var_cpwd.get():
            error_messages.append("Please Enter Password & Confirm Password as the Same!")
        if self.var_check.get() == 0:
            error_messages.append("Please Check the Agree Terms and Conditions to proceed!")
        if not self.validate_email(self.var_email.get()):
            error_messages.append("Invalid Email Address!")
        if not self.validate_password(self.var_pwd.get()):
            error_messages.append("Invalid Password! Password must contain at least 8 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        if not self.validate_string(self.var_fname.get()):
            error_messages.append("Invalid First Name! Only alphabetic characters allowed.")
        if not self.validate_string(self.var_lname.get()):
            error_messages.append("Invalid Last Name! Only alphabetic characters allowed.")
        if not self.validate_string(self.var_sa.get()):
            error_messages.append("Invalid Security Answer! Only alphabetic characters allowed.")
        if not self.validate_contact_number(self.var_cnum.get()):
            error_messages.append("Invalid Contact Number! Only integers with 10 digits allowed.")

        if error_messages:
            error_message = "\n".join(error_messages)
            error_label = Label(self.root, text=error_message, font=("times new roman", 12), fg="red")
            error_label.place(x=300, y=560)
            #messagebox.showerror("Error", error_message)
        else:
            try:
                conn = mysql.connector.connect(
                    user="root", password="aditi", host="localhost", database="face_recognition", port=3307
                )
                mycursor = conn.cursor()
                query = "SELECT * FROM regteach WHERE email=%s"
                value = (self.var_email.get(),)
                mycursor.execute(query, value)
                row = mycursor.fetchone()
                if row is not None:
                    error_label = Label(self.root, text="User already exists, please try with another email_id", font=("times new roman", 12), fg="red")
                    error_label.place(x=300, y=560)
                    #messagebox.showerror("Error", "User already exists, please try with another email_id")
                else:
                    mycursor.execute(
                        "INSERT INTO regteach VALUES(%s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_cnum.get(),
                            self.var_email.get(),
                            self.var_ssq.get(),
                            self.var_sa.get(),
                            self.var_pwd.get(),
                        ),
                    )
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully!")
            except Exception as es:
                error_label = Label(self.root, text=f"Due to: {str(es)}", font=("times new roman", 12), fg="red")
                error_label.place(x=300, y=560)
                #messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                    
    def validate_email(self, email):
        pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        if re.match(pattern, email):
            return True
        else:
            return False
    def validate_password(self, password):
        # Password must contain at least 8 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(pattern, password):
            return True
        else:
            return False 
    def validate_contact_number(self, contact_number):
        pattern = r"^(0|91)?[6-9]{1}[0-9]{9}$"  # Regular expression pattern for 10-digit contact number
        if re.match(pattern, contact_number):
            return True
        else:
            return False       
         




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
