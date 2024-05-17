import tkinter as tk 
import random


count=0

def new():
    result1.config(text="Random Number Generated Successfully ...")
    global rand 
    rand = random.randint(0,100)
    

def trying():
    
    num=int(textbox.get())
         
    if num==rand:
             result1.config(text="Your guessed it right !! ")
            
    
    elif num < rand:
             result1.config(text="Try with bigger number")
    
    elif num > rand:
             result1.config(text="Try with smaller number")  
    
    elif num != rand:
             result1.config(text="Generate the number first ")
    
    
    
   

root = tk.Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("Guess the Number ")
root.configure(bg="orange")

label = tk.Label(root, text="Guess the Random Number ", font=("Arial",20,'bold'),bg="orange")
label.pack(pady=15)

button = tk.Button(root, text="Generate Number", font=("Arial", 14), command=new)
button.pack(pady=15)

entry_label= tk.Label(root, text="Enter your Guess", font=("Arial", 14),bg="orange")
entry_label.pack()

textbox = tk.Entry(root, font=("Arial",14))
textbox.pack(pady=10)


button = tk.Button(root, text="Try", font=("Arial", 14), command=trying)
button.pack()



result1 = tk.Label(root, text="", font=("Arial",12),bg="orange")
result1.pack(pady=10)


root.mainloop()