from tkinter import *
from tkinter import ttk 
from tkinter import messagebox


def calculate_bmi():
    try:
        resulttext.delete("1.0","end")
        name=''
        name=nameentry.get().capitalize()
        height=float(heightentry.get())
        weight=float(weightentry.get())

        if v1.get()=="feet":
            height *=30.48
        elif v1.get()=="meter":
            height *=100
        if v2.get()=="lbs":
            weight *=0.453592
        bmi=weight/((height/100)**2)
        if bmi<=18.5:
            resulttext.tag_configure("center", justify='center')
            resulttext.insert("1.0","Hey {}, your BMI is {:.1f} which\nindicates that you are UNDERWEIGHT!".format(name,bmi))
            resulttext.tag_add("center", "1.0", "end")
        elif bmi>18.5 and bmi<25.0:
            resulttext.tag_configure("center", justify='center')
            resulttext.insert("1.0","Hey {}, your BMI is {:.1f} which\nindicates that you are HEALTHY WEIGHT!".format(name,bmi))
            resulttext.tag_add("center", "1.0", "end")
        elif bmi>=25.0 and bmi<30:
            resulttext.tag_configure("center", justify='center')
            resulttext.insert("1.0","Hey {}, your BMI is {:.1f} which indicates\nthat you are SLIGHTLY OVERWEIGHT!".format(name,bmi))
            resulttext.tag_add("center", "1.0", "end")
        else:
            resulttext.tag_configure("center", justify='center')
            resulttext.insert("1.0","Hey {}, your BMI is {:.1f}\nwhich indicates that you are OBESE!".format(name,bmi))
            resulttext.tag_add("center", "1.0", "end")
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid number')
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Height cannot be 0!')


mainwin=Tk()
mainwin.geometry("505x450+300+100")
mainwin.title("BMI Calculator")
mainwin.iconbitmap('D:/BMI Calculator-Python/iconcal.ico')
mainwin.config(bg="#15383B")
mainwin.resizable(False,False)

font30=('Arial',30,'bold')
font18=('Arial',18,'bold')
font15=('Arial',15,'bold')

titlelabel=Label(mainwin,font=font30,text="BMI Calculator",fg="#53C0C8", bg="#15383B")
titlelabel.place(x=120,y=5)

namelabel=Label(mainwin,font=font18,text="Name:",fg="#53C0C8", bg="#15383B")
namelabel.place(x=30,y=90)

weightlabel=Label(mainwin,font=font18,text="Weight:",fg="#53C0C8", bg="#15383B")
weightlabel.place(x=30,y=150) 

heightlabel=Label(mainwin,font=font18,text="Height:",fg="#53C0C8", bg="#15383B")
heightlabel.place(x=30,y=210)

nameentry=Entry(mainwin,font=font18,bg="#225C61",width=25)
nameentry.place(x=140,y=90)
nameentry.focus()

weightentry=Entry(mainwin,font=font18,bg="#225C61",width=18)
weightentry.place(x=140,y=150)

heightentry=Entry(mainwin,font=font18,bg="#225C61",width=18)
heightentry.place(x=140,y=210)

resulttext=Text(mainwin,font=font18,height=2,width=39,bg="#15383B",fg="#53C0C8", border=0)
resulttext.place(x=0,y=340)

weight_opt=['kgs','lbs']
height_opt=['cm','feet','meter']

v1=StringVar()
v2=StringVar()

style=ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#225C61", background= "#225C61",textcolor="black")

weight_combo=ttk.Combobox(mainwin,font=font15,background='#225C61',width=5, textvariable=v2, values=weight_opt, state='readonly')
weight_combo.set('kgs')
weight_combo.place(x=393,y=150,height=32)

height_combo=ttk.Combobox(mainwin,font=font15,background='#225C61',width=5,textvariable=v1, values=height_opt, state='readonly')
height_combo.set('cm')
height_combo.place(x=393,y=210,height=32)

calbutton=Button(mainwin,text="Calculate",width=18, background="#2E8188", activebackground="#225C61", font=font15, command=calculate_bmi)
calbutton.place(x=136,y=275)

mainwin.mainloop()
