import tkinter as tk                # python 3
from tkinter import font as tkfont

hesapA = {
    'ad': 'Sena Aydin',
    'sifre': '1234',
    'hesapNo': '007',
    'bakiye': 30000,
    'ekHesap': 20000
}
hesapB = {
    'ad': 'Ahsen Aydin',
    'sifre': '123',
    'hesapNo': '061',
    'bakiye': 44000,
    'ekHesap': 50000
}




class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Menu, Islem):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg='#2F4F4F')
        self.controller = controller
        self.controller.title('ATM')
        self.controller.state('zoomed')
        self.controller.iconphoto(False, tk.PhotoImage(file='C:/Users/asena/OneDrive/Bilder/atm.png'))

        headingLabel1 = tk.Label(self, text='ATM', font=('helvetica',45,'bold'), foreground='white',background='#2F4F4F')
        headingLabel1.pack(pady=25)

        space_Label = tk.Label(self,height=4,bg='#2F4F4F')
        space_Label.pack()

        hesapAdi_Label = tk.Label(self, text='Hesap Adi', font=('otbitron', 13), bg='#2F4F4F', fg='white')
        hesapAdi_Label.place(x=668,y=160)

        ad = tk.StringVar()
        hesapAdi = tk.Entry(self, textvariable=ad, font=('helvetica', 12), width=22)
        hesapAdi.focus_set()
        hesapAdi.pack()

        password_Label = tk.Label(self, text='Sifre',font=('otbitron',13),bg='#2F4F4F',fg='white')
        password_Label.pack()


        sifre=tk.StringVar()
        password=tk.Entry(self,textvariable=sifre,font=('helvetica',12),width=22)
        password.focus_set()
        password.pack()




        def check():
            if (hesapAdi_Label.get == 'hesapA'):
                if (hesapA.get('sifre') == sifre):
                    print(f"Merhaba {hesapA.get('ad')}")
                controller.show_frame('Menu')
            elif (hesapAdi_Label.get == 'hesapB'):
                if (hesapB.get('sifre') == sifre):
                    print(f"Merhaba {hesapB.get('ad')}")
            else:
                incorrect_password_label['text']='Sifre yanlis'
        enter_button=tk.Button(self, text='GIRIS',command=check,relief='raised',borderwidth=3,width=15, height=2)
        enter_button.pack(pady=10)

        incorrect_password_label=tk.Label(self, text='',font=('helvetice',13),fg='white',bg='#2F4F4F',anchor='n')
        incorrect_password_label.pack(fill='both', expand=True)


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#2F4F4F')
        self.controller = controller

        headingLabel = tk.Label(self, text='ATM', font=('helvetica', 45, 'bold'), foreground='white',
                                 background='#2F4F4F')
        headingLabel.pack(pady=25)

        miktargir=tk.Label(self, text='Cekilecek miktari girin.',font=('helvetica',13),fg='white',bg='#2F4F4F')
        miktargir.pack(pady=10)

        amount_entry_box = tk.Entry(self, font=('helvetica', 12), width=22)
        amount_entry_box.focus_set()
        amount_entry_box.pack(ipady=7)

        def paraCek(hesap, miktar):
            controller.show_frame('Islem')


        enter_button1 = tk.Button(self, text='GIRIS', command=paraCek, relief='raised', borderwidth=3, width=28,
                                 height=3)
        enter_button1.pack(pady=10)


class Islem(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#2F4F4F')
        self.controller = controller

        headingLabel2 = tk.Label(self, text='ATM', font=('helvetica', 45, 'bold'), foreground='white',
                                background='#2F4F4F')
        headingLabel2.pack(pady=25)


"""
        index = list(hesap)
        if (hesap.get('bakiye') >= miktar):
            hesap['bakiye'] = hesap['bakiye'] - miktar
            print('Paranizi Alabilirsiniz.')
        else:
            toplam = hesap.get('bakiye') + hesap.get('ekHesap')

            if (toplam >= miktar):
                ekHesapKullanimi = input('Ek Hesap kullanilsin mi? (E/H)')

                if ekHesapKullanimi == 'e':
                    hesap['ekHesap'] = hesap.get('ekHesap') + (hesap.get('bakiye') - miktar)
                    hesap['bakiye'] = 0
                    print('Bakiyeniz sıfırlanmıştır!')
                    print(f"Ek Hesap Kalan Bakiyeniz {hesap['ekHesap']} TL")
                    print('Paranizi Alabilirsiniz.')

                else:
                    print(f"{hesap.get('hesapNo')} nolu hesabinizda {hesap.get('bakiye')} bulunuyor.")

            else:
                print('Yetersiz bakiye.')

        print(f"Kalan Bakiyeniz {hesap['bakiye']} TL")
"""

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()




"""
hesapA= {
    'ad': 'Sena Aydin',
    'sifre': '1234',
    'hesapNo':'007',
    'bakiye':30000,
    'ekHesap':20000
}
hesapB= {
    'ad': 'Ahsen Aydin',
    'sifre': '123',
    'hesapNo':'061',
    'bakiye':44000,
    'ekHesap':50000
}


def paraCek(hesap,miktar):

    index = list(hesap)

    if (hesap.get('bakiye') >= miktar):
        hesap['bakiye'] = hesap['bakiye'] - miktar
        print('Paranizi Alabilirsiniz.')
    else:
        toplam = hesap.get('bakiye')+ hesap.get('ekHesap')

        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek Hesap kullanilsin mi? (E/H)')

            if ekHesapKullanimi == 'e':
                hesap['ekHesap'] = hesap.get('ekHesap') + (hesap.get('bakiye') - miktar)
                hesap['bakiye'] = 0
                print('Bakiyeniz sıfırlanmıştır!')
                print(f"Ek Hesap Kalan Bakiyeniz {hesap['ekHesap']} TL")
                print('Paranizi Alabilirsiniz.')
            
            else:
                print(f"{hesap.get('hesapNo')} nolu hesabinizda {hesap.get('bakiye')} bulunuyor.")

        else:
            print('Yetersiz bakiye.')
    
    print(f"Kalan Bakiyeniz {hesap['bakiye']} TL")



hesap = input('Hesap adi: ')
sifre = input('Sifre giriniz: ')
if (hesap == 'hesapA'):
    if (hesapA.get('sifre') == sifre):
        print(f"Merhaba {hesapA.get('ad')}")
        miktar = int(input("Cekilecek miktar: "))
        paraCek(hesapA,miktar)

elif (hesap == 'hesapB'):
    if (hesapB.get('sifre') == sifre):
        print(f"Merhaba {hesapB.get('ad')}")        
        miktar = int(input("Cekilecek miktar: "))
        paraCek(hesapB,miktar)

else:
    print('Sifre yanlis.')
"""