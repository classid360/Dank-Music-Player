import pygame
import pygame.mixer as mixer
from tkinter import *
from tkinter import messagebox

mixer.init()

def play():
    pygame.mixer.music.load('C:\\Users\\admin\\Desktop\\dev\\Python\\Media Player\\example_wav.wav')
    pygame.mixer.music.play()
 
def pause():
    pygame.mixer.music.pause()
 
def unpause():
    pygame.mixer.music.unpause()

def quit():
    pygame.mixer.quit()
    root.destroy()
                     
pygame.init()
 
root = Tk()
root.geometry('400x200')
 
myframe = Frame(root)
myframe.pack()
 
mylabel = Label(myframe, text = "Dank Music Player")
mylabel.pack()
 
button1 = Button(myframe, text = "Play", command = play, width = 45, background = "grey", activebackground = "red")
button1.pack(pady = 5)
button3 = Button(myframe, text = "Resume", command = unpause, width = 45, background = "grey", activebackground = "red")
button3.pack(pady = 5)
button4 = Button(myframe, text = "Pause", command = pause, width = 45, background = "grey", activebackground = "red")
button4.pack(pady = 5)
button5 = Button(myframe, text = "Quit", command = quit, width = 45, background = "grey", activebackground = "red")
button5.pack(pady = 5)

root.mainloop()
