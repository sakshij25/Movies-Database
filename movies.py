import tkinter as tk
from tkinter import ttk
import movies_database as db

mainWindow = tk.Tk()

mainWindow.title( "MOVIES RECORD")
mainWindow.geometry("500x300+100+100")

heading_label = tk.Label(mainWindow, text = "NAME")
heading_label.pack()
heading_label.place(x=30, y=20)
name_field = tk.Entry(mainWindow, width = 40)
name_field.pack()
name_field.place(x = 120,y = 20)

heading_label1 = tk.Label(mainWindow, text = "DURATION")
heading_label1.pack()
heading_label1.place(x=30, y=50)
name_field1 = tk.Entry(mainWindow, width = 40)
name_field1.pack()
name_field1.place(x = 120, y = 50)

heading_label2 = tk.Label(mainWindow, text = "GENRE")
heading_label2.pack()
heading_label2.place(x = 30, y = 80)
name_field2 = tk.Entry(mainWindow, width = 40)
name_field2.pack()
name_field2.place(x = 120, y =80)

heading_label3 = tk.Label(mainWindow, text = "RELEASE YEAR")
heading_label3.pack()
heading_label3.place(x = 30, y = 110)
name_field3 = tk.Entry(mainWindow, width = 40)
name_field3.pack()
name_field3.place(x = 120, y = 110)

heading_label4 = tk.Label(mainWindow, text = "RATINGS")
heading_label4.pack()
heading_label4.place(x = 30,y = 140)
name_field4 = tk.Entry(mainWindow, width = 40)
name_field4.pack()
name_field4.place(x = 120, y = 140)

def entry():
    name = name_field.get()
    duration = name_field1.get()
    genre = name_field2.get()
    release_year = name_field3.get()
    ratings = name_field4.get()

    db.insert_record(name, duration, genre, release_year, ratings)

def create_window():
    root = tk.Tk()
    window = tk.Toplevel(root)
    cursor = db.retrieve_records()

    tree = ttk.Treeview(root)
    tree["columns"] = ("one", "two", "three", "four", "five")

    tree.heading("one", text="Movie Name")
    tree.heading("two", text="Duration")
    tree.heading("three", text="Genre")
    tree.heading("four", text="Release Year")
    tree.heading("five", text="Ratings")

    i = 0

    for row in cursor:
        tree.insert('', i, text="Movie " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4],
                            row[5]))
        i = i + 1

    tree.pack()
    root.mainloop()

def exit_program():
        quit()


button1 = tk.Button(mainWindow, text = "SAVE",command = lambda:entry()).place(x=50, y=200)

button2 = tk.Button(mainWindow, text = "VIEW",command = lambda:create_window()).place(x=110, y=200)

button3 = tk.Button(mainWindow, text = "EXIT", command = lambda:exit_program()).place(x=170, y=200)

mainWindow.mainloop()
