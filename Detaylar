import sys: Bu satır, Python'un sys modülünü içe aktarır. sys modülü, Python yürütücüsine ve 
işletim sistemi ile etkileşime geçmek için kullanılır.
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, 
QPushButton, QListWidget, QMessageBox, QInputDialog: Bu satır, PyQt5 kütüphanesinden çeşitli 
bileşenleri içe aktarır. Açıklamak gerekirse:
QApplication: PyQt5 uygulamalarının temelini oluşturan QApplication sınıfını içerir.
QMainWindow: Ana pencereyi temsil eden sınıf.
QWidget: Pencere veya dialog gibi kullanıcı arayüzünün temelini oluşturan sınıf.
QVBoxLayout: Dikey bir düzen (layout) oluşturmak için kullanılan sınıf.
QLabel: Metin veya resimleri görüntülemek için kullanılan etiket sınıfı.
QLineEdit: Tek satırlık metin girişi sağlayan sınıf.
QPushButton: Tıklanabilir bir düğme oluşturan sınıf.
QListWidget: Liste görünümü oluşturan sınıf.
QMessageBox: Kullanıcıya mesajlar göstermek için kullanılan iletişim kutusu sınıfı.
QInputDialog: Kullanıcıdan giriş almak için kullanılan iletişim kutusu sınıfı.
from PyQt5.QtCore import Qt: Bu satır, PyQt5'in Qt modülünden Qt sabitlerini içe aktarır. 
Qt sabitleri, kullanıcı arayüzü elemanlarının özelliklerini belirlemede kullanılır.
from PyQt5.QtGui import QFont, QColor: Bu satır, PyQt5'in QtGui modülünden QFont ve QColor 
sınıflarını içe aktarır. QFont, yazı tipi özelliklerini belirlemek için kullanılırken, QColor, 
renk özelliklerini belirlemek için kullanılır.
-------------------------------------------------------------
__init__(self): Sınıfın yapıcı metodudur. QMainWindow sınıfından kalıtım alarak, ana pencereyi 
oluşturur ve başlangıç değerlerini ayarlar.
initializeUI(self): Kullanıcı arayüzünün oluşturulması ve ayarlanması için kullanılan metod. 
Ana pencere boyutu, başlığı ve düzeni ayarlanır. Ayrıca menü çubuğu ve menü öğeleri oluşturulur.
setupMenuBar(self): Menü çubuğunu oluşturan ve ayarlayan bir metod. "Siparişler" adında bir menü 
ekler ve bu menüye "Bekleyen Siparişler" ve "Teslim Edilmiş Siparişler" adında iki alt menü öğesi ekler.
add_menus(self): Restoran menüsünü oluşturan ve düzenleyen bir metod. Yemek adları ve bu yemeklere 
ait hazırla düğmeleri menü düzenine eklenir.
show_bekleyen_siparisler(self): Bekleyen siparişleri gösteren bir metod. Bekleyen siparişler 
birleştirilir ve bir ileti kutusunda gösterilir.
show_teslim_edilmis_siparisler(self): Teslim edilmiş siparişleri gösteren bir metod. Teslim edilmiş 
siparişler birleştirilir ve bir ileti kutusunda gösterilir.
add_example_orders(self): Örnek siparişleri ekleyen bir metod. Bu örnek siparişler başlangıçta bekleyen 
siparişler listesine eklenir.
add_order(self, siparis_adi, siparis_icerik, siparis_no): Sipariş ekleyen bir metod. Verilen müşteri adı, 
içerik ve sipariş numarasıyla bir sipariş oluşturur ve bekleyen siparişler listesine ekler.
prepare_order(self, yemek, button): Siparişi hazırlayan bir metod. Verilen yemeğe göre siparişin hazırlandığını 
işaretler, teslim edilmiş siparişlere ekler ve bekleyen siparişlerden kaldırır.
--------------------------------------------------------------
 Bu uygulama, bir restoranın sipariş yönetimini sağlar. Müşterilerin verdikleri 
siparişleri bekleyen ve teslim edilmiş siparişler olarak yönetebilir.
ygulama başlatıldığında karşımıza bir restoranın başlangıç ekranı çıkar.
Ekran, restoranın adını ve hoş geldiniz mesajını içerir.
Bekleyen Siparişler: Bu seçenek, bekleyen siparişleri gösterir.
Teslim Edilmiş Siparişler: Bu seçenek, teslim edilmiş siparişleri gösterir.
Menüler
Restoranın menüsü, yemeklerin listesi ve her yemeğe bir hazırla düğmesi ile gösterilir.
Menüde, hazırla düğmesine tıklandığında, o yemeğe ait sipariş hazırlanır ve teslim edilmiş siparişler listesine eklenir.
Siparişler
Bekleyen siparişler, müşteri adı, sipariş içeriği ve sipariş numarasıyla listelenir.
Teslim edilmiş siparişler, aynı bilgilerle listelenir.
Örnek Siparişler
Uygulama başlatıldığında örnek siparişler otomatik olarak eklenir.
Müşteri adı, sipariş içeriği ve sipariş numarasıyla birlikte bekleyen siparişler listelenir.
Sipariş İşlemleri
Herhangi bir yemeğin hazırla düğmesine tıklandığında, ilgili sipariş hazırlanır ve teslim edilmiş siparişler listesine eklenir.
Bekleyen siparişler menüsünden, bir siparişin durumu görüntülenebilir.
Sonuç ve Kapanış
Restoran uygulaması, müşterilerin siparişlerini yönetmek için kullanışlı bir araç sağlar.
Bu uygulama, restoran işletmelerine sipariş yönetiminde yardımcı olabilir.
Son Notlar: Bu sunum, PyQt5 ile geliştirilmiş bir restoran uygulamasının temel özelliklerini ve kullanımını özetlemektedir. 
Uygulama, restoran işletmelerinin sipariş yönetimini kolaylaştırmak için tasarlanmıştır.


