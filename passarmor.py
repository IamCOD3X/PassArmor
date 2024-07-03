#  Program to check the strenght of a given password.

import tkinter as tk

def check_strength():
    password = password_entry.get()
    strength = 0
    
    # Check for length
    if len(password) >= 8:
        strength += 1
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    
    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    
    # Check for special characters
    if any(not char.isalnum() for char in password):
        strength += 1
    
    strength_label.config(text=f"Strength: {strength}/5")

    if strength == 5:
        strength_label.config(fg="green")
    elif strength >= 3:
        strength_label.config(fg="orange")
    else:
        strength_label.config(fg="red")

    if strength == 5:
        suggestion.config(fg="green", text="Your password is strong!")
    elif strength >= 3:
        suggestion.config(fg="orange", text="Your password is moderately strong!")
    else:
        suggestion.config(fg="red", text="Your password is weak! UPDATE NEEDED!")

root = tk.Tk()
root.title("PassArmor")
root.geometry("600x300")
root.resizable(False, False)

# Icon
icon = tk.PhotoImage(file="./assets/icon.png")
root.iconphoto(False, icon)

head= tk.Label(root, text="PassArmor", font=('calibre',20, 'bold'))
head.pack()
subhead = tk.Label(root, text="The password strenght checker", font=('calibre',8))
subhead.pack(pady=15)

password = tk.Label(root, text="Enter Password", font=('Arial', 10, 'bold'))
password.pack(padx=10, pady=5)

password_entry = tk.Entry(root)
password_entry.pack(pady=10)

button = tk.Button(root, text="Check Strength", font=('Arial', 10), command=check_strength)
button.pack(pady=10)

strength_label = tk.Label(root, text="", font=('Arial', 10))
strength_label.pack(pady=10)

suggestion = tk.Label(root, text="", font=('Arial', 10))
suggestion.pack(pady=10)

root.mainloop()
