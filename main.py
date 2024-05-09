from tkinter import *
from PIL import ImageTk
root = Tk()
root.title("MMU Assistance")
root.geometry("460x750")
#root.resizable(False,False)
root.config(bg="OrangeRed")

def speak():
    print("Its running!!!")
def write():
    print("Its running!!!")
def delete():
    print("Its running!!!")

frame = LabelFrame(root, relief="raised")
frame.grid(row=0, column=0,pady=00)

text_label= Label(frame,text="MMU Assistance", font=("DarkOrange",14))
text_label.grid(row=0,column=0)

ai_image = PhotoImage(file="ai.png")
image_label=Label(frame,image=ai_image)
image_label.grid(row=1,column=0)

text=Text(root)
text.grid(row=2,column=0)
text.place(x=235,y=560,width=225,height=60)
text.config(bg="Green")

entry=Entry(root)
entry.place(x=0,y=560,width=230,height=60)
entry.config(bg="Teal")

button_1=Button(root,text="Speak",bg="DeepSkyBlue",command=speak)
button_1.place(x=30,y=660,width=115,height=60)

button_2=Button(root,text="Write",bg="DeepSkyBlue",command=write)
button_2.place(x=170,y=660,width=115,height=60)

button_3=Button(root,text="Delete",bg="DeepSkyBlue",command=delete)
button_3.place(x=310,y=660,width=115,height=60)

root.mainloop()