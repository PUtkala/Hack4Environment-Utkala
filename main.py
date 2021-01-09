
import sys
import folium
import Ciekawostka
import random
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTextBrowser
from PyQt5.QtGui import QImage, QPalette, QBrush, QColor, QIcon, QPixmap


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ciekawostka = Ciekawostka.Ciekawostka()
        self.initWindow()


    def initWindow(self):
        oImage = QImage("forest01.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)
        self.setWindowTitle(self.tr("WYSYPISKA SMIECI"))
        self.setFixedSize(1400, 800)
        self.display_map()

    def open_paper(self):
        QMessageBox.about(self, "PAPIER", "-opakowania z papieru, karton, tekturę\n -katalogi, ulotki, prospekty\n "
                                          "-gazety i czasopisma\n -papier szkolny i biurowy, zadrukowane kartki\n "
                                          "-zeszyty i książki\n -papier pakowy\n -torby i worki papierowe")
    def open_glass(self):
        QMessageBox.about(self, "SZKLO", "-butelki i słoiki po napojach i żywności (w tym butelki po napojach "
                                         "alkoholowych i olejach roślinnych)\n -szklane opakowania po kosmetykach "
                                         "(jeżeli nie są wykonane z trwale połączonych kilku surowców)")
    def open_metal(self):
        QMessageBox.about(self, "METAL I TWORZYWA SZTUCZNE", "-odkręcone i zgniecione plastikowe butelki po napojach\n "
                                                             "-nakrętki, o ile nie zbieramy ich osobno w ramach akcji dobroczynnych\n "
                                                             "-plastikowe opakowania po produktach spożywczych\n "
                                                             "-opakowania wielomateriałowe (np. kartony po mleku i sokach)\n "
                                                             "-opakowania po środkach czystości (np. proszkach do prania), "
                                                             "kosmetykach (np. szamponach, paście do zębów) itp.\n "
                                                             "-plastikowe torby, worki, reklamówki, inne folie\n -aluminiowe puszki po napojach i sokach\n "
                                                             "-puszki po konserwach\n -folię aluminiową\n -metale kolorowe\n -kapsle, zakrętki od słoików")
    def open_bio(self):
        QMessageBox.about(self, "BIODEGRADOWALNE", "-odpadki warzywne i owocowe (w tym obierki itp.)\n -gałęzie drzew i krzewów\n -skoszoną trawę, "
                                                   "liście, kwiaty\n -trociny i korę drzew\n -niezaimpregnowane drewno\n -resztki jedzenia")
    def open_bin(self):
        QMessageBox.about(self, "PRAWIDLOWA SEGREGACJA", "Po lewej znajduja sie ikonki przykladowych smieci\noraz co nalezy i NIE nalezy wyrzucac do poszczegolnych smietnikow")
    def open_x_paper(self):
        QMessageBox.about(self, "NIE PAPIER", "-ręczników papierowych i zużytych chusteczek higienicznych\n -papieru lakierowanego i powleczonego folią\n "
                                              "-papieru zatłuszczonego lub mocno zabrudzonego\n -kartonów po mleku i napojach\n -papierowych worków po nawozach, "
                                              "cemencie i innych materiałach budowlanych\n -tapet\n -pieluch jednorazowych i innych materiałów higienicznych\n "
                                              "-zatłuszczonych jednorazowych opakowań z papieru i naczyń jednorazowych\n -ubrań")
    def open_x_glass(self):
        QMessageBox.about(self, "NIE SZKLO", "-ceramiki, doniczek, porcelany, fajansu, kryształów\n -szkła okularowego\n -szkła żaroodpornego\n -Zniczy z "
                                             "zawartością wosku\n -żarówek i świetlówek\n -reflektorów\n -opakowań po lekach, rozpuszczalnikach, olejach silnikowych\n "
                                             "-luster\n -szyb okiennych i zbrojonych\n -monitorów i lamp telewizyjnych\n -termometrów i strzykawek")
    def open_x_metal(self):
        QMessageBox.about(self, "NIE METAL I\n TWORZYWA SZTUCZNE", "-butelek i pojemników z zawartością\n -plastikowych zabawek\n -opakowań po lekach i "
                                                                   "zużytych artykułów medycznych\n -opakowań po olejach silnikowych\n -części samochodowych\n "
                                                                   "-zużytych baterii i akumulatorów\n -puszek i pojemników po farbach i lakierach\n -zużytego sprzętu elektronicznego i AGD")
    def open_x_bio(self):
        QMessageBox.about(self, "NIE BIO", "-kości zwierząt\n -oleju jadalnego\n -odchodów zwierząt\n -popiołu z węgla kamiennego\n -leków\n -drewna impregnowanego\n "
                                           "-płyt wiórowych i pilśniowych MDF\n -ziemi i kamieni\n -innych odpadów komunalnych (w tym niebezpiecznych)")




    def random_FunFact(self):
        self.ciekawostka.number = random.randint(1, 11)
        fun_fact = self.ciekawostka.fun_fact
        self.textBrowser.append(fun_fact)
        self.textBrowser.append("\nzrodlo: https://naszesmieci.mos.gov.pl/ciekawostki ")
        self.textBrowser = []


    def open_file(self):
        webbrowser.open('mapa.html')


    def display_map(self):
        btn_mapa = QtWidgets.QPushButton(self.tr("Mapa"))
        btn_mapa.clicked.connect(self.open_file)
        btn_mapa.setStyleSheet("background-color: #fffffe")
        btn_ciek = QtWidgets.QPushButton(self.tr("Ciekawostka\n Dnia"), clicked = lambda:self.random_FunFact())
        btn_ciek.setStyleSheet("background-color: #fffffe")

        self.bin = QtWidgets.QPushButton(self.tr(""))
        self.bin.clicked.connect(self.open_bin)
        self.bin.setFixedSize(80, 130)
        self.bin.setStyleSheet("background-image : url(bin.png);")
        self.paper = QtWidgets.QPushButton(self.tr(""))
        self.paper.clicked.connect(self.open_paper)
        self.paper.setFixedSize(50, 60)
        self.paper.setStyleSheet("background-image : url(paper.png);")
        self.plastic = QtWidgets.QPushButton(self.tr(""))
        self.plastic.clicked.connect(self.open_metal)
        self.plastic.setFixedSize(50, 100)
        self.plastic.setStyleSheet("background-image : url(plastic.png);")
        self.glass = QtWidgets.QPushButton(self.tr(""))
        self.glass.clicked.connect(self.open_glass)
        self.glass.setFixedSize(50, 90)
        self.glass.setStyleSheet("background-image : url(glass.png);")
        self.metal = QtWidgets.QPushButton(self.tr(""))
        self.metal.clicked.connect(self.open_metal)
        self.metal.setFixedSize(50, 82)
        self.metal.setStyleSheet("background-image : url(metal.png);")
        self.bio = QtWidgets.QPushButton(self.tr(""))
        self.bio.clicked.connect(self.open_bio)
        self.bio.setFixedSize(50, 50)
        self.bio.setStyleSheet("background-image : url(banana.png);")

        self.x_paper = QtWidgets.QPushButton(self.tr(""))
        self.x_paper.clicked.connect(self.open_x_paper)
        self.x_paper.setFixedSize(50, 60)
        self.x_paper.setStyleSheet("background-image : url(x_paper.jpg);")
        self.x_plastic = QtWidgets.QPushButton(self.tr(""))
        self.x_plastic.clicked.connect(self.open_x_metal)
        self.x_plastic.setFixedSize(50, 100)
        self.x_plastic.setStyleSheet("background-image : url(x_plastic.jpg);")
        self.x_glass = QtWidgets.QPushButton(self.tr(""))
        self.x_glass.clicked.connect(self.open_x_glass)
        self.x_glass.setFixedSize(50, 90)
        self.x_glass.setStyleSheet("background-image : url(x_glass.jpg);")
        self.x_metal = QtWidgets.QPushButton(self.tr(""))
        self.x_metal.clicked.connect(self.open_x_metal)
        self.x_metal.setFixedSize(50, 82)
        self.x_metal.setStyleSheet("background-image : url(x_metal.jpg);")
        self.x_bio = QtWidgets.QPushButton(self.tr(""))
        self.x_bio.clicked.connect(self.open_x_bio)
        self.x_bio.setFixedSize(50, 50)
        self.x_bio.setStyleSheet("background-image : url(x_banana.jpg);")


        self.textBrowser = QTextBrowser()
        self.textBrowser.setStyleSheet("background-color: #ffffef")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setContentsMargins(50, 50, 50, 50)

        self.photo = QtWidgets.QLabel()
        self.photo.setFixedSize(800, 500)
        self.photo.setPixmap(QtGui.QPixmap("map.png"))

        btn_mapa.setFixedSize(150, 60)
        btn_ciek.setFixedSize(150, 60)
        self.textBrowser.setFixedSize(250, 300)


        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        #lay = QtWidgets.QHBoxLayout(central_widget)
        all_lay = QtWidgets.QVBoxLayout(central_widget)

        lay_container = QtWidgets.QWidget()
        lay = QtWidgets.QHBoxLayout(lay_container)

        types_container = QtWidgets.QWidget()
        types_container.setStyleSheet("background-color:white;")
        lay_types = QtWidgets.QHBoxLayout(types_container)
        #lay_types.addWidget(self.bin)
        lay_types.addStretch()
        lay_types.addWidget(self.paper)
        lay_types.addWidget(self.x_paper)
        lay_types.addStretch()
        lay_types.addWidget(self.plastic)
        lay_types.addWidget(self.x_plastic)
        lay_types.addStretch()
        lay_types.addWidget(self.glass)
        lay_types.addWidget(self.x_glass)
        lay_types.addStretch()
        lay_types.addWidget(self.metal)
        lay_types.addWidget(self.x_metal)
        lay_types.addStretch()
        lay_types.addWidget(self.bio)
        lay_types.addWidget(self.x_bio)
        lay_types.addStretch()

        button_container = QtWidgets.QWidget()
        vlay = QtWidgets.QVBoxLayout(button_container)
        vlay.setSpacing(50)
        vlay.addStretch()
        vlay.addWidget(btn_mapa)
        vlay.addWidget(btn_ciek)
        vlay.addStretch()
        lay.addWidget(button_container)
        lay.addStretch()
        lay.addWidget(self.photo)
        lay.addWidget(self.textBrowser, stretch=1)
        lay.addStretch()
        all_lay.addWidget(lay_container)
        #all_lay.addStretch()
        all_lay.addWidget(types_container)

        ################################################################################
        ################################################################################


        m = folium.Map(location=[53.1235, 18.0084])

        folium.Marker([53.1235, 18.0084], popup="<i>Bydgoszcz</i>").add_to(m)

        m.save('mapa.html')

        ################################################################################



app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())