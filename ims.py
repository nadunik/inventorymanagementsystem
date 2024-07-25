from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import pymysql

def exit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        window.destroy()
    else:
        pass

def update_item():
    def update_data():
        query= 'UPDATE item SET name=%s,quantity=%s,supplier=%s,dateadded=%s WHERE id=%s'
        mycursor.execute(query,(nameEntry.get(),quantityEntry.get(),supplierEntry.get(),dateEntry.get(),idEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Id {idEntry.get()} is updated successfully')
        updatewindow.destroy()
        show_item()

    updatewindow= CTkToplevel()
    updatewindow.title('Update Item')
    updatewindow.resizable(0, 0)
    updatewindow.grab_set()
    updatewindow.geometry('230+130')

    idLabel = CTkLabel(updatewindow, text='Id', font=('arial', 14, 'bold'))
    idLabel.grid(padx=20, pady=15, sticky=W)
    idEntry = CTkEntry(updatewindow, font=('arial', 13, 'bold'))
    idEntry.grid(row=0, column=1, padx=20, pady=15)

    nameLabel = CTkLabel(updatewindow, text='Name', font=('arial', 14, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = CTkEntry(updatewindow, font=('arial', 13, 'bold'))
    nameEntry.grid(row=1, column=1, padx=20, pady=15)

    quantityLabel = CTkLabel(updatewindow, text='Quantity', font=('arial', 14, 'bold'))
    quantityLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    quantityEntry = CTkEntry(updatewindow, font=('arial', 13, 'bold'))
    quantityEntry.grid(row=2, column=1, padx=20, pady=15)

    supplierLabel = CTkLabel(updatewindow, text='Supplier', font=('arial', 14, 'bold'))
    supplierLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    supplierEntry = CTkEntry(updatewindow, font=('arial', 13, 'bold'))
    supplierEntry.grid(row=3, column=1, padx=20, pady=15)

    dateLabel = CTkLabel(updatewindow, text='Date Added', font=('arial', 14, 'bold'))
    dateLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    dateEntry = CTkEntry(updatewindow, font=('arial', 13, 'bold'))
    dateEntry.grid(row=4, column=1, padx=20, pady=15)

    updateItemButton = CTkButton(updatewindow, text='Update Item', corner_radius=10, cursor='hand2', fg_color='#78C0BC', text_color='white',command=update_data)
    updateItemButton.grid(row=5, columnspan=2, pady=40)

    indexing=itemTable.focus()
    content=itemTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0, listdata[1])
    quantityEntry.insert(0, listdata[2])
    supplierEntry.insert(0, listdata[3])
    dateEntry.insert(0, listdata[4])



def show_item():
    query='SELECT * FROM item'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    itemTable.delete(*itemTable.get_children())
    for data in fetched_data:
        itemTable.insert('',END,values=data)

def delete_item():
    indexing = itemTable.focus()
    if not indexing:
        messagebox.showerror('Error', 'No item selected')
        return
    content = itemTable.item(indexing)
    contentId = content['values'][0]

    query = 'DELETE FROM item WHERE id = %s'
    try:
        mycursor.execute(query, (contentId,))
        con.commit()
        messagebox.showinfo('Delete', f'The item with ID {contentId} will be deleted')

        itemTable.delete(indexing)
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Error deleting item: {e}')

def search_item():
    def search_data():
        query='SELECT * FROM item WHERE id=%s or name=%s or quantity=%s or supplier=%s or dateadded=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),quantityEntry.get(),supplierEntry.get(),dateEntry.get()))
        itemTable.delete(*itemTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            itemTable.insert('',END,values=data)
        searchwindow.destroy()

    print("Search item window opened.")
    searchwindow = CTkToplevel()
    searchwindow.title('Search Item')
    searchwindow.resizable(0, 0)
    searchwindow.grab_set()
    searchwindow.geometry('230+130')

    idLabel = CTkLabel(searchwindow, text='Id', font=('arial', 14, 'bold'))
    idLabel.grid(padx=20, pady=15, sticky=W)
    idEntry = CTkEntry(searchwindow, font=('arial', 13, 'bold'))
    idEntry.grid(row=0, column=1, padx=20, pady=15)

    nameLabel = CTkLabel(searchwindow, text='Name', font=('arial', 14, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = CTkEntry(searchwindow, font=('arial', 13, 'bold'))
    nameEntry.grid(row=1, column=1, padx=20, pady=15)

    quantityLabel = CTkLabel(searchwindow, text='Quantity', font=('arial', 14, 'bold'))
    quantityLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    quantityEntry = CTkEntry(searchwindow, font=('arial', 13, 'bold'))
    quantityEntry.grid(row=2, column=1, padx=20, pady=15)

    supplierLabel = CTkLabel(searchwindow, text='Supplier', font=('arial', 14, 'bold'))
    supplierLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    supplierEntry = CTkEntry(searchwindow, font=('arial', 13, 'bold'))
    supplierEntry.grid(row=3, column=1, padx=20, pady=15)

    dateLabel = CTkLabel(searchwindow, text='Date Added', font=('arial', 14, 'bold'))
    dateLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    dateEntry = CTkEntry(searchwindow, font=('arial', 13, 'bold'))
    dateEntry.grid(row=4, column=1, padx=20, pady=15)

    searchItemButton = CTkButton(searchwindow, text='Search Item', corner_radius=10, cursor='hand2', fg_color='#78C0BC', text_color='white',command=search_data)
    searchItemButton.grid(row=5, columnspan=2, pady=40)


def add_item():
    print("Add item window opened.")  # Debug print
    def add_data():
        if idEntry.get() == '' or nameEntry.get() == '' or quantityEntry.get() == '' or supplierEntry.get() == '' or dateEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                query = 'INSERT INTO item VALUES (%s, %s, %s, %s, %s)'
                mycursor.execute(query, (idEntry.get(), nameEntry.get(), quantityEntry.get(), supplierEntry.get(), dateEntry.get()))
                con.commit()
                result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?')
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    quantityEntry.delete(0, END)
                    supplierEntry.delete(0, END)
                    dateEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'Id cannot be repeated')
                return

            query = 'SELECT * FROM item'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            itemTable.delete(*itemTable.get_children())
            for data in fetched_data:
                datalist = list(data)
                itemTable.insert('', END, values=datalist)
        addwindow.destroy()

    addwindow = CTkToplevel()
    addwindow.title('Add Item')
    addwindow.resizable(0, 0)
    addwindow.grab_set()
    addwindow.geometry('230+130')

    idLabel = CTkLabel(addwindow, text='Id', font=('arial', 14, 'bold'))
    idLabel.grid(padx=20, pady=15, sticky=W)
    idEntry = CTkEntry(addwindow, font=('arial', 13, 'bold'))
    idEntry.grid(row=0, column=1, padx=20, pady=15)

    nameLabel = CTkLabel(addwindow, text='Name', font=('arial', 14, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = CTkEntry(addwindow, font=('arial', 13, 'bold'))
    nameEntry.grid(row=1, column=1, padx=20, pady=15)

    quantityLabel = CTkLabel(addwindow, text='Quantity', font=('arial', 14, 'bold'))
    quantityLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    quantityEntry = CTkEntry(addwindow, font=('arial', 13, 'bold'))
    quantityEntry.grid(row=2, column=1, padx=20, pady=15)

    supplierLabel = CTkLabel(addwindow, text='Supplier', font=('arial', 14, 'bold'))
    supplierLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    supplierEntry = CTkEntry(addwindow, font=('arial', 13, 'bold'))
    supplierEntry.grid(row=3, column=1, padx=20, pady=15)

    dateLabel = CTkLabel(addwindow, text='Date Added', font=('arial', 14, 'bold'))
    dateLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    dateEntry = CTkEntry(addwindow, font=('arial', 13, 'bold'))
    dateEntry.grid(row=4, column=1, padx=20, pady=15)

    addItemButton = CTkButton(addwindow, text='Add Item', corner_radius=10, cursor='hand2', fg_color='#78C0BC', text_color='white', command=add_data)
    addItemButton.grid(row=5, columnspan=2, pady=40)


def connect_database():
    def connect():
        global mycursor
        global con
        try:
            con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()
            messagebox.showinfo('Success', 'Database connection is successful')

            query = 'CREATE DATABASE IF NOT EXISTS inventorymanagementsystem'
            mycursor.execute(query)
            con.commit()
            # mycursor.close()
            # con.close()
            query='USE inventorymanagementsystem'
            mycursor.execute(query)
            query='CREATE TABLE IF NOT EXISTS item(id int not null primary key,name varchar(30),quantity varchar(5),supplier varchar(30),dateadded varchar(10))'
            mycursor.execute(query)

        except pymysql.MySQLError as e:
            messagebox.showerror('Error', f'Error connecting to database: {e}')
        connectWindow.destroy()

    print("Database connection window opened.")
    connectWindow = CTkToplevel()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    hostnameLabel = CTkLabel(connectWindow, text='Host Name', font=('arial', 13, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20, pady=10)
    hostEntry = CTkEntry(connectWindow, width=200)
    hostEntry.grid(row=0, column=1, padx=20, pady=10)

    usernameLabel = CTkLabel(connectWindow, text='User Name', font=('arial', 13, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20, pady=10)
    userEntry = CTkEntry(connectWindow, width=200)
    userEntry.grid(row=1, column=1, padx=20, pady=10)

    passwordLabel = CTkLabel(connectWindow, text='Password', font=('arial', 13, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20, pady=10)
    passwordEntry = CTkEntry(connectWindow, width=200, show='*')
    passwordEntry.grid(row=2, column=1, padx=20, pady=10)

    connectButton = CTkButton(connectWindow, text='Connect', corner_radius=10, cursor='hand2', fg_color='#78C0BC', text_color='white', command=connect)
    connectButton.grid(row=3, column=1, padx=20, pady=40)


window=CTk()
window.geometry('930x580')
window.resizable(False,False)
window.title('Inventory Management System')
# window.configure(fg_color='black')
logo=CTkImage(Image.open('inventory.jpeg'),size=(930,158))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)

connectButton=CTkButton(window,text='Connect Database',corner_radius=10,bg_color='#6DC09D',cursor='hand2',fg_color='#FFFFFF',text_color='green',command=connect_database)
connectButton.place(x=730,y=0)

leftFrame=CTkFrame(window)
leftFrame.grid(row=1,column=0)

# idLabel=CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'))
# idLabel.grid(row=0,column=0,padx=20)

# idEntry=CTkEntry(leftFrame,font=('arial',15,'bold',),width=180)
# idEntry.grid(row=0,column=1)

# nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'))
# nameLabel.grid(row=1,column=0,padx=20)

# nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold',),width=180)
# nameEntry.grid(row=1,column=1)

addItemButton=CTkButton(leftFrame,text='Add Item',corner_radius=10,cursor='hand2',fg_color='#78C0BC',text_color='white',command=add_item)
addItemButton.grid(row=0,column=0,padx=20,pady=20)

searchItemButton=CTkButton(leftFrame,text='Search Item',corner_radius=10,cursor='hand2',fg_color='#78C0BC',text_color='white',command=search_item)
searchItemButton.grid(row=1,column=0,padx=20,pady=20)

deleteItemButton=CTkButton(leftFrame,text='Delete Item',corner_radius=10,cursor='hand2',fg_color='#78C0BC',text_color='white',command=delete_item)
deleteItemButton.grid(row=2,column=0,padx=20,pady=20)

updateItemButton=CTkButton(leftFrame,text='Update Item',corner_radius=10,cursor='hand2',fg_color='#78C0BC',text_color='white',command=update_item)
updateItemButton.grid(row=3,column=0,padx=20,pady=20)

showItemsButton=CTkButton(leftFrame,text='Show All',corner_radius=10,cursor='hand2',fg_color='#78C0BC',text_color='white',command=show_item)
showItemsButton.grid(row=4,column=0,padx=20,pady=20)

exitButton=CTkButton(leftFrame,text='Exit',corner_radius=10,cursor='hand2',fg_color='#78C0BC',text_color='white',command=exit)
exitButton.grid(row=5,column=0,padx=20,pady=20)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

itemTable=ttk.Treeview(rightFrame,height=13)
itemTable.grid(row=1,column=0,columnspan=4)

itemTable['columns']=('Id','Name','Quantity','Supplier','Added Date')

itemTable.heading('Id',text='Id')
itemTable.heading('Name',text='Name')
itemTable.heading('Quantity',text='Quantity')
itemTable.heading('Supplier',text='Supplier')
itemTable.heading('Added Date',text='Added Date')

itemTable.config(show='headings')

itemTable.column('Id',width=80,anchor=CENTER)
itemTable.column('Name',width=160,anchor=CENTER)
itemTable.column('Quantity',width=80,anchor=CENTER)
itemTable.column('Supplier',width=200,anchor=CENTER)
itemTable.column('Added Date',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',13,'bold'))

connectButton.lift()

window.mainloop()