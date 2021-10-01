from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui import QPainter, QColor, QPen , QIcon , QFont , QPixmap
from PyQt5.QtCore import Qt
import sys
def suranomi():

    lst = ["1. Фотиҳа","2. Бақара", "3. Оли Имрон", "4. Нисо", "5. Моида", "6. Анъом","7. Аъроф", "8. Анфол", "9. Тавба",
"10. Юнус","11. Ҳуд","12. Юсуф","13. Раъд","14. Иброҳим","15. Ҳижр","16. Наҳл","17. Исро","18. Каҳф","19. Марям",
"20. Тоҳо","21. Анбиё","22. Ҳаж","23. Муъминун","24. Нур","25. Фурқон","26. Шуаро","27. Намл","28. Қосос","29. Анкабут",
"30. Рум","31. Луқмон","32. Сажда","33. Аҳзоб","34. Сабаъ","35. Фотир","36. Ёсин","37. Соффаат","38. Сод","39. Зумар",
"40. Ғофир","41. Фуссилат","42. Шууро","43. Зухруф","44. Духон","45. Жосия","46. Аҳқоф","47. Муҳаммад","48. Фатҳ","49. Ҳужурот",
"50. Қоф","51. Зориёт","52. Тур","53. Нажм","54. Қамар","55. Ар-Роҳман","56. Воқиъа","57. Ҳадид","58. Мужодала","59. Ҳашр",
"60. Мумтаҳана","61. Софф","62. Жумуъа","63. Мунофиқун","64. Тағобун","65. Талоқ","66. Таҳрим","67. Мулк","68. Қалам","69. Ҳаққо",
"70. Маъориж","71. Нуҳ","72. Жин","73. Муззаммил","74. Муддассир","75. Қиёмат","76. Инсон","77. Мурсалот","78. Набаъ","79. Нозиъот",
"80. Абаса","81. Таквир","82. Инфитор","83. Мутоффифун","84. Иншиқоқ","85. Буруж","86. Ториқ","87. Аълаа","88. Ғошия","89. Фажр",
"90. Балад","91. Шамс","92. Лайл","93. Зуҳо","94. Шарҳ","95. Тийн","96. Алақ","97. Қадр","98. Баййина","99. Залзала",
"100. Адият","101. Қориъа","102. Такаасур","103. Аср","104. Ҳумаза","105. Фил","106. Қурайш","107. Мааъуун",
"108. Кавсар","109. Каафирун","110. Наср","111. Масад","112. Ихлос","113. Фалақ","114. Наас"]
    return lst

def dbsura(sura):


    dbarabic = sqlite3.connect("arabcha.db")
    cursor = dbarabic.cursor()

    cursor.execute("SELECT text FROM arabic_text WHERE sura = ?",(sura,))
    lst=[]
    malumotlarar = cursor.fetchall()
    for i in range(len(malumotlarar)):
        qosh=malumotlarar[i][0]
        lst.append(qosh)
    return lst
    dbarabic.close()

def tarjimadb(index,sura):
    if index==1:dbtar = sqlite3.connect("uzkrill.db")
    elif index==2:dbtar = sqlite3.connect("uzlotin.db")
    elif index==3:dbtar = sqlite3.connect("uzmansur.db")
    elif index==4:dbtar = sqlite3.connect("inglizchauqish.db")
    elif index==5:dbtar = sqlite3.connect("inglizchatar.db")
    elif index==6:dbtar = sqlite3.connect("ruscha.db")
    elif index==7:dbtar = sqlite3.connect("qozoqcha.db")
    cursor = dbtar.cursor()

    cursor.execute("SELECT text FROM verses WHERE sura = ?",(sura,))

    malumotlaruz = cursor.fetchall()
    lst=[]
    for i in range(len(malumotlaruz)):
        qosh=malumotlaruz[i][0]
        lst.append(qosh)
    return lst

    dbtar.close()


class Quran(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.oyna()

    def oyna(self):
        self.resize(800, 600)
        self.setWindowTitle("Qur'an")
        self.comboBox = QtWidgets.QComboBox()
        self.textBrowser = QtWidgets.QTextBrowser()
        self.textBrowser.setFont(QFont('Times new roman',20))
        self.textBrowser.setStyleSheet("background-color: #2196F3;color: black")
        self.comboBox1 = QtWidgets.QComboBox()
        self.pushButton = QtWidgets.QPushButton("КЎРИШ")
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("#E8EAF6"))
        self.setPalette(p)
        h_box= QtWidgets.QHBoxLayout()
        h_box.addWidget(self.comboBox)
        h_box.addWidget(self.comboBox1)
        h_box.addWidget(self.pushButton)
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.textBrowser)
        self.setLayout(v_box)
        self.show()
        self.pushButton.clicked.connect(self.korsat)
        self.suranom=suranomi()
        for i in self.suranom:
            self.comboBox.addItem(i)
        self.tar=["Фақат арабча","Шайх Муҳаммад Содиқ","Лотинча","Абдулазиз Мансур","Инглизча ўқилиши","Инглизча таржима","Русча","Қозоқча"]
        for i in self.tar:
            self.comboBox1.addItem(i)
    

    def korsat(self):
        self.textBrowser.clear()
        snomer=1
        for i in self.suranom:
            if self.comboBox.currentText()==i:
                break
            snomer+=1
        
        tarj=0
        for i in self.tar:
            if self.comboBox1.currentText()==i:
                break
            tarj+=1
        tay=""
        sura=dbsura(snomer)
        if tarj>=1:
            tarjima=tarjimadb(tarj,snomer)
            
            for i in range(len(sura)):
                tay+=str(i+1)+"\n"+sura[i]+"\n"+tarjima[i]+"\n"*3
        else:
            for i in range(len(sura)):
                tay+=str(i+1)+"\n"+sura[i]+"\n"*3
        self.textBrowser.setText(tay)

app= QtWidgets.QApplication(sys.argv)
oyna = Quran()
sys.exit(app.exec_())