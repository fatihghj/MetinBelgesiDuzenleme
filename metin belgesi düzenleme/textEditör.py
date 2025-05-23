import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
    QColorDialog, QFontDialog, QMenu
)
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metin Belgesi Oluşturucu")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.create_menu()
        self.text_edit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text_edit.customContextMenuRequested.connect(self.context_menu)

    def create_menu(self):
        menu_bar = self.menuBar()

        # Dosya 
        file_menu = menu_bar.addMenu("Dosya")

        new_action = QAction("Yeni", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("Aç", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Kaydet", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        clear_action = QAction("Temizle", self)
        clear_action.triggered.connect(self.clear_text)
        file_menu.addAction(clear_action)

        # Düzen 
        edit_menu = menu_bar.addMenu("Düzen")

        font_action = QAction("Yazı Tipi", self)
        font_action.triggered.connect(self.change_font)
        edit_menu.addAction(font_action)

        color_action = QAction("Yazı Rengi", self)
        color_action.triggered.connect(self.change_color)
        edit_menu.addAction(color_action)

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt)")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                self.text_edit.setText(f.read())

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Farklı Kaydet", "", "Metin Dosyaları (*.txt)")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.text_edit.toPlainText())

    def clear_text(self):
        self.text_edit.clear()

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setCurrentFont(font)

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)

    def context_menu(self, position):
        menu = QMenu()
        menu.addAction("Kopyala", self.text_edit.copy)
        menu.addAction("Kes", self.text_edit.cut)
        menu.addAction("Yapıştır", self.text_edit.paste)
        menu.addAction("Tümünü Seç", self.text_edit.selectAll)
        menu.exec_(self.text_edit.mapToGlobal(position))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())
