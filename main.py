from PySide6 import QtCore, QtWidgets, QtGui
import sys
import random
import os
os.chdir(os.path.dirname(sys.argv[0]))

class MainMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.setWindowTitle("PLANT ENCYCLOPEDIA by Dan")

        oImage = QtGui.QImage("./grass.jpg")
        sImage = oImage.scaled(QtCore.QSize(1280, 720))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))                        
        self.setPalette(palette)

        self.plant_pics = ["1.png", "2.png"] # "2.png", "3.png", "4.png"
        random_plant = random.choice(self.plant_pics)

        self.button1 = QtWidgets.QPushButton("BROWSE PLANTS")
        self.button1.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button1.setStyleSheet("""font-size:36px;""")

        self.button2 = QtWidgets.QPushButton("RANDOM PLANT")
        self.button2.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button2.setStyleSheet("""font-size:36px;""")

        self.button3 = QtWidgets.QPushButton("WATERING")
        self.button3.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button3.setStyleSheet("""font-size:36px;""")

        self.button4 = QtWidgets.QPushButton("EXIT")
        self.button4.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.button4.setStyleSheet(f"""font-size:36px;""")

        self.picture = QtWidgets.QLabel(self, alignment=QtCore.Qt.AlignCenter)
        self.picture.setPixmap(QtGui.QPixmap(f"./pics/{random_plant}"))
        self.picture.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.picture.setGeometry(2000,2000,2000,2000)

        self.label = self.determine_label(random_plant)
        self.button5 = QtWidgets.QPushButton(f"{self.label}")

        self.text = QtWidgets.QLabel("PLANT ENCYCLOPEDIA VERSION 0.1",
                                    alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.text.setStyleSheet("""font-size:56px; background-color:{QtGui.QColor(255,0,0).name};""")
        self.bg = QtWidgets.QLabel(self)
        
        self.rand_pic = QtWidgets.QVBoxLayout(self)
        self.rand_pic.addWidget(self.picture, 5)
        self.rand_pic.addWidget(self.button5)
        pic_layout = QtWidgets.QWidget()
        pic_layout.setLayout(self.rand_pic)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(self.layout)

        menu_layout = QtWidgets.QHBoxLayout(self)
        menu_layout.addWidget(pic_layout, 2)
        menu_layout.addWidget(main_widget, 2)
        to_add = QtWidgets.QWidget()
        to_add.setLayout(menu_layout)

        full_layout = QtWidgets.QVBoxLayout(self)
        full_layout.addWidget(self.text)
        # full_layout.addWidget(search_bar)
        full_layout.addWidget(to_add)

        self.button4.clicked.connect(self._exit)

    @QtCore.Slot()
    def _exit(self):
        exit()

    def determine_label(self, filename):
        if filename == "1.png":
            return "Rhododendron"
        if filename == "2.png":
            return "Blue Flower idk what this is actually lol"

class BrowseMenu(QtWidgets.QWidget):
    def __init__(self, parent=None, selected=None, plant_list=None):
        super(BrowseMenu, self).__init__(parent)
        self.setWindowTitle("PLANT ENCYCLOPEDIA by Dan")

        self.plant_list = plant_list

        self.text_widget = QtWidgets.QTextBrowser(self)
        self.menu_widget = QtWidgets.QListWidget()
        index = None
        if selected != None:
            for i in range(len(self.plant_list)):
                if self.plant_list[i][0] == selected:
                    index = i
        counter = 0
        for i in self.plant_list:
            counter += 1
            item = QtWidgets.QListWidgetItem(f"{i[0]}")
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.menu_widget.addItem(item)

        self.menu_widget.itemSelectionChanged.connect(self.selectionChanged)

        if index != None:
            self.menu_widget.setCurrentRow(index)

        add_button = QtWidgets.QPushButton("Add to Watering")
        remove_button = QtWidgets.QPushButton("Remove from Watering")
        self.back_button = QtWidgets.QPushButton("Back")

        two_buttons = QtWidgets.QHBoxLayout()
        two_buttons.addWidget(add_button)
        two_buttons.addWidget(remove_button)

        content_layout = QtWidgets.QVBoxLayout()
        content_layout.addWidget(self.text_widget)
        content_layout.addLayout(two_buttons)
        content_layout.addWidget(self.back_button)
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(content_layout)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)



        self.setStyleSheet("""
        QLabel {
            background-color: gray;
        }
        QListWidget {
            color: #FFFFFF;
            background-color: #33373B;
        }

        QListWidget::item {
            height: 50px;
        }

        QListWidget::item:selected {
            background-color: #800080;
        }

        QLabel {
            background-color: #FFFFFF;
            qproperty-alignment: AlignCenter;
        }

        QPushButton {
            background-color: #FFA500;
            padding: 20px;
            font-size: 18px;
        }
        """)



    def selectionChanged(self):
        selected = self.menu_widget.selectedItems()[0].text()
        print(f"{selected} selected")
        index = None
        for i in range(len(self.plant_list)):
            if self.plant_list[i][0] == selected:
                index = i
        if index != None:
            self.text_widget.setSource(QtCore.QUrl.fromLocalFile(f"flowers\{selected}.html"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(1280, 720)
        self.startMainMenu()

        self.plant_list = [
            ["Columbine"],
            ["Wild Ginger"],
            ["Butterfly Weed"],
            ["White Wood Aster"],
            ["New England Aster"],
            ["Aromatic Aster"],
            ["Blue Wild Indigo"],
            ["Turtlehead"],
            ["Green-and-Gold"],
            ["Bugbane"],
            ["Tall Coreopsis"],
            ["Wild Bleeding Heart"],
            ["Joe-pye Weed"],
            ["Cranesbill"],
            ["Common Sneezeweed"],
            ["Swamp Sunflower"],
            ["False Sunflower"],
            ["Alumroot"],
            ["Dwarf Crested Iris"],
            ["Gayfeather"],
            ["Michigan Lily"],
            ["Great Blue Lobelia"],
            ["Virginia Bluebells"],
            ["Beebalm"],
            [],
            [],
            [],
            [],
            [],
        ]

    def startMainMenu(self):
        self.Window = MainMenu(self)
        self.setCentralWidget(self.Window)
        self.Window.button1.clicked.connect(self.startBrowseMenu)
        self.Window.button2.clicked.connect(self.startBrowseMenuRandom)
        self.Window.button3.clicked.connect(self.startWatering)
        self.Window.button5.clicked.connect(self.startBrowseMenuDisplayed)
        self.show()

    def startBrowseMenu(self):
        self.Window = BrowseMenu(self, None, self.plant_list)
        self.setCentralWidget(self.Window)
        self.Window.back_button.clicked.connect(self.startMainMenu)
        self.show()

    def startBrowseMenuRandom(self):
        num = random.randint(0, len(self.plant_list)-1)
        ran = self.plant_list[num][0]
        self.Window = BrowseMenu(self, ran, self.plant_list)
        self.setCentralWidget(self.Window)
        self.Window.back_button.clicked.connect(self.startMainMenu)
        self.show()

    def startBrowseMenuDisplayed(self):
        self.Window = BrowseMenu(self, self.Window.label, self.plant_list)
        self.setCentralWidget(self.Window)
        self.Window.back_button.clicked.connect(self.startMainMenu)
        self.show()

    def startWatering(self):
        self.Window = BrowseMenu(self)
        self.setCentralWidget(self.Window)
        self.Window.back_button.clicked.connect(self.startMainMenu)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MainWindow()
    widget.resize(1280, 720)
    widget.show()

    sys.exit(app.exec())