from tkinter import * 
from meta import folder_generate


folder = folder_generate.Mkdir.mkdir
root = Tk()#オブジェクトのインスタンス定義

#メソッド定義
root.title('folder and file generate')
root.geometry('500x500')
root.configure(bg = 'green')
frame = Frame(root)
sc = Scrollbar(frame)
sc.pack(side=RIGHT, fill=Y)

result = Listbox(frame, width=50, height=10,yscrollcommand=sc.set,bg = 'lightgreen')
result.pack(side=LEFT, fill=BOTH, pady=10)


  
  
    


btn = Button(root, text="決定",width = 25, font=("Courier", 10),bg='salmon2',fg = 'green',command=folder)
btn.place(x = 250,y = 250)

frame.pack()




def enter_function(event):
    btn.invoke()

root.bind('<Return>', enter_function)






root.mainloop()