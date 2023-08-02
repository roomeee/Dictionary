from tkinter import *
from PyDictionary import PyDictionary
import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
root.title("Dictionary")
root.geometry('620x500')
root.resizable(False, False)

def Lookup():
    text.delete(1.0, END)

    word = entry.get().strip()
    if not word:
        text.insert(END, "Please enter a word.", 'error')
        return

    dictionary = PyDictionary()
    try:
        explanation = dictionary.meaning(word)
        if explanation:
            for key, value in explanation.items():
                text.insert(END, key + '\n\n', 'title')
                for val in value:
                    text.insert(END, f'- {val}\n\n', 'content')
        else:
            text.insert(END, f" sorry, the Word '{word}' not found in the dictionary.", 'error')
    except Exception as e:
        text.insert(END, "An error occurred while fetching the data. Please try again later.", 'error')

frame = ctk.CTkFrame(root, corner_radius=10)
frame.pack(pady=20)


label = Label(frame, text='Dictionary', font=('Arial', 20,'bold'), fg='#a58ede', bg='#292929')
label.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 20))

entry = ctk.CTkEntry(frame, width=400, height=40, border_width=1, placeholder_text="Enter a word", text_color='silver')
entry.grid(row=1, column=0, padx=10)

button = ctk.CTkButton(frame, text="Search", command=Lookup)
button.grid(row=1, column=1, padx=10)

text_frame = ctk.CTkFrame(root, corner_radius=10)
text_frame.pack(pady=10)


scrollbar = Scrollbar(text_frame, troughcolor='#292929', activebackground='#292929', bg='#292929')
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(text_frame, width=68, height=20, bd=0, wrap=WORD, bg='#292929', fg='white', font=('Arial', 13), yscrollcommand=scrollbar.set)
text.tag_configure('title', font=('Arial', 14, 'bold'), foreground='#a58ede')
text.tag_configure('content', font=('Arial', 12), foreground='white')
text.tag_configure('error', font=('Arial', 12), foreground='red')
text.pack(pady=10, padx=10)


scrollbar.config(command=text.yview)

root.mainloop()
