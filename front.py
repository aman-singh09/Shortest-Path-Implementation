import rt as a
from  tkinter import *
r=Tk()
def about():
    newwin=Toplevel(r)
    newwin.title('About the program')
    newwin['bg']='black'
    Label(newwin,text="This is a program of shortest distance between 10 cities using djikstra's algorithm",fg='yellow',bg='black',font=('times', 14, 'italic bold')).grid(row=2)
    Label(newwin,text="This is developed by Apurva, Ankit, Aman",fg='red',bg='black',font=('times', 18, 'italic bold')).grid(row=4)
    Label(newwin,text='References: https://www.geeksforgeeks.org',fg='blue',bg='black',font=('times', 18, 'italic bold underline')).grid(row=6)
def new_window():
    w=Toplevel(r)
    menu = Menu(w) 
    w.config(menu=menu) 
    filemenu = Menu(menu) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='New',command=new_window)
    filemenu.add_separator() 
    filemenu.add_command(label='Exit', command=r.destroy) 
    helpmenu = Menu(menu) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About',command=about)
    w.title("Shortest path using djikstra's algorithm")
    Label(w,text="\t\t\t\tEnter source",fg='blue',font='bold').grid(row=4,column=0)
    Label(w,text="\t\t\t\tEnter destination",fg='orange',font='bold ').grid(row=5,column=0)
    x = StringVar()
    x.set('Nothing')
    y = StringVar()
    y.set('Nothing')
    drop = OptionMenu(w, x, 'Delhi', 'Mumbai', 'Pune', 'Chennai', 'Vishakapatnam', 'Bangalore', 'Gandhinagar', 'Assam','Allahabad', 'Bhopal')
    drop1 = OptionMenu(w, y, 'Delhi', 'Mumbai', 'Pune', 'Chennai', 'Vishakapatnam', 'Bangalore', 'Gandhinagar', 'Assam','Allahabad', 'Bhopal')
    drop.grid(row=4, column=2)
    drop1.grid(row=5, column=2)
    e1 = Entry(w,textvariable=x)
    e2 = Entry(w,textvariable=y)
    e1.grid(row=4, column=1) 
    e2.grid(row=5, column=1)

    graph = {'Mumbai': {'Pune': 150, 'Delhi': 1500, 'Allahabad':1400},
            'Pune': {'Mumbai': 150, 'Delhi': 1435, 'Bangalore':840, 'Assam': 2900},
            'Delhi': {'Mumbai': 1500, 'Pune': 1435, 'Chennai': 2200, 'Gandhinagar': 930 },
            'Bangalore': {'Pune': 840, 'Chennai': 345, 'Vishakapatnam': 1000, 'Assam': 3000},
            'Chennai': {'Delhi': 2200, 'Bangalore': 345, 'Vishakapatnam': 800, 'Assam': 2800},
            'Vishakapatnam': {'Bangalore': 1000, 'Chennai': 800, 'Allahabad': 1100},
            'Assam': {'Pune': 2900, 'Bangalore': 3000, 'Chennai': 2800, 'Gandhinagar': 2700},
            'Gandhinagar': {'Delhi': 930, 'Assam': 2700, 'Bhopal': 600},
            'Allahabad': {'Mumbai': 1400, 'Vishakapatnam': 1100, 'Bhopal': 600},
            'Bhopal': {'Gandhinagar': 600, 'Allahabad': 600}}

    Label(w,text='Cities to choose from=\n\nMumbai \tPune\tDelhi\tBangalore\tChennai',font=('times', 14, 'italic bold underline')).grid(row=0,column=0)
    Label(w,text='Vishakapatnam\tAssam\tGandhinagar\tAllahabad\tBhopal',font=('times', 14, 'italic bold underline')).grid(row=1,column=0)
    b = Button(w,text="SUBMIT",font='bold',width= 25,fg='green',command=lambda :a.dijkstra(graph,x.get(),y.get()))
    c = Button(w,text="QUIT",font='bold',width= 25,fg='red',command=r.destroy)
    b.grid(row=8,column=3)
    c.grid(row=9,column=3)
    def good():
        Label(w,text='Thanks',fg='violet',font='bold').grid(row=11)
    Checkbutton(w,text="Was it good",fg='brown',font='bold',command=good).grid(row=10)


menu = Menu(r)
r.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New',command=new_window)
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=r.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About',command=about)

r.title("Shortest path using djikstra's algorithm")
Label(r,text="\t\t\t\t\tEnter source",fg='blue',font='bold').grid(row=4,column=0)
Label(r,text="\t\t\t\t\tEnter destination",fg='orange',font='bold ').grid(row=5,column=0)
x = StringVar()
x.set('Nothing')
y = StringVar()
y.set('Nothing')
drop = OptionMenu(r, x, 'Delhi','Mumbai','Pune','Chennai','Vishakapatnam','Bangalore','Gandhinagar','Assam','Allahabad','Bhopal')
drop1 = OptionMenu(r, y, 'Delhi','Mumbai','Pune','Chennai','Vishakapatnam','Bangalore','Gandhinagar','Assam','Allahabad','Bhopal')
drop.grid(row=4,column=2)
drop1.grid(row=5,column=2)
e1 = Entry(r,textvariable=x)
e2 = Entry(r,textvariable=y)
e1.grid(row=4,column=1) 
e2.grid(row=5,column=1)

graph = {'Mumbai': {'Pune': 150, 'Delhi': 1500, 'Allahabad':1400},
        'Pune': {'Mumbai': 150, 'Delhi': 1435, 'Bangalore':840, 'Assam': 2900},
        'Delhi': {'Mumbai': 1500, 'Pune': 1435, 'Chennai': 2200, 'Gandhinagar': 930 },
        'Bangalore': {'Pune': 840, 'Chennai': 345, 'Vishakapatnam': 1000, 'Assam': 3000},
        'Chennai': {'Delhi': 2200, 'Bangalore': 345, 'Vishakapatnam': 800, 'Assam': 2800},
        'Vishakapatnam': {'Bangalore': 1000, 'Chennai': 800, 'Allahabad': 1100},
        'Assam': {'Pune': 2900, 'Bangalore': 3000, 'Chennai': 2800, 'Gandhinagar': 2700},
        'Gandhinagar': {'Delhi': 930, 'Assam': 2700, 'Bhopal': 600},
        'Allahabad': {'Mumbai': 1400, 'Vishakapatnam': 1100, 'Bhopal': 600},
        'Bhopal': {'Gandhinagar': 600, 'Allahabad': 600}}

Label(r,text='Cities to choose from=\n\nMumbai \t Pune\tDelhi\tBangalore\tChennai',font=('times', 14, 'italic bold underline')).grid(row=0,column=0)
Label(r,text='Vishakapatnam\tAssam\tGandhinagar\tAllahabad\tBhopal',font=('times', 14, 'italic bold underline')).grid(row=1,column=0)
b = Button(r,text="SUBMIT",font='bold',width= 25,fg='green',command=lambda :a.dijkstra(graph,x.get(),y.get()))
c = Button(r,text="QUIT",font='bold',width= 25,fg='red',command=r.destroy)
b.grid(row=8,column=2)
c.grid(row=9,column=2)
def good():
    Label(r,text='Thanks!!!! I know',fg='violet',font='bold').grid(row=11)
Checkbutton(r,text="Was it good",fg='brown',font='bold',command=good).grid(row=10)
r.mainloop()


