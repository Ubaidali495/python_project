import tkinter as tk
from PIL import Image,ImageTk
import random

window = tk.Tk()
window.geometry()
window.title('Dice Roll')

dice=['C:/Users/HTC/pythonProject12/Lib/site-packages/dice/dice1.png','C:/Users/HTC/pythonProject12/Lib/site-packages/dice/dice2.png','C:/Users/HTC/pythonProject12/Lib/site-packages/dice/dice3.png','C:/Users/HTC/pythonProject12/Lib/site-packages/dice/dice4.png','C:/Users/HTC/pythonProject12/Lib/site-packages/dice/dice5.png','C:/Users/HTC/pythonProject12/Lib/site-packages/dice/dice6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x = 40, y = 100)
label2.place(x = 300,y = 100)
def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2

button = tk.Button(window,text="Roll",bg='blue',fg='white',font='Times 20 bold',command=dice_roll)
button.place(x =200 , y = 0)

window.mainloop()

# with numbers
'''def roll_dice():
    a = random.randint(1,6)
    label = tk.Label(window,text= a).pack()

button = tk.Button(window,text = "click",command=roll_dice)
button.pack()'''
