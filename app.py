import sys
import opencc
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QComboBox

class TextConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文字轉換工具")
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        # 建立主視窗部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 建立佈局
        layout = QVBoxLayout()

        # 建立文字編輯框
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        # 建立選擇轉換方式的下拉框
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("簡轉繁")
        self.combo_box.addItem("繁轉簡")
        layout.addWidget(self.combo_box)


        # 建立轉換按鈕
        convert_button = QPushButton("轉換", self)
        convert_button.clicked.connect(self.convert_text)
        layout.addWidget(convert_button)


        # 建立顯示結果的文字框（可編輯）
        self.result_text_edit = QTextEdit(self)
        layout.addWidget(self.result_text_edit)

        # 將佈局設定為主視窗部件的佈局
        central_widget.setLayout(layout)

    def convert_text(self):
        selected_index = self.combo_box.currentIndex()
        text_to_convert = self.text_edit.toPlainText()

        if selected_index == 0:
            converter = opencc.OpenCC('s2twp')
        else:
            converter = opencc.OpenCC('t2s')

        converted_text = converter.convert(text_to_convert)
        self.result_text_edit.setPlainText(converted_text)  # 將結果設定為可編輯文字框中的文字

def main():
    app = QApplication(sys.argv)
    window = TextConverterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


