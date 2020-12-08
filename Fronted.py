from tkinter import *
import backend
def select_from_list(event):
    try:
        global select_tuple
        cur = list1.curselection()[0]
        select_tuple = list1.get(cur)
        e1.delete(0,END)
        e1.insert(END,select_tuple[1])
        e2.delete(0,END)
        e2.insert(END,select_tuple[2])
        e3.delete(0,END)
        e3.insert(END,select_tuple[3])
        e4.delete(0,END)
        e4.insert(END,select_tuple[4])
    except:
        pass
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_cmmand():
    list1.delete(0,END)
    for row  in backend.search(title.get(),author.get(),year.get(),isbn.get()):
        list1.insert(END,row)

def addEntry_command():
    backend.insert(title.get(),author.get(),year.get(),isbn.get())
    #list1.delete(0,END)
    list1.insert(END,(title.get(),author.get(),year.get(),isbn.get()))


def delet_command():
    backend.delect(select_tuple[0])
    view_command()

def update_command():
    #list1.delete(cur)
    backend.update(select_tuple[0],title.get(),author.get(),year.get(),isbn.get())
    #list1.insert(cur,(title.get(),author.get(),year.get(),isbn.get()))
    view_command()

window = Tk()
window.wm_title("BookStore")
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)
l2 = Label(window,text="Author")
l2.grid(row=0,column=2)
l3 = Label(window,text="Year")
l3.grid(row=1,column=0)
l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

title  = StringVar()
e1 = Entry(window,textvariable=title)
e1.grid(row=0,column=1)

author  = StringVar()
e2 = Entry(window,textvariable=author)
e2.grid(row=0,column=3)

year = StringVar()
e3 = Entry(window,textvariable=year)
e3.grid(row=1,column=1)

isbn = StringVar()
e4 = Entry(window,textvariable=isbn)
e4.grid(row=1,column=3)

b1 = Button(window,text="View All",command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search Entry",command=search_cmmand)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add Entry",command=addEntry_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update",command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",command=delet_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close")
b6.grid(row=7,column=3)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
list1.bind('<<ListboxSelect>>',select_from_list)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)


window = mainloop()
