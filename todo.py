import tkinter as tk
from tkinter import messagebox, ttk 
import sqlite3

#defining the function add
def add_task():
    task = task_field.get()
    if len(task) == 0:
        messagebox.showinfo('Task is not entered')
    else:
        tasks.append(task)
        cursor.execute('INSERT INTO tasks VALUES (?)', (task,))
        connection.commit()
        update_list()
        task_field.delete(0, 'end')

def update_list():
    listbox.delete(0, 'end')
    for row in cursor.execute('SELECT task from tasks'):
        listbox.insert('end', row[0])

def delete_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            cursor.execute('DELETE from tasks WHERE task=?', (selected_task,))
            connection.commit()
            update_list()
    except:
        messagebox.showinfo('No task selected for Deletion')

def clear_list():
    cursor.execute('DELETE from tasks')
    connection.commit()
    update_list()

def close():
    todoWindow.destroy()

#establishing the connection
connection = sqlite3.connect('List_of_Tasks.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks (task TEXT)')

#defining the main function
if __name__ == '__main__':
    tasks = []
    todoWindow = tk.Tk()
    todoWindow.title("To-Do List Manager")
    todoWindow.geometry("750x350")
    todoWindow.resizable(0, 0)
    todoWindow.configure(bg="#FFD700")

    header_frame=tk.Frame(todoWindow, bg="#FFD700")
    functions_frame=tk.Frame(todoWindow, bg="#FFD700")
    label_field_frame=tk.Frame(todoWindow, bg="#FFD700")
    listbox_frame=tk.Frame(todoWindow, bg="#FFD700")

    header_frame.pack(fill="both")
    functions_frame.pack(side="right", fill="both", expand="True")
    label_field_frame.pack(side="right", fill="both", expand="True")
    listbox_frame.pack(side="left", fill="both", expand="True")

    header_label=ttk.Label(
    	header_frame,
    	text="To-Do List Manager",
    	font=("Florina", "18", "bold"),
    	background="#FFFFFF",
    	foreground="#990F4B"
    )

    header_label.pack(padx=20, pady=20)

    task_label=ttk.Label(
    	label_field_frame,
   	    text="Enter the task:",
   	    font=("Florina", "18", "bold", "italic"),
   	    background="#FFD700",
   	    foreground="#FFFFFF"
   	)

    task_label.pack(padx=30, pady=20)

    

    task_field=ttk.Entry(
    	label_field_frame,
    	font=("Florina", "18"),
    	width=18,
        background="#F7FFDC",
        foreground="#000000"
       )

    task_field.pack(padx=30, pady=5)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        command=add_task
    )
    add_button.pack(padx=30, pady=10)

    delete_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        command=delete_task
    )
    delete_button.pack(padx=30, pady=10)

    clear_button = ttk.Button(
        functions_frame,
        text="Clear List",
        command=clear_list
    )
    clear_button.pack(padx=30, pady=10)

    listbox = tk.Listbox(
        listbox_frame,
        font=("Consolas", "14"),
        width=40,
        height=10,
        selectbackground="yellow",
        selectmode=tk.SINGLE
    )
    listbox.pack(padx=30, pady=10)

    close_button = ttk.Button(
        functions_frame,
        text="Close",
        command=close
    )
    close_button.pack(padx=30, pady=10)

    update_list()
    todoWindow.mainloop()
    cursor.close()


  