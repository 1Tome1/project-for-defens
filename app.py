from tkinter import *
from tkinter import ttk


app = Tk()

app.title("neural network")
app.geometry("300x400")
app.resizable(False, False)


icon = PhotoImage( file = "images.png")
app.iconphoto(True, icon)


for i in range(3): app.columnconfigure(index=i,weight=1)
for j in range(3): app.rowconfigure(index=j,weight=1)

label1 = ttk.Entry()
label1.grid(row=0, column=0, padx=0.5, pady=1, sticky="s")
textbox1 = ttk.Label(text="Вес человека")
textbox1.grid(row=0, column=0, padx=0.5, pady=1)


label2 = ttk.Entry()
label2.grid(row=0, column=2, padx=0.5, pady=1, sticky="s")
textbox2 = ttk.Label(text="Рост человека")
textbox2.grid(row=0, column=2, padx=0.5, pady=1)


textbox3 = ttk.Label(text="Пол", font=(24))
textbox3.grid(row=1, column=1, padx=1, pady=1)



button = ttk.Button(text="Определить")
button.grid(row=2, column=1)

app.mainloop()