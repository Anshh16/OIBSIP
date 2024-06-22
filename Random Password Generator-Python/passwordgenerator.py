from tkinter import *
from tkinter import messagebox
from random import randint


def gen_pass():
    try:
        passentry.delete(0,END)
        passlen=int(charentry.get())
        mypass=''
        for i in range(passlen):
            mypass += chr(randint(33,126))
        passentry.insert(0,mypass)
    except ValueError:
        messagebox.showerror('Error', 'Please enter number of characters.')

def cliptocopy():
    mainwin.clipboard_clear()
    mainwin.clipboard_append(passentry.get())
    messagebox.showinfo('Info', 'Password copied to clipboard!')

mainwin=Tk()
mainwin.geometry("500x330+300+100")
mainwin.title("Password Generator")
mainwin.iconbitmap('D:/Random Password Generator-Python/passicon.ico')
mainwin.config(bg="#0d1b2a")
mainwin.resizable(False,False)

font30=('Arial',30,'bold')
font18=('Arial',18,'bold')
font14=('Arial',14,'bold')
font10=('Arial',10,'bold')
font17=('Arial',17,'bold')

titlelabel=Label(mainwin,font=font30,text="Password Generator",fg="#778da9", bg="#0d1b2a")
titlelabel.place(x=52,y=5)

password=chr(randint(33,126))

label=Label(mainwin, font=font14, text="Number of characters:", fg="#778da9", bg="#0d1b2a")
label.place(x=80,y=85)

charentry=Entry(mainwin,font=font14, bg="#778da9",width=10)
charentry.place(x=295,y=85)
charentry.focus()

passentry=Entry(mainwin, font=font17, bg="#778da9",width=28)
passentry.place(x=63,y=160)

button1=Button(mainwin,text='Generate Strong Password', width=22, background="#778da9", activebackground="#e0e1dd", font=font10, command=gen_pass)
button1.place(x=52,y=245)

button2=Button(mainwin,text='Copy to Clipboard', width=22, background="#778da9", activebackground="#e0e1dd", font=font10, command=cliptocopy)
button2.place(x=260,y=245)

mainwin.mainloop()
