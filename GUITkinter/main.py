from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import *

root = Tk()
root.title("Regular Expression Simulator")
root.config(bg="#F5FFFA")

#pencerenin boyutlari ve ekranin ortasinda acilmasi
width = 1050
height = 550
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(0, 0)


#help menu
def tip():
    tkinter.messagebox.showinfo('Tip', 'Click the DELETE button, enter your regEx and select text file.\n'
                                       'Choose your option for the transformation (NFA/DFA).\n'
                                       'Click the "Start Simulation" button.')

menubar = Menu(root)
help = Menu(menubar, tearoff=0)
menubar.add_command(label="Help", command=tip)
root.config(menu=menubar)

label = Label(text="Regular Expression to NFA / DFA", font="Arial 22 ", fg="#BC8F8F", bg="#F5FFFA").pack()


#arayüz ikiye bölünür
left_frame = Frame(bg="#F5FFFA", width=600, height=520, highlightbackground="#DCDCDC", highlightcolor="#DCDCDC", highlightthickness=1)
left_frame.pack(side="left")
right_frame = Frame(bg="#F5FFFA", width=450, height=520, highlightbackground="#DCDCDC", highlightcolor="#DCDCDC", highlightthickness=1)
right_frame.pack(side="left")

#kullanicidan regEx alinir
Label(right_frame, text="Enter your regular expression:", bg="#F5FFFA").place(x=26, y=30)
e1 = Entry(right_frame, width=54, borderwidth=4)
e1.place(x=30, y=55)
e1.insert(INSERT, '(a(ab)|c)*')


#metin secme
def openfile():
    select = askopenfilename(initialdir="Desktop", title="Open File", filetypes=(("text files", "*.txt"), ("all files", "*.*")))

    try:
        with open(select) as fileinput:
            Output1.insert(END, fileinput.read())
    except:
        print("No File Selected")


Label(right_frame, text="Select Text", width=50, borderwidth=4, relief="groove", justify=RIGHT).place(x=30, y=100)
b1=Button(right_frame, text=" ... ", borderwidth=2, relief="groove", width=4, command=openfile).place(x=382, y=100)

Output1 = Text(right_frame, height=13, width=35, bg="white", font="Arial")
Output1.place(x=30, y=123)


#regEx'lerin NFA ve DFA dönüsüm fonksiyonlari
def regExToNFA():
    Output2.insert(END, e1.get() + " to NFA")


def regExToDFA():
    Output2.insert(END,  e1.get() + " to DFA")

#secilen buttonlara göre dönüsümün gerceklesmesi ve basilmasi
Label(right_frame, text="Choose an option:", bg="#F5FFFA").place(x=26, y=428)

b2 = Button(right_frame, text="NFA", fg="white", font="bold", bg="#BC8F8F", width=7, borderwidth=3, relief="raised", command=regExToNFA).place(x=30, y=452)
b3 = Button(right_frame, text="DFA", fg="white", font="bold", bg="#BC8F8F", width=7, borderwidth=3, relief="raised", command=regExToDFA).place(x=150, y=452)

Label(left_frame, text="Entered Regular Expression:", bg="#F5FFFA").place(x=32, y=30)
Output2 = Text(left_frame, height=5, width=48, bg="light cyan", font="Arial")
Output2.place(x=35, y=55)



#simülasyonun yansitilmasi
Label(left_frame, text="Simulation:", bg="#F5FFFA").place(x=32, y=190)
c=Canvas(left_frame, height=255, width=530, bg="white")
c.place(x=35, y=210)


#girilen, basilan ifade ve metin dosyasi silinir
def delete():
   Output1.delete("1.0", "end")
   Output2.delete("1.0", "end")
   e1.delete(0, "end")

b4 = Button(right_frame, text="DELETE", width=7, relief="groove", command=delete).place(x=360, y=54)


#ifadenin eslesip eslesmedigi kontrol edilir
def find():
    # remove tag 'found' from index 1 to END
    Output1.tag_remove('found', '1.0', END)

    # returns to widget currently in focus
    s = e1.get()
    if s:
        idx = '1.0'
        while 1:
            # searches for desried string from index 1
            idx = Output1.search(s, idx, nocase=1, stopindex=END)

            if not idx:
                  break

            # last index sum of current index and
            # length of text
            lastidx = '%s+%dc' % (idx, len(s))

            # overwrite 'Found' at idx
            Output1.tag_add('found', idx, lastidx)
            idx = lastidx

        # mark located string
        Output1.tag_config('found', foreground="white", background='#9ACD32')

    e1.focus_set()




b5 = Button(left_frame, text="Start Simulation", width=13, relief="groove", command=find).place(x=469, y=470)


root.mainloop()
