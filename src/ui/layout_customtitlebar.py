"""
Copyright 2017 Martin Fitzpatrick

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
# Referenece: https://www.pythonguis.com/tutorials/custom-title-bar-pyqt6/



from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import (
	QWidget,
	QHBoxLayout,
	QVBoxLayout,
	QLabel,
)

class CustomTitleBar(QWidget):
	def __init__(self, parent):
		super().__init__(parent)
		self.setAutoFillBackground(True)
		self.setBackgroundRole(QPalette.ColorRole.Highlight)
		self.initial_pos = None
		title_bar_layout = QHBoxLayout(self)
		title_bar_layout.setContentsMargins(1, 1, 1, 1 )
		title_bar_layout.setSpacing(2)

		self.title = QLabel(f"{self.__class__.__name__}", self)
		self.title.setStyleSheet(
			"""Qlabel {
					font-weight: bold;
					border: 2px solid black;
					border-radius: 12px;
					margin: 2px;
				}
			"""
		)
		self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		if title := parent.windowTitle():
			self.title.setText(title)
		title_bar_layout.addWidget(self.title)
