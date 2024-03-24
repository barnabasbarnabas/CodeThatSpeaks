from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QStackedWidget
from PySide6.QtCore import Qt, QTimer, QEvent, QObject, Signal, QSize
from PySide6.QtGui import QCursor
from functools import partial

class ModernPage(QWidget):
    back_to_main = Signal()  

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title_label = QLabel("Text Translation", self)
        title_label.setStyleSheet("font-size: 36px; font-weight: bold; margin-bottom: 20px; color: whitesmoke;")
        layout.addWidget(title_label)

        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("User Input")
        self.user_input.setStyleSheet("border: 1px solid gray; border-radius: 5px;")
        self.user_input.setFixedSize(300, 40)
        layout.addWidget(self.user_input)

        self.target_language_input = QLineEdit(self)
        self.target_language_input.setPlaceholderText("Target Language")
        self.target_language_input.setFixedSize(300, 40)
        layout.addWidget(self.target_language_input)

        translate_button = QPushButton("Translate", self)
        translate_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; border: none; border-radius: 5px;")
        translate_button.setFixedSize(100, 50)
        layout.addWidget(translate_button)

        back_button = QPushButton("Back", self)
        back_button.setStyleSheet("background-color: #FF5733; color: white; font-size: 18px; padding: 10px; border: none; border-radius: 5px;")
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.go_to_main_window)
        layout.addWidget(back_button)

    def go_to_main_window(self):
        self.back_to_main.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Button Cluster")
        self.setStyleSheet("background-color: #333;")

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.setup_main_window()
        self.setup_modern_page()

    def setup_main_window(self):
        main_window_widget = QWidget()
        layout = QGridLayout(main_window_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_texts = ["Text-Translation", "Button 1", "Button 2", "Button 3", "Button 4", "Button 5",
                        "Extract Patterns", "2", '3', '4', '5', '6', "8", '9', '10']
        rows = 4
        cols = 6
        for i, text in enumerate(button_texts):
            button = QPushButton(text, self)
            button.setStyleSheet(
                "background-color: #4CAF50; color: white; font-size: 20px; padding: 10px; border: none; border-radius: 10px;")
            button.setFixedSize(button.sizeHint())
            button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            button.clicked.connect(self.show_modern_page)
            row = i // cols
            col = i % cols
            layout.addWidget(button, row, col)

        self.central_widget.addWidget(main_window_widget)

    def setup_modern_page(self):
        modern_page = ModernPage()
        modern_page.back_to_main.connect(self.show_main_window)
        self.central_widget.addWidget(modern_page)

    def show_modern_page(self):
        self.central_widget.setCurrentIndex(1)

    def show_main_window(self):
        self.central_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
