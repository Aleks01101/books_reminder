from tkinter import *
from tkinter.scrolledtext import ScrolledText
import book


def view_command():
    list1.delete(0,END)
    for row in book.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in book.search(title_text.get(),author_text.get()):
        list1.insert(END,row)

def add_command():
    book.add_book(title_text.get(),author_text.get(),rating_text.get(),finished_text.get(),e5.get('1.0','end-1c'))

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



e5 = ScrolledText(window,height=6,width=35)
e5.grid(row=1,column=5)

list1 = Listbox(window,height=10,width=60)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


b1 = Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Add entry",width=12,command=add_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Search entry",width=12,command=search_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update selected",width=12,command=view_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete selected",width=12,command=view_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=12,command=view_command)
b6.grid(row=7,column=3)


window.mainloop()


