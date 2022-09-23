import customtkinter as ctk
import tkinter as ttk

ctk.set_default_color_theme("dark-blue")  
ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry('500x300')
root.title('Python GUI')

class page1(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.master = root



def ch_p1():
    p1.pack(fill='both', expand=True)
    p2.pack_forget()

def ch_p2():
    p2.pack(fill='both', expand=True)
    p1.pack_forget()

p1 = ctk.CTkFrame(master=root)
p1.pack(fill="both", expand=True)
label_1 = ctk.CTkLabel(master=p1, justify=ttk.LEFT, text='This is Page 1')
label_1.pack(pady=12, padx=10)

p2 = ctk.CTkFrame(master=root)
label_2 = ctk.CTkLabel(master=p2, justify=ttk.LEFT, text='This is Page 2')
label_2.pack(pady=12, padx=10)

b1 = ctk.CTkButton(master=p2, text='Page 1', command=ch_p1)
b1.pack(padx=20, pady=10)

b2 = ctk.CTkButton(master=p1, text='Page 2', command=ch_p2)
b2.pack(padx=20, pady=10)

root.mainloop()
app = page1()

app.mainloop()