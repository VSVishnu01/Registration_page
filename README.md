# Registration Page with CRUD Operations

This project is a GUI-based **Registration Page** developed with Python and Tkinter, featuring **Sign-In** and **Sign-Up** windows. It supports CRUD (Create, Read, Update, Delete) operations for managing user data, stored in a MySQL database.

## Features
- **Sign-In Window**:
  - User login with error handling for invalid inputs.
  - Forgot Password functionality to reset a user's password.
- **Sign-Up Window**:
  - New user registration with validation.
  - Email and username validation.
  - Terms & Conditions checkbox.
  
## Project Structure
- **Signin_window.py**: Contains code for the Sign-In window and Forgot Password functionality.
- **Signup_window.py**: Contains code for the Sign-Up window with validation.
- **assets**: Folder for all image files (backgrounds, icons).

---

## Table of Contents
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Features and Functionality](#features-and-functionality)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Contact](#contact)

---

## Installation

### Prerequisites
- **Python**
- **MySQL Database**
- **PIP** package manager (for dependencies)

### Dependencies
Install the required Python packages:
```bash
pip install tkinter pillow mysql-connector-python
```

## Database Setup

### Update Database Credentials:
- Modify database credentials in both signin.py and signup.py to match your MySQL user setup:
```python
con = mysql.connect(host='localhost', user='your_mysql_user', password='your_mysql_password', database='userdata')
```

## Features and Functionality

### Sign-In Window (`Signin_window.py`)
- **User Login**: Allows users to log in by validating credentials against the database.
- **Forgot Password**: Validates and updates the password securely.

### Sign-Up Window (`Signup_window.py`)
- **New User Registration**: Allows users to create new accounts.
    - **Validations**:
        - Email format.
        - Username availability
        - Password and confirm password match.
        - Acceptance of Terms & Conditions.
- **Database Insertion**: Adds new users to the database upon successful registration.

## File Structure

```plaintext
Registration_Page_Project/
│
├── assets/
│   ├── main_background_img.png
│   ├── forgot_pass_background_img.png
│   ├── closeeye_icon.png
│   ├── openeye_icon.png
│   ├── fb_logo_icon.png
│   ├── x_logo_icon.png
│   └── google_logo_icon.png
│
├── Signin_window.py              # Code for the Sign-In functionality
├── Signup_window.py              # Code for the Sign-Up functionality
└── README.md              # Project documentation
```

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: GUI framework.
- **MySQL**: Database for user data.
- **Pillow**: For handling image assets.

## Contact

**Vishnu VS**  
Email: vishnuvs.dev@gmail.com  
GitHub: [VSVishnu01](https://github.com/VSVishnu01)
