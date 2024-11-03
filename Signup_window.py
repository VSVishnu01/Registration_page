import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector as mysql
import re

# Sign Up Page
class Sign_up:
    
    def __init__(self):
        
        # GUI setup
        self.signup_window = tk.Tk()
        self.signup_window.title('Sign Up')
        self.signup_window.geometry('1142x640+0+0')
        
        # Background image
        try:
            self.bgimage = ImageTk.PhotoImage(file=r'Registration_page/assets/main_background_img.png')
            self.label = tk.Label(self.signup_window, image=self.bgimage)
            self.label.pack()
        except Exception as e:
            print(f"Error loading image: {e}")
        
        # Frame setup
        self.frame = tk.Frame(self.signup_window, background='white')
        self.frame.place(x=647, y=80)
        
        # Labeling
        self.heading = tk.Label(self.frame, text='CREATE NEW ACCOUNT', font=('Calibri', 30, 'bold'), background='white', foreground='firebrick4')
        self.heading.grid(row=0, column=0, padx=10)
        
        # Email Label & Entry
        self.email = tk.Label(self.frame, text='Email', font=('Calibri', 14), background='white', foreground='firebrick4')
        self.email.grid(row=1, column=0, sticky='W', padx=28, pady=(10, 0))
        
        self.email_entry = tk.Entry(self.frame, border=0, background='firebrick4', foreground='white', width=35, font=('Calibri', 14))
        self.email_entry.grid(row=2, column=0, sticky='W', padx=(34, 0))
        
        # Username Label & Entry
        self.username = tk.Label(self.frame, text='Username', font=('Calibri', 14), background='white', foreground='firebrick4')
        self.username.grid(row=3, column=0, sticky='W', padx=28, pady=(10, 0))
        
        self.username_entry = tk.Entry(self.frame, border=0, background='firebrick4', foreground='white', width=35, font=('Calibri', 14))
        self.username_entry.grid(row=4, column=0, sticky='W', padx=(34, 0))
        
        # Password Label & Entry
        self.password = tk.Label(self.frame, text='Password', font=('Calibri', 14), background='white', foreground='firebrick4')
        self.password.grid(row=5, column=0, sticky='W', padx=28, pady=(10, 0))
        
        self.password_entry = tk.Entry(self.frame, border=0, background='firebrick4', foreground='white', width=35, font=('Calibri', 14), show='*')
        self.password_entry.grid(row=6, column=0, sticky='W', padx=(34, 0))
        
        # Confirm Password Label & Entry
        self.cfm_password = tk.Label(self.frame, text='Confirm Password', font=('Calibri', 14), background='white', foreground='firebrick4')
        self.cfm_password.grid(row=7, column=0, sticky='W', padx=28, pady=(10, 0))
        
        self.cfm_password_entry = tk.Entry(self.frame, border=0, background='firebrick4', foreground='white', width=35, font=('Calibri', 14), show='*')
        self.cfm_password_entry.grid(row=8, column=0, sticky='W', padx=(34, 0), pady=(0, 10))
        
        # Terms Checkbutton
        self.check = tk.IntVar()
        self.terms = tk.Checkbutton(self.frame, text='I agree to the Terms & Conditions', font=('Calibri', 12), background='white', activebackground='white', foreground='firebrick4', activeforeground='firebrick4', cursor='hand2', variable=self.check)
        self.terms.grid(row=9, column=0, padx=33, pady=5)
        
        # Signup Button
        self.signup_button = tk.Button(self.frame, text='Signup', font=('Calibri', 26, 'bold'), background='firebrick4', activebackground='firebrick4', foreground='white', activeforeground='white', border=0, width=19, cursor='hand2', command=self.connect_database)
        self.signup_button.grid(row=10, column=0, sticky='W', padx=(35, 0), pady=10)
        
        # Already have an account Label & Button
        self.already_acc = tk.Label(self.frame, text="Already have an account?", font=('Calibri', 12), background='white', foreground='firebrick4')
        self.already_acc.grid(row=11, column=0, sticky='W', padx=(100, 0), pady=10)
        
        self.already_acc_button = tk.Button(self.frame, text='Login', font=('Calibri', 12, 'bold underline'), background='white', activebackground='white', foreground='dodgerblue4', activeforeground='dodgerblue4', border=0, cursor='hand2', command=self.Login_page)
        self.already_acc_button.place(x=269, y=459)
        
        self.signup_window.mainloop()
        
    def Login_page(self):
        self.signup_window.destroy()
        import Signin_window
        Signin_window.Sign_in()
   
    def connect_database(self):
        if not self.validate_inputs():
            return
        
        # Connecting to MySQL database
        try:
            con = mysql.connect(host='localhost', user='root', password='Vis@0105')
            mycursor = con.cursor()
            
            # Check and create database if not exists
            mycursor.execute("CREATE DATABASE IF NOT EXISTS userdata")
            mycursor.execute("USE userdata")
            mycursor.execute("CREATE TABLE IF NOT EXISTS data (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(50), username VARCHAR(100), password VARCHAR(20))")
            
            # Check if username already exists
            mycursor.execute("SELECT * FROM data WHERE username=%s", (self.username_entry.get(),))
            row = mycursor.fetchone()
            
            if row is not None:
                messagebox.showerror('Error', 'Username already exists')
            else:
                # Insert new user details
                mycursor.execute("INSERT INTO data(email, username, password) VALUES(%s, %s, %s)", 
                                 (self.email_entry.get(), self.username_entry.get(), self.password_entry.get()))
                con.commit()
                messagebox.showinfo('Success', 'Registration is successful')
                
                self.clear()
                self.signup_window.destroy()
                self.Login_page()
        
        except mysql.Error as e:
            messagebox.showerror('Error', f'Database Connectivity Issue: {e}')
        
        finally:
            if con.is_connected():
                con.close()
                
    def validate_inputs(self):
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.cfm_password_entry.get()
        
        if not email or not username or not password or not confirm_password:
            messagebox.showerror('Error', 'All fields are required')
            return False
        
        if password != confirm_password:
            messagebox.showerror('Error', 'Password mismatch')
            return False
        
        if self.check.get() == 0:
            messagebox.showerror('Error', 'Please accept Terms & Conditions')
            return False
        
        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror('Error', 'Invalid email format')
            return False
        
        return True
    
    def clear(self):
        self.email_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.cfm_password_entry.delete(0, tk.END)
        self.check.set(0)

if __name__ == '__main__':
    Sign_up()
