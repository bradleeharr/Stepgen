import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
	QApplication,
	QMainWindow,
	QWidget,
	QHBoxLayout,
	QVBoxLayout,
	QLabel,
	QPushButton,
)
from .layout_colorwidget import Color
from .layout_customtitlebar import CustomTitleBar

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Stepgen")
		self.resize(400, 200)
#		self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

		central_widget = QWidget()
		self.title_bar = CustomTitleBar(self)

		work_space_layout = QVBoxLayout()
		work_space_layout.setContentsMargins(11, 11, 11, 11)
		work_space_layout.addWidget(QLabel("Hello, World!", self))

		central_widget_layout = QVBoxLayout()
		central_widget_layout.setContentsMargins(2, 2, 2, 2)
		central_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
		central_widget_layout.addWidget(self.title_bar)
		central_widget_layout.addLayout(work_space_layout)


		ok_button = QPushButton("OK")
		def button_quit():
			QApplication.quit()
		ok_button.clicked.connect(button_quit)
		central_widget_layout.addWidget(ok_button)

		central_widget.setLayout(central_widget_layout)
#		central_widget = Color("red")
		self.setCentralWidget(central_widget)


def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()
