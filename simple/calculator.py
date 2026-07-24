from tkinter import*
#create window

root=Tk()
root.title("Calculator")
root.resizable(False,False)

expression=""
#display
entry=Entry(root,font=("Arial",20), justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipadx=8,ipady=8)

def press(num):
    global expression
    expression+=str(num)
    entry.delete(0,END)
    entry.insert(END,expression)



def clear():
    global expression
    expression="" 
    entry.delete(0,END)


def equal():
    global expression
    try:
        result=str(eval(expression))
        entry.delete(0,END)
        entry.insert(END,result)
        expression=result

    except:
        entry.delete(0,END)
        entry.insert(END,"error")
        expression=""




#designing button

# buttons=[
#     ()
# ]

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for(text,row,col) in buttons:

    if text=="C":
        cmd=clear
    elif text =="=":
        cmd=clear
    else:
        cmd=lambda t=text: press(t)

    Button(
        root,
        text=text,
        font=("Arial",16),
        width=5,
        height=2,
        command=cmd
    ).grid(row=row,column=col,padx=5,pady=5)


root.mainloop()