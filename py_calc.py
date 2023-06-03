# python calculator

"""Python Calculator is smaple calculator build with Python and PyQt6."""

import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
ERROR_MSG = "ERROR"


# View
class py_calc_window(QMainWindow):
    """Python Calculator's main window (GUI or View)."""
    def __init__(self):
        """Python Calculator's main window initializer"""
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setWindowIcon(QtGui.QIcon(r"D:\Study\projects\Python_Projects\GUI_Desktop_Calculator\icon.jpeg"))
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.createDisplay()
        self.createButtons()
        
    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
        
    def createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBord = [
            ["pow", ",", "<-"],
            ['7', '8', '9', '/', 'C'],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0","00", ".", "+", "="],
        ]
        
        for row, key in enumerate(keyBord):
            for col, key in enumerate(key):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        
        self.generalLayout.addLayout(buttonsLayout)
    
    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the Display."""
        self.setDisplayText("")
        
    def clearChar(self):
        """Clear One Character."""
        self.string = self.display.text()
        self.setDisplayText(self.string[:-1])

# Model
def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))

    except Exception:
        result = ERROR_MSG

    return result

# Controller
class PyCalc:
    """PyCalc's controller class."""

    def __init__(self, model, view) -> None:
        """PyCalc's controller class initializer."""
        self._evaluate = model
        self._view = view
        self._conncetSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpressionq(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _conncetSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C","<-"}:
                button.clicked.connect(
                    partial(self._buildExpressionq, keySymbol)
                )
        
        # Return Result if pressed '='
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        # Return Result if pressed 'enter'
        self._view.display.returnPressed.connect(self._calculateResult)
        # Clear Display if pressed 'C'
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)
        # Clear One Character if pressed '<-'
        self._view.buttonMap["<-"].clicked.connect(self._view.clearChar)




def main():
    """Python Calculator's main function."""
    pycalc_app = QApplication([])
    pycalc_window = py_calc_window()
    PyCalc(model=evaluateExpression, view=pycalc_window)
    pycalc_window.show()
    sys.exit(pycalc_app.exec())

if __name__ == "__main__":
    main()

