from tkinter import *

window=Tk()
window.geometry("520x400")
window.resizable(0,0)
window.title("Calculator")
window.configure(bg="grey")

def button_click(item):
    global expression
    expression =expression + str(item)
    input_text.set(expression)
    

def button_clear():
    global expression
    expression=""
    input_text.set("")

def button_equals():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""

expression=""

input_text = StringVar()
    

#--------------------------------------------set frame-----------------------------------------------------------------

frame = Frame(window,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
frame.pack(side=TOP)

input_field=Entry(frame,font=("Arial",18,"bold"),textvariable=input_text,width=50,foreground="black",bg="#eee",bd=0,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)
# ‘ipady’ is internal padding that increases the height of the input field.


buttons_frame=Frame(window,width=312,height=272.5,bg="grey")
buttons_frame.pack()



#---------------------------------Buttons---------------------------------------------------------------------------------


one = Button(buttons_frame, text = "1", bg="white", fg = "black", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: button_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

twobutton=Button(buttons_frame,text="2",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command= lambda: button_click(2)).grid(row=3,column= 1, padx = 1, pady =1 )

threebutton=Button(buttons_frame,text="3",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command= lambda: button_click(3)).grid(row=3,column= 2, padx = 1, pady = 1)

fourbutton=Button(buttons_frame,text="4",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click(4)).grid(row=2,column= 0, padx = 1, pady = 1)

fivebutton=Button(buttons_frame,text="5",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click(5)).grid(row=2,column= 1, padx = 1, pady = 1)

sixbutton=Button(buttons_frame,text="6",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click(6)).grid(row=2,column= 2, padx = 1, pady = 1)

sevenbutton=Button(buttons_frame,text="7",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click(7)).grid(row=1,column= 0, padx = 1, pady = 1)

eightbutton=Button(buttons_frame,text="8",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click(8)).grid(row=1,column= 1, padx = 1, pady = 1)

ninebutton=Button(buttons_frame,text="9",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click(9)).grid(row=1,column= 2, padx = 1, pady = 1)

zerobutton=Button(buttons_frame,text="0",width=24,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click(0)).grid(row=4,column= 0,columnspan=2, padx =1, pady = 1)

dotbutton=Button(buttons_frame,text=".",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click(".")).grid(row=4,column= 2, padx =1, pady = 1)

plusbutton=Button(buttons_frame,text="+",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click("+")).grid(row=0,column= 3, padx = 1, pady =1 )

minusbutton=Button(buttons_frame,text="-",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click("-")).grid(row=1,column= 3, padx = 1, pady =1 )

productbutton=Button(buttons_frame,text="*",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click("*")).grid(row=2,column= 3, padx = 1, pady =1 )

dividebutton=Button(buttons_frame,text="/",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_click("/")).grid(row=3,column= 3, padx = 1, pady =1 )

resultbutton=Button(buttons_frame,text="=",width=10,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_equals()).grid(row=4,column= 3, padx = 1, pady =1)

clearbutton=Button(buttons_frame,text="C",width=38,height=3,bg="white",fg="black",bd=0,cursor="hand2",command=lambda:button_clear()).grid(row=0,column= 0,columnspan=3, padx = 1, pady =1)








window.mainloop()