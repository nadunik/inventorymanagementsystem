from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required.')
    elif usernameEntry.get()=='naduni' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login successful')
        root.destroy()
        import ims
    else:
        messagebox.showerror('Error','Incorrect username or password')

root=CTk()
root.geometry('930x478')
root.resizable(False,False)
root.title('Login Page')
image = CTkImage(Image.open('login.jpeg'), size=(930,478))
imageLabel= CTkLabel(root,image=image,text=' ')
imageLabel.place(x=0,y=0)
topicLabel=CTkLabel(root,text='Inventory Management System',bg_color='#FFFFFF',font=('Gaudy Old Style',20,'bold'),text_color='dark blue')
topicLabel.place(x=20,y=100)

usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username ',width=180,fg_color='#FFFFFF',corner_radius=10,border_color='#3204B8',bg_color='#CCD2EA',text_color='black')
usernameEntry.place(x=50,y=170)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password ',width=180,fg_color='#FFFFFF',corner_radius=10,show='*',border_color='#3204B8',bg_color='#CCD2EA',text_color='black')
passwordEntry.place(x=50,y=220)

loginButton=CTkButton(root,text='Login',corner_radius=10,bg_color='#CCD2EA',cursor='hand2',command=login)
loginButton.place(x=70,y=270)

usernameEntry.lift()
passwordEntry.lift()
loginButton.lift()

root.mainloop()
