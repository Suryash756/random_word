from tkinter import*
import random

root = Tk()
root.title("random_word_generator")
root.geometry("400x400")
root.configure(background="cyan")
show = Label(root,bg="cyan",fg="black")
def word1():
    list_alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    random1 = random.randint(0,25)
    random2 = random.randint(0,25)
    random3 = random.randint(0,25)
    random4 = random.randint(0,25)
    random5 = random.randint(0,25)
    
    a=list_alph[random1]
    b=list_alph[random2]
    c=list_alph[random3]
    d=list_alph[random4]
    e=list_alph[random5]
    show["text"] ="word = "+str(a)+str(b)+str(c)+str(d)+str(e)

btn = Button(root,text="show the word",bg="yellow",fg="black",command=word1)
btn.place(rely=0.5,relx=0.5,anchor=CENTER)
show.place(rely=0.7,relx=0.5,anchor=CENTER)
root.mainloop()