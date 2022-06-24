import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Rolling the Dice')


#root.mainloop()

l0 = tkinter.Label(root,text="")
l0.pack()

l1 = tkinter.Label(root, text="Dice Rolling Simulator",fg = "black",
                             font = " Helvetica 16 bold italic")
l1.pack()


dice = ['inverted-dice-1.png','inverted-dice-2.png','inverted-dice-3.png','inverted-dice-4.png','inverted-dice-5.png','inverted-dice-6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root,image=image1)
label1.image = image1


label1.pack(expand = True)

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1
# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='black', command=rolling_dice)
# pack a widget in the parent widget
button.pack( expand=True)

root.mainloop()
