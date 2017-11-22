from tkinter import *
import tkinter.messagebox
import os

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            checkWinner()
            player = "O"
            button["bg"] = "yellow"
      else :
            checkWinner()
            player = "X"
            button["bg"] = "lightgreen"
            
      


def checkWinner():
      if list[0]["text"] == list[1]["text"] == list[2]["text"] != "     ":
            playerwin()   
      elif list[3]["text"] == list[4]["text"] == list[5]["text"] != "     ":
            playerwin()
      elif list[6]["text"] == list[7]["text"] == list[8]["text"] != "     ":
            playerwin()
      elif list[0]["text"] == list[3]["text"] == list[6]["text"] != "     ":
            playerwin()
      elif list[1]["text"] == list[4]["text"] == list[7]["text"] != "     ":
            playerwin()
      elif list[2]["text"] == list[5]["text"] == list[8]["text"] != "     ":
            playerwin()
      elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
            playerwin()
      elif list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
            playerwin()

def playerwin():
      if player == "X":
            tkinter.messagebox.showinfo("","Player1 Win!, Close the Window")
            os._exit(0)
      else:
            tkinter.messagebox.showinfo("","Player2 Win!, Close the Window")
            os._exit(0)
      

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)



window.mainloop()


