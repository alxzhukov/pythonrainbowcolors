from tkinter import *

root  = Tk()

root.title(' Цвета Радуги')
root.iconbitmap('C:/Users/User/Desktop/lessons/tkinter/logo.ico')
root.geometry('600x400+475+200')
root.resizable(False,True)
# root.config(bg='white')
root['bg']='white'
colors= {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый",

}

class MyButtons:
    def __init__(self,master,textcolor,hexcolor):
        self.textcolor=textcolor
        self.hexcolor= hexcolor
        self.b = Button(root,bg=hexcolor,command=self.get_color)
        self.b.pack(fill=X)
    def get_color(self):
        color_name['text']=self.textcolor
        color_code.delete(0,END)
        color_code.insert(0,self.hexcolor)

color_name=Label(root)
color_code=Entry(root,justify='center')
color_name.pack(fill=X)
color_code.pack()
for k, v in colors.items():
    MyButtons(root, v, k )


root.mainloop()