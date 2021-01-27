import tkinter
from PIL import Image, ImageTk
import random

#create window
root = tkinter.Tk()
root.geometry('400x400')
root.title('Hameed Project "dice simulator"')

# creating label
blanklabel = tkinter.Label(root, text = "=================" )
blanklabel.pack()

HeadingLabel = tkinter.Label(root, text = 'Dice simulator', fg = 'white', bg = 'red', font = 'Helvetica 16 bold')
HeadingLabel.pack()

# config the dice images
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
diceimage = ImageTk.PhotoImage(Image.open(random.choice(dice)))


# create label for image
imageLabel = tkinter.Label(root, text = 'dice image not found', image = diceimage)
imageLabel.image = diceimage
imageLabel.pack(expand = True)

# creating a button
def dieroll():
    diceimage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    imageLabel.configure(image = diceimage)
    imageLabel.image = diceimage

button = tkinter.Button(root, text = "Roll the die", fg = 'red', command = dieroll)
button.pack(expand = True)

#loop the window
root.mainloop()
