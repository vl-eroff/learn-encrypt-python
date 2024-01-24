import tkinter as tk
from tkinter import filedialog
from tkinter import Menu

def encrypt_decrypt(text, key, encrypt=True):
    result = ""
    key = [int(digit) for digit in str(key)]
    key_len = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key[i % key_len] if encrypt else -key[i % key_len]
            result += chr((ord(char) - ord('А' if char.isupper() else 'а') + shift) % 33 + ord('А' if char.isupper() else 'а'))
        else:
            result += char
            
    return result

def process_cipher():
    text = input_text.get("1.0", "end-1c")
    key = key_entry.get()
    is_encrypt = encrypt_var.get()
    
    result = encrypt_decrypt(text, key, is_encrypt)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def open_file():
    file_path = tk.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf8") as file:
            content = file.read()
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, content)

def save_file():
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        content = output_text.get("1.0", tk.END)
        with open(file_path, "w", encoding="utf8") as file:
            file.write(content)

def clear_fields():
    input_text.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)
    output_text.delete("1.0", tk.END)

def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    
    about_label = tk.Label(about_window, text="This is a Gronsfeld Cipher application.")
    about_label.pack(padx=10, pady=10)
    
    close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
    close_button.pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("Gronsfeld Cipher")
root.resizable(False, False)

# Menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=False)

# Open, Save and Exit buttons
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="Выход", command=root.destroy)
menu_bar.add_cascade(label="Файл", menu=file_menu)

# About option
menu_bar.add_command(label="О программе", command=open_about_window)

# Input text
input_label = tk.Label(root, text="Исходный текст:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=0, column=1, padx=5, pady=5)

# Key entry
key_label = tk.Label(root, text="Ключ:")
key_label.grid(row=1, column=0, padx=5, pady=5)
key_entry = tk.Entry(root)
key_entry.grid(row=1, column=1, padx=5, pady=5)

# Encryption/Decryption choice
encrypt_var = tk.BooleanVar()
encrypt_check = tk.Checkbutton(root, text="Расшифровать", variable=encrypt_var)
encrypt_check.grid(row=2, column=1, padx=5, pady=5)

# Output text
output_label = tk.Label(root, text="Результат:")
output_label.grid(row=3, column=0, padx=5, pady=5)
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=3, column=1, padx=5, pady=5)

# Process button
process_button = tk.Button(root, text="Преобразовать", command=process_cipher)
process_button.grid(row=4, column=1, padx=5, pady=10)

# Clear Fields button
clear_button = tk.Button(root, text="Очистить поля", command=clear_fields)
clear_button.grid(row=6, column=1, padx=5, pady=10)

root.mainloop()