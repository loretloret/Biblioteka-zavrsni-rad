from stranice import *

# Ograničiti pristup stranicama Zaposli i Otpusti sasmo za šefa, odnosno, onog zaposlenog čije polje šef
# ima vrednost True.
# Ograničiti pristup stranicama Izdaj knjigu, Vrati knjigu, Dodaj knjigu i Izdaci knjigu za zaposlene koji
# su prijavljeni, odnosno, onog zaposlenog čije polje jePrijavljen ima vrednost True.
# Na kraju kreirati objekat GUI sa dimenzijama 1200x600


class GUI(Tk):
    def __init__(self, **kwargs):
        Tk.__init__(self, **kwargs)
        self.title("Biblioteka Sad ili Nikad")

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.stranice = dict()

        meni = Menu(container)

        zmeni = Menu(meni, tearoff=0)
        zmeni.add_command(label='Registracija', command=lambda: self.prikazi_stranicu(Registracija))
        zmeni.add_command(label='Login', command=lambda: self.prikazi_stranicu(Login))
        zmeni.add_separator()
        zmeni.add_command(label='Zaposli', command=lambda: self.provera(Zaposli))
        zmeni.add_command(label='Otpusti', command=lambda: self.provera(Otpusti))
        zmeni.add_separator()
        zmeni.add_command(label='Izlaz', command=self.destroy)

        meni.add_cascade(menu=zmeni, label="Zaposleni")

        self.kmeni = Menu(meni, tearoff=0)
        self.kmeni.add_command(label='Izdaj knjigu', command=lambda: self.provera(IzdajKnjigu))
        self.kmeni.add_command(label='Vrati knjigu', command=lambda: self.provera(VratiKnjigu))
        self.kmeni.add_separator()
        self.kmeni.add_command(label='Dodaj knjigu', command=lambda: self.provera(DodajKnjigu))
        self.kmeni.add_command(label='Izbaci knjigu', command=lambda: self.provera(IzbaciKnjigu))

        meni.add_cascade(menu=self.kmeni, label="Knjige")

        Tk.config(self, menu=meni)

        for s in (PocetnaStranica, Registracija, Login, Zaposli, Otpusti, IzdajKnjigu, VratiKnjigu, DodajKnjigu,
                  IzbaciKnjigu):
            stranica = s(container, self)
            self.stranice[s] = stranica
            stranica.grid(row=0, column=0, sticky='NSEW')

        self.prikazi_stranicu(PocetnaStranica)

    def prikazi_stranicu(self, cont):
        stranica = self.stranice[cont]
        stranica.tkraise()

    def provera(self, cont):
        if biblioteka.jeprijavljen:
            self.prikazi_stranicu(cont)
        else:
            self.prikazi_stranicu(Login)


IS = GUI()
IS.geometry("1200x600")
IS.mainloop()
