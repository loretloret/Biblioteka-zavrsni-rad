from tkinter import *
from klase import biblioteka

# Kreirati klase:
# • PocetnaStranica
# • Registracija
# • Login
# • IzdajKnjigu
# • VratiKnjigu
# • DodajKnjigu
# • IzbaciKnjigu
# • Zaposli
# • Otpusti


class PocetnaStranica(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text="DOBRODOSLI \n Biblioteka 'Sad ili nikad'", font='Times 20 bold',
              bg="lightblue").pack(pady=250)


class Registracija(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Registracija', font='Times 16 bold', bg="lightblue").pack(pady=50)
        lf1 = LabelFrame(self, text='Ime i Prezime')
        lf1.pack(pady=5)
        e1 = Entry(lf1)
        e1.pack(pady=5, padx=5)
        lf2 = LabelFrame(self, text='JMBG')
        lf2.pack(pady=5)
        e2 = Entry(lf2)
        e2.pack(pady=5, padx=5)
        lf3 = LabelFrame(self, text='Username')
        lf3.pack(pady=5)
        e3 = Entry(lf3)
        e3.pack(pady=5, padx=5)
        lf4 = LabelFrame(self, text='Password')
        lf4.pack(pady=5)
        e4 = Entry(lf4)
        e4.pack(pady=5, padx=5)

        def registracija():
            succsess = biblioteka.registracija_zaposlenog(e1.get(), e2.get(), e3.get(), e4.get())
            if succsess:
                l1.configure(text='Registracija je uspesno zavrsena!')
            else:
                l1.configure(text='Registracija nije bila uspesna, korisnik vec postoji!')

        b1 = Button(self, text='Registracija', command=lambda: registracija())
        b1.pack(pady=10)
        l1 = Label(self, bg="lightblue")
        l1.pack()


class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Login', font='Times 16 bold', bg="lightblue").pack(pady=50)
        lf1 = LabelFrame(self, text='Username')
        lf1.pack(pady=5)
        e1 = Entry(lf1)
        e1.pack(pady=5, padx=5)
        lf2 = LabelFrame(self, text='Password')
        lf2.pack(pady=5)
        e2 = Entry(lf2)
        e2.pack(pady=5, padx=5)

        def login():
            succsess = biblioteka.prijava(e1.get(), e2.get())
            if succsess:
                l1.configure(text='Dobrodosli!')
            else:
                l1.configure(text='Pogresno korisnicko ime ili lozinka!')

        b1 = Button(self, text='Prijavi se', command=lambda: login())
        b1.pack(pady=10)
        l1 = Label(self, bg="lightblue")
        l1.pack()


class Zaposli(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Zaposli', font='Times 16 bold', bg="lightblue").pack(pady=50)
        lf1 = LabelFrame(self, text='Ime i Prezime')
        lf1.pack(pady=5)
        e1 = Entry(lf1)
        e1.pack(pady=5, padx=5)
        lf2 = LabelFrame(self, text='JMBG')
        lf2.pack(pady=5)
        e2 = Entry(lf2)
        e2.pack(pady=5, padx=5)
        lf3 = LabelFrame(self, text='Broj telefona')
        lf3.pack(pady=5)
        e3 = Entry(lf3)
        e3.pack(pady=5, padx=5)
        lf4 = LabelFrame(self, text='Diploma')
        lf4.pack(pady=5)
        e4 = Entry(lf4)
        e4.pack(pady=5, padx=5)

        def zaposli():
            succsess = biblioteka.zaposli(e1.get(), e2.get(), e3.get(), e4.get())
            if succsess:
                l1.configure(text='Prijava radnika je bila uspesna!')
            else:
                l1.configure(text='Prijava radnika nije bila uspesna!')

        b1 = Button(self, text='Zaposli', command=lambda: zaposli())
        b1.pack(pady=10)
        l1 = Label(self, bg="lightblue")
        l1.pack()


class Otpusti(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Otpusti', font='Times 16 bold', bg="lightblue").pack(pady=50)
        lf1 = LabelFrame(self, text='Ime i Prezime')
        lf1.pack(pady=5)
        e1 = Entry(lf1)
        e1.pack(pady=5, padx=5)
        b1 = Button(self, text='Otpusti', command=lambda: biblioteka.otpusti(e1.get()))
        b1.pack(pady=10)


class IzdajKnjigu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Izdaj knjigu', font='Times 16 bold', bg="lightblue").pack(pady=50)
        lf1 = LabelFrame(self, text='Naslov')
        lf1.pack(pady=5)
        e1 = Entry(lf1)
        e1.pack(pady=5, padx=5)
        b1 = Button(self, text='Nadji knjigu', command=lambda: biblioteka.nadji_knjigu(e1.get()))
        b1.pack(pady=10)
        l1 = Label(self, bg="lightblue")
        l1.pack()
        b2 = Button(self, text='Izdaj knjigu', command=lambda: biblioteka.izdaj_knjigu(e1.get()))
        b2.pack(pady=10)
        l2 = Label(self, bg="lightblue")
        l2.pack()


class VratiKnjigu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Vrati knjigu', font='Times 16 bold', bg="lightblue").pack(pady=50)
        lf1 = LabelFrame(self, text='Naslov')
        lf1.pack(pady=5)
        e1 = Entry(lf1)
        e1.pack(pady=5, padx=5)
        b1 = Button(self, text='Vrati knjigu', command=lambda: biblioteka.vrati_knjigu(e1.get()))
        b1.pack(pady=10)


class DodajKnjigu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Dodaj knjigu', font='Times 16 bold', bg="lightblue").pack(pady=50)
        lf1 = LabelFrame(self, text='Naslov')
        lf1.pack(pady=5)
        e1 = Entry(lf1)
        e1.pack(pady=5, padx=5)
        lf2 = LabelFrame(self, text='Autor')
        lf2.pack(pady=5)
        e2 = Entry(lf2)
        e2.pack(pady=5, padx=5)
        lf3 = LabelFrame(self, text='Godina izdavanja')
        lf3.pack(pady=5)
        e3 = Entry(lf3)
        e3.pack(pady=5, padx=5)
        lf4 = LabelFrame(self, text='Zemlja porekla')
        lf4.pack(pady=5)
        e4 = Entry(lf4)
        e4.pack(pady=5, padx=5)
        lf5 = LabelFrame(self, text='Jezik')
        lf5.pack(pady=5)
        e5 = Entry(lf5)
        e5.pack(pady=5, padx=5)
        b1 = Button(self, text='Dodaj knjigu', command=lambda: biblioteka.dodaj_knjigu(e1.get(), e2.get(), e3.get(),
                                                                                       e4.get(), e5.get()))
        b1.pack(pady=10)


class IzbaciKnjigu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='lightblue')
        Label(self, text='Izbaci knjigu', font='Times 16 bold', bg="lightblue").pack(pady=50)
        lf1 = LabelFrame(self, text='Naslov')
        lf1.pack(pady=5)
        e1 = Entry(lf1)
        e1.pack(pady=5, padx=5)
        b1 = Button(self, text='Izbaci knjigu', command=lambda: biblioteka.izbaci_knjigu(e1.get()))
        b1.pack(pady=10)
