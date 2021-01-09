import numpy
import random

class Ciekawostka:

    def __init__(self,):

        #self.number = random.randint(1,11)
        self.number = random.randint(1,11)
        self.fun_fact = "init"

        self.ciekawostka()


    def ciekawostka(self):

        if self.number == 1:
            self.fun_fact = "Z 35 plastikowych butelek można wyprodukować bluzę z polaru."
        if self.number == 2:
            self.fun_fact = "Polska wydaje 16 mln złotych rocznie na oczyszczanie lasów ze śmieci."
        if self.number == 3:
            self.fun_fact = "Niemal cały samochód (80 - 95%) przeznaczony do złomowania nadaje sie do recyklingu."
        if self.number == 4:
            self.fun_fact = "Styropianowa tacka rozkłada się 500 lat."
        if self.number == 5:
            self.fun_fact = "Jedna bateria z zegarka elektronicznego może zatruć aż 400 litrów wody.Nie wyrzucaj baterii do kosza. Oddawaj je w punkcie zbiórki albo wrzucaj do specjalnego pojemnika w sklepie"
        if self.number == 6:
            self.fun_fact = "Do produkcji 1 tony papieru potrzeba ok. 17 drzew. Te drzewa produkują w ciągu roku tlen, który wystarczyłby dla 170 osób."
        if self.number == 7:
            self.fun_fact = "Foliowa torba rozkłada się ok. 300 lat. Na zakupy zawsze zabieraj własną torbę wielokrotnego użytku."
        if self.number == 8:
            self.fun_fact = "Ręczniki papierowe, zatłuszczony papier czy chusteczki higieniczne nie nadają się do recyklingu. Wyrzuć je do śmieci zmieszanych"
        if self.number == 9:
            self.fun_fact = "W ciągu roku wyrzucasz ok.66 plastikowych butelek PET. Nie pozwól aby zalegały na składowisku - segreguj."
        if self.number == 10:
            self.fun_fact = "Karton po mleku ma wartość energetyczną, która pozwala zasilać żarówke o mocy 40 Watt przez 1.5 godziny"
        if self.number == 11:
            self.fun_fact = "Jedna plastikowa butelka rozkłada się ok. 500 lat"
        if self.number == 11:
            self.fun_fact = "Jedna aluminiowa puszka rozkłada się od 200 do 400 lat."



