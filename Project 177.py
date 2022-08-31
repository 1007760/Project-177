from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Project 177")
name = Label(root, text = "Name : ")
name.place(relx = 0.5, rely = 0.1, anchor = CENTER)
entry1 = Entry(root)
entry1.place(relx = 0.5, rely = 0.2, anchor = CENTER)
password = Label(root, text = "Password : ")
password.place(relx = 0.5, rely = 0.3, anchor = CENTER)
entry2 = Entry(root)
entry2.place(relx = 0.5, rely = 0.4, anchor = CENTER)
captcha = Label(root, text = "Captcha : ")
captcha.place(relx = 0.5, rely = 0.5, anchor = CENTER)
entry3 = Entry(root)
entry3.place(relx = 0.5, rely = 0.6, anchor = CENTER)
user = Label(root)
user.place(relx = 0.5, rely = 0.7, anchor = CENTER)
show_captcha = Label(root, text = "Captca : ")
show_captcha.place(relx = 0.5, rely = 0.8, anchor = CENTER)
entry4 = Entry(root)
entry4.place(relx = 0.5, rely = 0.9, anchor = CENTER)
label1 = Label(root)
label2 = Label(root)
label3 = Label(root)
label1.pack()
label2.pack()
label3.pack()

class userDB :
    def __init__(self) :
        self.username = "Yeet183"
        self.password = "red184*"
        self.captcha = 1028
        
    def showUser(self) :
        name['text'] = "Name : " + self.username
        password['text'] = "Password : " + self.password
        captcha['text'] = "Captcha : " + self.captcha

obj1 = userDB()

def addUser():
    global obj1
    username = "De172"
    name['text'] = self.username
    captcha = 1928
    Captcha['text'] = self.captcha
    print("Details Updated")

btn1 = Button(root, text = "Update Login Details", command = addUser)
btn1.pack()
btn2 = Button(root, text = "Show Profile", command = obj1.showUser())
btn2.pack()
root.mainloop()