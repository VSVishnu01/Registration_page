import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector as mysql

class Sign_in:
    
    def __init__(self):
        self.bgimage = None
        self.login_window = tk.Tk()
        self.login_window.title('Sign In')
        self.login_window.resizable(0,0)
        self.login_window.geometry('1142x640+0+0')
        
        self.setup_ui()
        self.login_window.mainloop()

    def setup_ui(self):
        try:
            self.bgimage = ImageTk.PhotoImage(file=r"Registration_page/assets/main_background_img.png")
            tk.Label(self.login_window, image=self.bgimage).pack()
        except Exception as e:
            print(f"Background image error: {e}")
        
        # Create the login form elements
        self.create_heading()
        self.create_entries()
        self.create_buttons()

    def create_heading(self):
        heading = tk.Label(self.login_window, 
                           text='USER LOGIN', 
                           font=('Calibri', 40, 'bold'), 
                           background='white', 
                           foreground='firebrick4')
        heading.place(x=725, y=90)

    def create_entries(self):
        # Username Entry
        self.username_entry = self.create_entry("Username", 190)
        self.username_entry.bind('<FocusIn>', self.clear_username_placeholder)
        self.username_entry.bind('<FocusOut>', self.set_username_placeholder)

        # Password Entry
        self.password_entry = self.create_entry("Password", 260, show='*')
        self.password_entry.bind('<FocusIn>', self.clear_password_placeholder)
        self.password_entry.bind('<FocusOut>', self.set_password_placeholder)

        # Eye button for toggling password visibility
        self.setup_eye_button()

    def create_entry(self, placeholder, y, show=None):
        entry = tk.Entry(self.login_window, 
                         font=('Calibri', 18), 
                         background='white', 
                         foreground='firebrick4', 
                         border=0, 
                         width=26,
                         show=show)
        entry.place(x=700, y=y)
        entry.insert(0, placeholder)
        self.create_underline(y + 30)
        return entry

    def create_underline(self, y):
        tk.Frame(self.login_window, 
                 width=315, 
                 height=2,
                 background='firebrick4').place(x=700, y=y)

    def clear_username_placeholder(self, event):
        if self.username_entry.get() == "Username":
            self.username_entry.delete(0, tk.END)

    def set_username_placeholder(self, event):
        if not self.username_entry.get():
            self.username_entry.insert(0, "Username")

    def clear_password_placeholder(self, event):
        if self.password_entry.get() == "Password":
            self.password_entry.delete(0, tk.END)
            self.password_entry.config(show="*")

    def set_password_placeholder(self, event):
        if not self.password_entry.get():
            self.password_entry.insert(0, "Password")
            self.password_entry.config(show="")

    def setup_eye_button(self):
        try:
            self.closeeye = tk.PhotoImage(file=r"Registration_page/assets/closeeye_icon.png")
            self.openeye = tk.PhotoImage(file=r"Registration_page/assets/openeye_icon.png")
            
            self.eye_button = tk.Button(self.login_window,
                                        image=self.closeeye, 
                                        border=0, 
                                        background='white',
                                        activebackground='white',
                                        cursor='hand2', 
                                        command=lambda: self.toggle_password)
            self.eye_button.place(x=990, y=270)
        except Exception as e:
            print(f"Eye icon error: {e}")

    def toggle_password(self):
        if self.password_entry.cget('show') == '':
            self.password_entry.config(show='*')
            self.eye_button.config(image=self.closeeye)
        else:
            self.password_entry.config(show='')
            self.eye_button.config(image=self.openeye)

    def create_buttons(self):
        self.create_login_button()
        self.create_social_buttons()
        self.create_account_buttons()
        self.forgot_password_button()

    def forgot_password_button(self):
        forgot_pass_button=tk.Button(self.login_window,
                                      text='Forgot Password?', 
                                      font=('Calibri', 12),
                                      border=0, 
                                      background='white',
                                      foreground='firebrick4',
                                      activebackground='white',
                                      activeforeground='firebrick4',
                                      cursor='hand2' ,
                                      command=lambda: self.forgot_password()
                                      )
        forgot_pass_button.place(x=895, y=295)


    def create_login_button(self):
        login_bt = tk.Button(self.login_window,
                             text='Login', 
                             font=('Calibri', 26, 'bold'),
                             border=0, 
                             background='firebrick4',
                             foreground='white',
                             activebackground='firebrick4',
                             activeforeground='white',
                             cursor='hand2',
                             padx=107,
                             command=self.login_user)
        login_bt.place(x=700, y=330)

        or_label = tk.Label(self.login_window, 
                            text=' - - - - - - - - - - - - OR - - - - - - - - - - - -', 
                            font=('Calibri', 18, 'bold'), 
                            background='white',
                            foreground='firebrick4')
        or_label.place(x=690, y=410)

    def create_social_buttons(self):
        try:
            self.facebook_logo = tk.PhotoImage(file=r"Registration_page/assets/fb_logo_icon.png")
            self.x_logo = tk.PhotoImage(file=r"Registration_page/assets/x_logo_icon.png")
            self.google_logo = tk.PhotoImage(file=r"Registration_page/assets/google_logo_icon.png")
            
            tk.Label(self.login_window, 
                     image=self.facebook_logo, 
                     background='white', 
                     cursor='hand2').place(x=745, y=455)
            
            tk.Label(self.login_window, 
                     image=self.x_logo, 
                     background='white', 
                     cursor='hand2').place(x=830, y=455)
            
            tk.Label(self.login_window, 
                     image=self.google_logo, 
                     background='white', 
                     cursor='hand2').place(x=915, y=455)
        except Exception as e:
            print(f"Social icons error: {e}")

    def create_account_buttons(self):
        signup_label = tk.Label(self.login_window, 
                                text="Don't have an account?", 
                                font=('Calibri', 12), 
                                background='white',
                                foreground='firebrick4')
        signup_label.place(x=707, y=530)

        newacc_bt = tk.Button(self.login_window,
                              text='Create New Account', 
                              font=('Calibri', 12, 'bold underline'),
                              border=0, 
                              background='white',
                              foreground='dodgerblue4',
                              activebackground='white',
                              activeforeground='dodgerblue4',
                              cursor='hand2',
                              command=lambda: self.signup_page())
        newacc_bt.place(x=862, y=528)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == 'Username' or password == 'Password' or not username or not password:
            messagebox.showerror('Error', 'All fields are required')
            return
        
        try:
            con = mysql.connect(host='localhost', user='root', password='Vis@0105', database='userdata')
            mycursor = con.cursor()
            query = 'SELECT * FROM data WHERE username=%s AND password=%s'
            mycursor.execute(query, (username, password))
            row = mycursor.fetchone()
            
            if row:
                messagebox.showinfo('Welcome', 'Login Successfully')
            else:
                messagebox.showerror('Error', 'Incorrect Username or Password')
        except mysql.Error as e:
            messagebox.showerror('Error', f'Database error: {e}')
        finally:
            con.close()

    def forgot_password(self):
        # Create new window for password reset
        replace_window = tk.Toplevel(self.login_window)
        replace_window.title('Change Password')
        replace_window.geometry('1142x640+0+0')
        
        self.reset_bgimage = ImageTk.PhotoImage(file='Registration_page/assets/forgot_pass_background_img.png')
        tk.Label(replace_window, image=self.reset_bgimage).pack()
        
        frame = tk.Frame(replace_window, background='white', width=50)
        frame.place(x=370, y=90)
        self.create_password_reset_form(frame, replace_window)
        
        replace_window.mainloop()

    def create_password_reset_form(self, frame, parent):
        # Create reset password form
        tk.Label(frame, text='Reset Password', font=('Calibri', 40, 'bold'), foreground='firebrick4', background='white').grid(row=0, column=0)
        fields = [('Username', 1, 3), ('New Password', 4, 6), ('Confirm Password', 7, 9)]
        entries = {}

        for text, row, frame_row in fields:
            tk.Label(frame, text=text, font=('Calibri', 18), foreground='firebrick4', background='white').grid(row=row, column=0, sticky='W', padx=10, pady=(10, 0))
            entry = tk.Entry(frame, font=('Calibri', 18), foreground='firebrick4', background='white', border=0, width=30)
            entry.grid(row=row+1, column=0, sticky='W', padx=(15, 0), pady=(8, 0))
            entries[text.lower()] = entry
            
            tk.Frame(frame, background='firebrick4', width=365, height=2,).grid(row=frame_row, column=0, sticky='W', padx=(15, 0))

        tk.Button(frame, text='Submit', font=('Calibri', 26, 'bold'), foreground='white', background='firebrick4', width=18,
                  command=lambda: self.reset_password(entries, parent)).grid(row=10, column=0, padx=(12, 0), pady=(20, 0))
    
    def reset_password(self, entries, parent):
        username = entries['username'].get()
        new_password = entries['new password'].get()
        confirm_password = entries['confirm password'].get()

        if not all([username, new_password, confirm_password]):
            messagebox.showerror('Error', 'All fields are required', parent=parent)
            return
        
        if new_password != confirm_password:
            messagebox.showerror('Error', 'Passwords do not match', parent=parent)
            return

        try:
            con = mysql.connect(host='localhost', user='root', password='Vis@0105', database='userdata')
            mycursor = con.cursor()
            mycursor.execute('SELECT * FROM data WHERE username=%s', (username,))
            if mycursor.fetchone() is None:
                messagebox.showerror('Error', 'Username does not exist', parent=parent)
            else:
                mycursor.execute('UPDATE data SET password=%s WHERE username=%s', (new_password, username))
                con.commit()
                messagebox.showinfo('Success', 'Password updated successfully', parent=parent)
        except mysql.Error as err:
            print(f"Error: {err}")
            messagebox.showerror('Error', 'Unable to update password. Please try again later.', parent=parent)
        finally:
            if con:
                con.close()
                parent.destroy()
                
    def signup_page(self):
        self.login_window.destroy()
        import Signin_window
        Signin_window.Sign_up()

if __name__ == '__main__':
    Sign_in()