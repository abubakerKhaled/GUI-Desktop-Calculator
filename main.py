

def hello_world_GUI():
    '''Hello, World! GUI Example'''
    import sys
    # 1. Import QApplication and all the required widgets
    from PyQt6.QtWidgets import QApplication, QLabel, QWidget

    # 2. Create an instance of QApplication
    app = QApplication([])

    # 3. Create your application's GUI
    window = QWidget()
    window.setWindowTitle('PyQt App')
    window.setGeometry(100, 100, 280, 80)
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(60, 15)

    # 4. Show your application's GUI
    window.show()

    # 5. Run your application's event loop
    sys.exit(app.exec())


def herizontal_layout():
    """Herizontal Layout Example."""
    import sys
    from PyQt6.QtWidgets import (
        QApplication,
        QHBoxLayout,
        QPushButton,
        QWidget
    )
    
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('QHBoxLayout')
    window.setGeometry(200, 200, 500, 400)

    layout = QHBoxLayout()
    layout.addWidget(QPushButton('TopLeft'))
    layout.addWidget(QPushButton('Left'))
    layout.addWidget(QPushButton('Center'))
    layout.addWidget(QPushButton('Right'))
    layout.addWidget(QPushButton('TopRight'))
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())


def vertical_layout():
    """Vertical Layout Example."""
    import sys
    from PyQt6.QtWidgets import (
        QApplication,
        QVBoxLayout,
        QPushButton,
        QWidget
    )
    
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('QVBoxLayout')
    window.setGeometry(200, 200, 500, 400)

    layout = QVBoxLayout()
    layout.addWidget(QPushButton('TOP'))
    layout.addWidget(QPushButton('TopBottom'))
    layout.addWidget(QPushButton('Center'))
    layout.addWidget(QPushButton('TopBottom'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())

def grid_layout():
    """Grid Layout Example."""
    import sys
    from PyQt6.QtWidgets import (
        QApplication,
        QGridLayout,
        QPushButton,
        QWidget
    )
    
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('QGridLayout')
    window.setGeometry(200, 200, 500, 400)

    layout = QGridLayout()
    layout.addWidget(QPushButton('Button (0,0)'),0,0)
    layout.addWidget(QPushButton('Button (0,1)'),0,1)
    layout.addWidget(QPushButton('Button (0,2)'),0,2)
    layout.addWidget(QPushButton('Button (0,3)'),0,3)
    layout.addWidget(QPushButton('Button (1,0)'),1,0)
    layout.addWidget(QPushButton('Button (1,1)'),1,1)
    layout.addWidget(QPushButton('Button (1,2)'),1,2)
    layout.addWidget(QPushButton('Button (1,3)'),1,3)
    layout.addWidget(QPushButton('Button (2,0)'),2,0)
    layout.addWidget(QPushButton('Button (2,1)'),2,1)
    layout.addWidget(QPushButton('Button (2,2) + 2 Columns Span'),2,2,1,2)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())

def form_layout():
    import sys
    from PyQt6.QtWidgets import (
        QApplication,
        QFormLayout,
        QLineEdit,
        QWidget
    )
    
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('QFormLayout')
    window.setGeometry(200, 200, 500, 400)

    layout = QFormLayout()
    layout.addRow("Name: ", QLineEdit())
    layout.addRow("Age: ", QLineEdit())
    layout.addRow("Job: ", QLineEdit())
    layout.addRow("Hobbies: ", QLineEdit())
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())


def dialog_layout():
    """Dialog Layout Example"""
    import sys
    from PyQt6.QtWidgets import (
        QApplication, 
        QDialog,
        QDialogButtonBox,
        QFormLayout,
        QLineEdit,
        QVBoxLayout,
    )
    
    class window(QDialog):
        def __init__(self) -> None:
            super().__init__(parent=None)
            self.setWindowTitle("QDialog")
            dialogLayout = QVBoxLayout()
            formLayout = QFormLayout()
            formLayout.addRow("Name: ", QLineEdit())
            formLayout.addRow("Age: ", QLineEdit())
            formLayout.addRow("Job: ", QLineEdit())
            formLayout.addRow("Hobbies: ", QLineEdit())
            dialogLayout.addLayout(formLayout)
            buttons = QDialogButtonBox()
            buttons.setStandardButtons(
                QDialogButtonBox.StandardButton.Cancel
                | QDialogButtonBox.StandardButton.Ok
            )
            dialogLayout.addWidget(buttons)
            self.setLayout(dialogLayout)
    if __name__ == "__main__":
        app = QApplication([])
        window = window()
        window.show()
        sys.exit(app.exec())


def main_window():
    """Main Window-Style application"""
    import sys
    from PyQt6.QtWidgets import (
        QApplication,
        QLabel,
        QMainWindow,
        QStatusBar,
        QToolBar
    )
    
    class window(QMainWindow):
        def __init__(self) -> None:
            super().__init__(parent=None)
            self.setWindowTitle('QMainWindow')
            self.setCentralWidget(QLabel('<h1>I am the central widget</h1>'))
            self._createMenu()
            self._createToolBar()
            self._createStatusBar()

        def _createMenu(self):
            menu = self.menuBar().addMenu("&Menu")
            menu.addAction("&Exit", self.close)

        def _createToolBar(self):
            tools = QToolBar()
            tools.addAction("Exit", self.close)
            self.addToolBar(tools)

        def _createStatusBar(self):
            status = QStatusBar()
            status.showMessage("I am the Status Bar")
            self.setStatusBar(status)

    if __name__ == "__main__":
        app = QApplication([])
        window = window()
        window.setGeometry(200, 200, 300, 200)
        window.show()
        sys.exit(app.exec())


def signals_slots():
    import sys
    from PyQt6.QtWidgets import (
        QApplication,
        QLabel,
        QPushButton,
        QVBoxLayout,
        QWidget,
    )
    
    def greet():
        if msgLabel.text():
            msgLabel.setText("")
            
        else:
            msgLabel.setText("Hello, World!")
    
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Signals and Slots")
    layout = QVBoxLayout()

    button = QPushButton("Greet")
    button.clicked.connect(greet)

    layout.addWidget(button)
    msgLabel = QLabel("")
    layout.addWidget(msgLabel)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())



def signals_slots_lambda():
    import sys
    from PyQt6.QtWidgets import (
        QApplication,
        QLabel,
        QPushButton,
        QVBoxLayout,
        QWidget,
    )
    
    # def greet():
    #     if msgLabel.text():
    #         msgLabel.setText("")
            
    #     else:
    #         msgLabel.setText("Hello, World!")
    
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Signals and Slots")
    layout = QVBoxLayout()

    button = QPushButton("Greet")
    button.clicked.connect(lambda : msgLabel.setText("") or msgLabel.setText("Hello, World!"))

    layout.addWidget(button)
    msgLabel = QLabel("")
    layout.addWidget(msgLabel)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())



