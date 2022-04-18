from tkinter import*
# It helps to display the root window and manages all the other components of the tkinter application
root=Tk()
root.configure(background="blue")
root.title("CHATBOAT")

def send():
    # get() : Returns the entry's current text as a string
    send = "you:"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hi"):
        txt.insert(END,"\n"+"                       Computer Hello!, How can we help you? ")
    elif (e.get()=="i want to know about NAVGURUKUL?"):
        txt.insert(END,"\n"+"Computer                  Sure! Navgurukul is free SOFTWARE DEVELOPMENT COURSE  ")
    elif (e.get()=="what are the languages you are teaching "):
        txt.insert(END,"\n"+"Computer                  We  teahes Programming Languages ")
    elif (e.get()=="Like?"):
        txt.insert(END,"\n"+"Computer                  Python,Javascript ,Advance javascript ,Node js and react.js ")
    elif (e.get()=="okay thankyou!"):
        txt.insert(END,"\n"+"Computer                  for any other query please visit again.")
    else:
        txt.insert(END,"\n"+"Computer Plese enter again ")
    e.delete(0,END)
txt = Text(root)
txt.grid(row=0,column=0)
# Entry widgets are used to display a single line text that is generally taken in the form of user Input.
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)

# # The grid() geometry manager organises widgets in a table-like 
# structure in the parent widget. The master widget is split into rows and 
# columns, and each part of the table can hold a widget. It uses column , 
e.grid(row=1,column=0)
root.mainloop()
# # mainloop() tells Python to run the Tkinter event loop. 





