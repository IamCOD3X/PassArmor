# PassArmor

**PassArmor** is a simple yet effective password strength checker built using Python and Tkinter. It evaluates the strength of a given password based on its length, the inclusion of uppercase letters, lowercase letters, digits, and special characters.

## Features

- **Password Strength Evaluation**: Checks password strength on a scale of 0 to 5.
- **Visual Feedback**: Displays strength status with color-coded text (red for weak, orange for moderate, green for strong).
- **User-Friendly Interface**: A simple GUI for easy password input and strength checking.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/IamCOD3X/PassArmor.git
   cd PassArmor
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. You can install Tkinter using pip:
   ```bash
   pip install tk
   ```

3. **Run the Program**:
   Execute the Python script:
   ```bash
   python password_strength_checker.py
   ```

## How It Works

- **Password Input**: Enter your password in the text box.
- **Strength Check**: Click the "Check Strength" button to evaluate your password.
- **Feedback**: The strength meter will show the strength score, and a suggestion message will guide you on improving your password's security.

## Code Overview

Here's a brief overview of the code:

```python
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
subhead = tk.Label(root, text="The password strength checker", font=('calibre',8))
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
```

## Contributing

Feel free to contribute to this project. Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.