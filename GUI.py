from tkinter import *
from tkinter.scrolledtext import ScrolledText

window = Tk()

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Rating")
l3.grid(row=1,column=0)

l4 = Label(window,text="Finished")
l4.grid(row=1,column=2)

l5 = Label(window,text="Opinion ")
l5.grid(row=0,column=4)


title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

rating_text = StringVar()
e3 = Entry(window,textvariable=rating_text)
e3.grid(row=1,column=1)

finished_text = StringVar()
e4 = Entry(window,textvariable=finished_text)
e4.grid(row=1,column=3)



e5 = ScrolledText(window,height=7,width=40)
e5.grid(row=1,column=5)





window.mainloop()


