import customtkinter as ctk
import time

root = ctk.CTk()
root.title('Custom Tkinter')
root.minsize(300, 150)
# root.iconbitmap("C:/Users/Soumya/Desktop/S.png")
root.grid_rowconfigure(0)
root.grid_columnconfigure(1)

entry = ctk.CTkEntry(root, placeholder_text='Enter Width')
#entry1.place(relx=0.5, rely=0.5, anchor='s')
entry.grid(row=0, column=0)
entry.focus()


def resize():
    x = entry.get()
    root.geometry(f'{x}x{x}')
    ctk.set_appearance_mode('light')

button = ctk.CTkButton(root, text='Enter', command=resize)
button.grid(row=0, column=1)

button2 = ctk.CTkButton(root, text='Quit', command=lambda : root.quit())
button2.grid(row=0, column=3)

root.mainloop()