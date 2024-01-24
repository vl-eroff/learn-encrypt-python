import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QCheckBox, QDialog, QLineEdit

class GronsfeldCipherApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Gronsfeld Cipher')
        self.setGeometry(100, 100, 800, 400)

        # Input text
        input_label = QLabel('Исходный текст:')
        self.input_text = QTextEdit(self)

        # Key entry
        key_label = QLabel('Ключ:')
        self.key_entry = QLineEdit(self)
        self.key_entry.setText("2015")

        # Encryption/Decryption choice
        self.encrypt_check = QCheckBox('Расшифровать', self)

        # Output text
        output_label = QLabel('Результат:')
        self.output_text = QTextEdit(self)

        # Buttons
        process_button = QPushButton('Преобразовать', self)
        process_button.clicked.connect(self.process_cipher)

        clear_button = QPushButton('Очистить поля', self)
        clear_button.clicked.connect(self.clear_fields)

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Файл')

        file_menu.addAction('Открыть', self.open_file)
        file_menu.addAction('Сохранить', self.save_file)
        file_menu.addAction('Выход', self.close)

        # About option
        menubar.addAction('О программе', self.open_about_window)

        # Layout
        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.addWidget(input_label)
        left_layout.addWidget(self.input_text)
        left_layout.addWidget(key_label)
        left_layout.addWidget(self.key_entry)
        left_layout.addWidget(self.encrypt_check)

        right_layout = QVBoxLayout()
        right_layout.addWidget(output_label)
        right_layout.addWidget(self.output_text)

        button_layout = QVBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(process_button)
        button_layout.addWidget(clear_button)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        main_layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def process_cipher(self):
        text = self.input_text.toPlainText()
        key = self.key_entry.text()
        is_encrypt = not self.encrypt_check.isChecked()

        result = self.encrypt_decrypt(text, key, is_encrypt)

        self.output_text.clear()
        self.output_text.insertPlainText(result)

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Открыть файл', '', 'Text files (*.txt)')
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.input_text.clear()
                self.input_text.insertPlainText(content)

    def save_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, 'Сохранить файл', '', 'Text files (*.txt)')
        if file_path:
            content = self.output_text.toPlainText()
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

    def clear_fields(self):
        self.input_text.clear()
        self.key_entry.clear()
        self.output_text.clear()

    def open_about_window(self):
        about_window = AboutWindow()
        about_window.exec_()

    @staticmethod
    def encrypt_decrypt(text, key, encrypt=True):
        result = ''
        key = [int(digit) for digit in str(key)]
        key_len = len(key)

        for i, char in enumerate(text):
            if char.isalpha():
                shift = key[i % key_len] if encrypt else -key[i % key_len]
                result += chr((ord(char) - ord('А' if char.isupper() else 'а') + shift) % 33 + ord('А' if char.isupper() else 'а'))
            else:
                result += char

        return result


class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('About')
        self.setGeometry(200, 200, 400, 300)

        about_label = QLabel('Это приложение для шифрования методом Гронсфельда', self)

        html_content = ""
        with open('./about.html', 'r', encoding="utf8") as file:
            html_content = file.read()

        about_text = QTextEdit(self)
        about_text.setHtml(html_content)
        about_text.setReadOnly(True)

        close_button = QPushButton('Закрыть', self)
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(about_label)
        layout.addWidget(about_text)
        layout.addWidget(close_button)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = GronsfeldCipherApp()
    main_window.show()
    sys.exit(app.exec_())