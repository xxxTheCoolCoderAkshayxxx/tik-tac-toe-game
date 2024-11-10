from tkinter import *
import tkinter as Tk
from tkinter.ttk import *
from tkinter import messagebox
class Tiktacto:
    def __init__(self,root):
        self.root=root
        self.root.title("tic tac toe")
        self.currentplayer="X"
        self.buttons=[[None for i in range(3)]for i in range(3)]
        self.createwidget()
    def createwidget(self):
        for r in range(3):
            for c in range(3):
                button=Tk.Button(self.root,text="",font=("Times New Roman",40),width=5,height=2,command=lambda r=r,c=c:self.on_button_click(r,c))
                button.grid(row=r,column=c)
                self.buttons[r][c]=button
    
    def on_button_click(self,r,c):
        if self.buttons[r][c]["text"]=="" and not self.checkwinner():
            self.buttons[r][c]["text"]=self.currentplayer
            if self.checkwinner():
                messagebox.showinfo("Game Over",f"player {self.currentplayer} wins")
                self.resetgame()
            elif self.isboardfull():
                messagebox.showinfo("Game Over","Nobody won")
                self.resetgame()
            else:
                # read from the if currentplayer is x then change the current player to O if not let it remain as o
                self.currentplayer="O" if self.currentplayer == "X" else "X"
    
    def checkwinner(self):
        for r in range(3):
            if self.buttons[r][0]["text"]==self.buttons[r][1]["text"]==self.buttons[r][2]["text"]!="":
                return True
        for c in range(3):
            if self.buttons[0][c]["text"]==self.buttons[1][c]["text"]==self.buttons[2][c]["text"]!="":
                return True
        if self.buttons[0][0]["text"]==self.buttons[1][1]["text"]==self.buttons[2][2]["text"]!="":
            return True
        if self.buttons[0][2]["text"]==self.buttons[1][1]["text"]==self.buttons[2][0]["text"]!="":
            return True
        return False
    
    def isboardfull(self):
        return all(self.buttons[r][c] ["text"]!="" for r in range(3) for c in range(3))
    
    def resetgame(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]["text"]=""
        self.currentplayer="X"
if __name__=="__main__":
    root=Tk.Tk()
    game=Tiktacto(root)
    root.mainloop()
    
    
        
        
        




                







