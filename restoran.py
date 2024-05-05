import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QMessageBox, QAction, QGridLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bekleyen_siparisler = []
        self.teslim_edilmis_siparisler = []
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Kültür Üniversitesi Restoran')
        self.setupMenuBar()

        main_layout = QVBoxLayout()

        
        main_widget = QWidget()
        main_widget.setStyleSheet("background-color: orange;")
        main_layout.addWidget(main_widget)

        
        header_label = QLabel("KÜLTÜR ÜNİVERSİTESİ RESTORANI")
        header_label.setAlignment(Qt.AlignCenter)
        font = header_label.font()
        font.setPointSize(24)  
        font.setBold(True)
        header_label.setFont(font)
        main_layout.addWidget(header_label, alignment=Qt.AlignTop)  

        self.menu_grid = QGridLayout()
        self.menu_grid.setSpacing(10)  

        self.add_menus()

        main_widget.setLayout(self.menu_grid)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(main_layout)

        
        self.add_example_orders()

    def setupMenuBar(self):
        menu_bar = self.menuBar()

        siparis_menu = menu_bar.addMenu("Siparişler")

        bekleyen_siparisler_action = QAction("Bekleyen Siparişler", self)
        bekleyen_siparisler_action.triggered.connect(self.show_bekleyen_siparisler)
        siparis_menu.addAction(bekleyen_siparisler_action)

        teslim_edilmis_siparisler_action = QAction("Teslim Edilmiş Siparişler", self)
        teslim_edilmis_siparisler_action.triggered.connect(self.show_teslim_edilmis_siparisler)
        siparis_menu.addAction(teslim_edilmis_siparisler_action)

    def add_menus(self):
        yemekler = ["Pizza", "Hamburger", "Makarna", "Köfte", "Salata", 
                    "Çorba", "Kebap", "Balık", "Tavuk Dürüm", "Vegan Tabağı",
                    "Sushi", "Risotto", "Sandviç", "Pide", "Börek", 
                    "Lazanya", "Taco", "Steak", "Ramen", "Gözleme"]

        for index, yemek in enumerate(yemekler):
            label = QLabel(yemek)
            font = label.font()
            font.setPointSize(16) 
            label.setFont(font)
            self.menu_grid.addWidget(label, index, 0)

            
            button = QPushButton("Hazırla")
            button.setStyleSheet("background-color: #3CB371; color: white;")
            if yemek in ["Pizza", "Makarna", "Hamburger", "Salata"]:
                button.setStyleSheet("background-color: #FF4500; color: white;")
            button.clicked.connect(lambda checked, yemek=yemek, button=button: self.prepare_order(yemek, button))  # Butona tıklandığında ilgili yemeğin hazırlandığını belirlemek için lambda kullanıldı
            self.menu_grid.addWidget(button, index, 1)

    def show_bekleyen_siparisler(self):
        siparisler = "\n".join(self.bekleyen_siparisler)
        msg_box = QMessageBox()
        msg_box.setText(siparisler or "Bekleyen sipariş yok.")
        msg_box.setStyleSheet("background-color: #32CD32; color: white;")
        msg_box.exec()

    def show_teslim_edilmis_siparisler(self):
        siparisler = "\n".join(self.teslim_edilmis_siparisler)
        msg_box = QMessageBox()
        msg_box.setText(siparisler or "Teslim edilmiş sipariş yok.")
        msg_box.setStyleSheet("background-color: #32CD32; color: white;")
        msg_box.exec()

    def add_example_orders(self):
        
        self.add_order("Ahmet", "Pizza", 123)
        self.add_order("Ayşe", "Makarna", 124)
        self.add_order("Ali", "Hamburger", 125)
        self.add_order("Fatma", "Salata", 126)

    def add_order(self, siparis_adi, siparis_icerik, siparis_no):
        siparis = f"Sipariş Veren Müşteri: {siparis_adi}, İçeriği: {siparis_icerik}, Sipariş No: {siparis_no}"
        self.bekleyen_siparisler.append(siparis)

    def prepare_order(self, yemek, button):
        siparis = next((siparis for siparis in self.bekleyen_siparisler if yemek in siparis), None)
        if siparis:
            siparis_no = siparis.split(",")[2].split(":")[1].strip()
            QMessageBox.information(self, "Sipariş Hazırlandı", f"{siparis_no} numaralı sipariş için {yemek} hazırlandı.")
            self.teslim_edilmis_siparisler.append(siparis)
            self.bekleyen_siparisler.remove(siparis)
            button.setStyleSheet("background-color: #3CB371; color: white;")
        else:
            QMessageBox.information(self, "Uyarı", f"{yemek} için sipariş bulunmamakta.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setStyleSheet("background-color: #32CD32;") 
    main_window.show()
    sys.exit(app.exec_())
