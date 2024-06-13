import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("To-Do-List/tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("To-Do-List/tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')
        listbox.delete(ANCHOR)
def openTaskFile():
    try:
        global task_list
        with open("To-Do-List/tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('To-Do-List/tasklist.txt', 'w')
        file.close()

#icon
img_icon = PhotoImage(file="To-Do-List/download.png")
root.iconphoto(True, img_icon)

#topbar
top_bar_icon = PhotoImage(file="To-Do-List/d1.png")
Label(root,image=top_bar_icon).pack()

#docimg
doc_img = PhotoImage(file="To-Do-List/d2.png")
Label(root, image=doc_img, bg="#32405b").place(x=30,y=15)

#task_icon
task_icon = PhotoImage(file="To-Do-List/d3.png")
Label(root, image=task_icon, bg="#32405b").place(x=310,y=10)
heading = Label(root, text="All Task", font="arial 30 bold", fg="white", bg="black")
heading.place(x=130,y=20)
#main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="ariel 20", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6,bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

#listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#delete
Delete_icon = PhotoImage(file="To-Do-List/d5.png")
Button(root, image=Delete_icon, command=deleteTask).pack(side=BOTTOM,pady=13)

openTaskFile()


root.mainloop()