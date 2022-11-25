# Initializacion Library Python 3.x
        # Initializate Library Python 2.x
# Import the system functions
from os import system
# Import the tkinter Function
from tkinter import *
# Import the Tkinter Message box
from tkinter import messagebox
# Import Module Image
from PIL import Image, ImageTk

# Create the Tk App
root=Tk()

# Create the name app
root.title('App')
# Gestionate the geometry of the programm ( Not Modified )
root.geometry('1024x768+300+200')
# Config the background color
root.configure(bg="#fff")
# With this command this validate if the programm has modified in the borders 
root.resizable(False,False)

# Positionate the image logo and gestionate the places 
img = PhotoImage(file="logo.png")
Label(root,image=img,bg='white').place(x=50,y=50)

# Positionate the image and gestionate the places 
img = PhotoImage(file="12.png")
Label(root,image=img,bg='white').place(x=50,y=50)

# Write or draw a box-content
frame=Frame(root,width=350,height=350,bg="red")
# Modified the place of the image
frame.place(x=480,y=70)


# Execute the functions
        # Execute the Tkinter Function init
root.mainloop()

