import tkinter as tk
from tkinter import messagebox

CREDENTIALS_FILE = "credentials.txt"

# File read Sign In function
def sign_in():
    user = signin_username.get()
    pwd = signin_password.get()

    if not user or not pwd:
        messagebox.showwarning("Error", "Please fill in both fields.")
        return

    try:
        with open(CREDENTIALS_FILE, "r") as f:
            lines = [line.strip().split(",") for line in f if line.strip()]
    except FileNotFoundError:
        lines = []

    if [user, pwd] in lines:
        messagebox.showinfo("Success", f"Welcome, {user}!")
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password.")


# File write Sign Up function
def sign_up():
    user = signup_username.get()
    pwd = signup_password.get()

    if not user or not pwd:
        messagebox.showwarning("Error", "Please fill in both fields.")
        return

    with open(CREDENTIALS_FILE, "a") as f:
        f.write(f"{user},{pwd}\n")

    messagebox.showinfo("Success", "Account created! Please sign in.")
    sign_in_window()


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# sign in window
def sign_in_window():
    global signin_username, signin_password
    clear_window()

    tk.Label(root, text="Sign In", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    signin_username = tk.Entry(root)
    signin_username.pack()

    tk.Label(root, text="Password").pack()
    signin_password = tk.Entry(root, show="*")
    signin_password.pack()

    tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)
    tk.Button(root, text="Need an account? Sign Up", command=sign_up_window).pack()


# sign up window
def sign_up_window():
    global signup_username, signup_password
    clear_window()

    tk.Label(root, text="Sign Up", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    signup_username = tk.Entry(root)
    signup_username.pack()

    tk.Label(root, text="Password").pack()
    signup_password = tk.Entry(root, show="*")
    signup_password.pack()

    tk.Button(root, text="Sign Up", command=sign_up).pack(pady=5)
    tk.Button(root, text="Already have an account? Sign In", command=sign_in_window).pack()


# main menu window
def main_menu():
    clear_window()

    tk.Label(root, text="Main Menu", font=("Arial", 14)).pack(pady=20)
    tk.Label(root, text="You are logged in!").pack(pady=10)
    tk.Button(root, text="Log Out", command=sign_in_window).pack(pady=10)


# root window
root = tk.Tk()
root.title("Application")
root.geometry("300x200")
sign_in_window()

root.mainloop()