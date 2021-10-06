# Klasu Zaposleni koja ima sledeća polja:
# • ime_prezime - string
# • JMBG - string
# • br_telefona - string
# • diploma - string
# • username - string
# • password - string
# • šef – boolean(True/False)
# Kreirati konstruktor koji prima argumente ime_prezime, JMBG, br_telefona, diploma, username i
# pasword a polje šef postavlja na False.
# Kreirati metodu za ispis zaposlenog u fomatu:
# [“Zaposleni: ime_prezime\nJMBG: jmbg\nBroj telefona: br_tel\n“]

class Zaposlen:
    def __init__(self, ime_prezime, jmbg, br_telefona, diploma, username, password):
        Zaposlen.validacija(ime_prezime, jmbg, br_telefona, diploma, username, password)
        self.ime_prezime = ime_prezime
        self.jmbg = jmbg
        self.br_telefona = br_telefona
        self.diploma = diploma
        self.username = username
        self.password = password
        self.sef = False

    @staticmethod
    def validacija(ime_prezime, jmbg, br_telefona, diploma, username, password):
        assert type(ime_prezime) == str, "Ime i prezime moraju biti string!"
        assert type(jmbg) == str, "JMBG mora biti string!"
        assert type(br_telefona) == str, "Broj telefona mora biti string!"
        assert type(diploma) == str, "Diploma mora biti string!"
        assert type(username) == str, "Username mora biti string!"
        assert type(password) == str, "Password mora biti string!"

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __str__(self):
        return ["Zaposleni: {} \nJMBG: {} \nBroj telefona: {} \n".format(self.ime_prezime, self.jmbg, self.br_telefona)]


# Klasu Knjiga koja ima sledeća polja:
# • naslov - string
# • autor - string
# • godina_izdavanja - string
# • zemlja_porekla - string
# • jezik - string
# • stanje - string
# Kreirati konstruktor koji prima argumente naslov, autor, godina_izdavanja, zemlja_porekla i jezik, a
# polje stanje postavlja na string „Na stanju“.
# Kreirati metodu za ispis knjige u fomatu:
# [“Naslov: naslov\nAutor: autor\nZemlja porekla: zemlja?porekla\n Jezik originalne verzije: jezik\nStanje: stanje\n“]


class Knjiga:
    def __init__(self, naslov, autor, godina_izdavanja, zemlja_porekla, jezik):
        Knjiga.validacija(naslov, autor, godina_izdavanja, zemlja_porekla, jezik)
        self.naslov = naslov
        self.autor = autor
        self.godina_izdavanja = godina_izdavanja
        self.zemlja_porekla = zemlja_porekla
        self.jezik = jezik
        self.stanje = "Na stanju"

    @staticmethod
    def validacija(naslov, autor, godina_izdavanja, zemlja_porekla, jezik):
        assert type(naslov) == str, "Naslov mora biti string!"
        assert type(autor) == str, "Autor mora biti string!"
        assert type(godina_izdavanja) == str, "Godina izdavanja mora biti string!"
        assert type(zemlja_porekla) == str, "Zemlja porekla mora biti string!"
        assert type(jezik) == str, "Jezik mora biti string!"

    def __str__(self):
        return ["Naslov: {} \nAutor: {} \nZemlja porekla: {} \nJezik originalne verzije: {} \nStanje: {} \n".format(
            self.naslov, self.autor, self.zemlja_porekla, self.jezik, self.stanje)]


# Klasu Biblioteka koja ima sledeća polja:
# • zaposleni – niz Zaposlen
# • knjige – niz Knjiga
# • jePrijavljen – boolean (True/False)
# Kreirati konstruktor koji prima argumente niz zaposlenih i niz knjiga, a polje jePrijavljen postavlja na
# False.


# Na kraju kreirati objekat Biblioteka i proslediti mu liste knjiga i zaposlenih koje se nalaze u tekstualnim
# fajlovima zaposleni.txt i knjige.txt


class Biblioteka:
    def __init__(self, zaposleni=[], knjige=[]):
        Biblioteka.validacija(zaposleni, knjige)
        self.zaposleni = zaposleni
        self.knjige = knjige
        self.jeprijavljen = False

    @staticmethod
    def validacija(zaposleni, knjige):
        assert type(zaposleni) == list, "Mora biti lista!"
        assert type(knjige) == list, "Mora biti lista!"
        if len(zaposleni):
            for zaposlen in zaposleni:
                assert type(zaposlen) == Zaposlen, "Mora biti lista!"
        if len(knjige):
            for knjiga in knjige:
                assert type(knjiga) == Knjiga, "Mora biti lista!"

    # Kreirati sledeće metode:

    # • registracija_zaposlenog – (koja registruje zaposlenog u sistem) – ta metoda prima sve
    # argumente potrebne za kreaciju objekta zapolenog, zatim proverava da li u bazi ima zaposelnog
    # sa tim imenom i jmbg-om i ukoliko ne postoji takav zaposleni kreira nov objekat zaposlenog i
    # dodaje ga u niz zapolsenih. U suprotnom ispisuje odgovarajuću poruku.

    def registracija_zaposlenog(self, ime_prezime, jmbg, username, password):
        for zaposlen in self.zaposleni:
            if zaposlen.ime_prezime == ime_prezime and zaposlen.jmbg == jmbg:
                self.zaposleni.append(Zaposlen(zaposlen.ime_prezime, zaposlen.jmbg, zaposlen.br_telefona,
                                               zaposlen.diploma, username, password))
                with open("zaposleni.txt", "r+") as file:
                    new_file = file.readlines()
                    file.seek(0)
                    for line in new_file:
                        if ime_prezime and jmbg not in line:
                            file.write(line)
                    else:
                        file.write('{}, {}, {}, {}, {}, {}\n'.format(zaposlen.ime_prezime, zaposlen.jmbg,
                                                                     zaposlen.br_telefona, zaposlen. diploma,
                                                                     username, password))
                    file.truncate()
                    return True
            else:
                return False

    # • prijava – (koja prijavljuje korisnika i omogućuje mu pristup sistemu) – ta metoda prima
    # argumente username i password i proverava da li se poklapa sa nekim zaposlenim iz baze i
    # ukoliko takav zaposleni postoji, polje jePrijavljen postavlja na True i ispisuje „Dobro došli
    # {ime_prezime} u sistem biblioteke.”, a u suprotnom ispisuje odgovarajuću poruku.

    def prijava(self, username, password):
        for zaposlen in self.zaposleni:
            if zaposlen.username == username and zaposlen.password == password and not self.jeprijavljen:
                self.jeprijavljen = True
                return True
        return False

    # • dodaj_knjigu – (koja dodaje novu knjigu u sistem(niz knjige, tekstualni fajl knjige.txt) – ta
    # metoda prima objekat Knjiga i ubacuje isti u sistem

    def dodaj_knjigu(self, naslov, autor, godina_izdavanja, zemlja_porekla, jezik):
        self.knjige.append(Knjiga(naslov, autor, godina_izdavanja, zemlja_porekla, jezik))
        file = open("knjige.txt", 'a')
        file.write('{}, {}, {}, {}, {}\n'.format(naslov, autor, godina_izdavanja, zemlja_porekla, jezik))
        file.close()

    # • izbaci_knjigu – (koja izbacuje knjigu iz sistema(niz knjige, tekstualni fajl knjige.txt) – ta
    # metoda prima naslov, zatim proverava da li takva knjiga postoji i ukoliko postoji izbacuje je iz
    # sistema, a u suprotnom ispisuje odgovarajuću poruku

    def izbaci_knjigu(self, naslov):
        for knjiga in self.knjige:
            if knjiga.naslov == naslov:
                with open("knjige.txt", "r+") as file:
                    new_file = file.readlines()
                    file.seek(0)
                    for line in new_file:
                        if naslov not in line:
                            file.write(line)
                    file.truncate()

    # • nadji_knjigu – (koja nalazi knjigu) – ta metoda prima naslov, zatim proverava da li takva knjiga
    # postoji i ukoliko postoji ispisuje sve podatke o toj konkretnoj knjizi, a u suprotnom ispisuje
    # odgovarajuću poruku

    def nadji_knjigu(self, naslov):
        for knjiga in self.knjige:
            if knjiga.naslov == naslov:
                return knjiga
        return "Knjiga nije nadjena!"

    # • izdaj_knjigu – (koja izdaje knjigu) – ta metoda prima naslov, zatim proverava da li takva knjiga
    # postoji i ukoliko postoji, proverava da li je na stanju i ukoliko jeste izdaje tu knjigu, odnosno,
    # polje stanje menja na „Izdato“ i ispisuje nam odgovarajuću poruku, a u suprotnom ispisuje
    # odgovarajuću poruku

    def izdaj_knjigu(self, naslov):
        for knjiga in self.knjige:
            if knjiga.naslov == naslov:
                if knjiga.stanje == "Na stanju":
                    knjiga.stanje = "Izdato"
                    return "Knjiga je izdata!"
                return "Knjiga je vec izdata!"
        return "Knjiga nije nadjena!"

    # • vrati_knjigu – (koja vraća knjigu) – ta metoda prima naslov, zatim proverava da li takva knjiga
    # postoji i ukoliko postoji i vraća je u sistem, odnosno, polje stanje menja na „Na stanju“ i
    # ispisuje nam odgovarajuću poruku, a u suprotnom ispisuje odgovarajuću poruku

    def vrati_knjigu(self, naslov):
        for knjiga in self.knjige:
            if knjiga.naslov == naslov:
                knjiga.stanje = "Na stanju"
                return "Knjiga je vracena!"
        return "Knjiga nije nadjena!"

    # • zaposli – (koja dodaje novog zaposlenog u sistem(niz zaposleni, tekstualni fajl zaposleni.txt) –
    # ta metoda prima objekat Zaposlen i ubacuje isti u sistem ?????

    def zaposli(self, ime_prezime, jmbg, br_telefona, diploma):
        username = ime_prezime[:ime_prezime.index(' ')].strip().lower() + '.' + \
                   ime_prezime[ime_prezime.index(' '):].strip().lower()
        password = '123'
        self.zaposleni.append(Zaposlen(ime_prezime, jmbg, br_telefona, diploma, username, password))
        file = open("zaposleni.txt", 'a')
        file.write('{}, {}, {}, {}, {}, {}\n'.format(ime_prezime, jmbg, br_telefona, diploma, username, password))
        file.close()
        return True

    # • otpusti – (koja izbacuje zaposlenog iz sistema(niz zaposleni, tekstualni fajl zaposleni.txt) – ta
    # metoda prima ime i prezime, zatim proverava da li takav zaposleni postoji i ukoliko postoji
    # izbacuje ga iz sistema

    def otpusti(self, ime_prezime):
        with open("zaposleni.txt", "r") as file:
            lines = file.readlines()
        with open("zaposleni.txt", "w") as file:
            for line in lines:
                if ime_prezime not in line.strip("\n"):
                    file.write(line)


radnici = [zaposleni.strip().split(', ') for zaposleni in open("zaposleni.txt", 'r')]

radnici = [Zaposlen(zap[0], zap[1], zap[2], zap[3], zap[4], zap[5]) for zap in radnici]

knjige = [knjiga.strip().split(', ') for knjiga in open("knjige.txt", 'r')]

knjige = [Knjiga(knj[0], knj[1], knj[2], knj[3], knj[4]) for knj in knjige]

biblioteka = Biblioteka(radnici, knjige)
