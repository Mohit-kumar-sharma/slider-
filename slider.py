from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("700x300")
root.title("Slider")

def getdollars():
    print(f"we have created {myslider.get()} dollars to your bank account")
    tmsg.showinfo("Account credited",f"we have created {myslider.get()} dollars to your bank account ")


label=Label(root,text="How many dolloars do you want").pack()
myslider=Scale (root , from_=0, to=100, orient="horizontal",tickinterval=50)
myslider.pack()
Button=Button(root,text="Get Dollars", pady=20, command=getdollars)
Button.pack()



root.mainloop()