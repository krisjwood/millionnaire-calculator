"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt


# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QComboBox, QDoubleSpinBox, QGridLayout, QLabel, QMainWindow, QSpinBox, QVBoxLayout, QWidget, QPushButton, QFormLayout

__version__ = '0.1'
__author__ = '[Wooden]Caine'
# PEP 8 styling ignored


class CustomSpinBox(QSpinBox):
    """Define custom SpinBox allowing more than 2 digits"""
    def __init__(self, *args):
       QSpinBox.__init__(self, *args)

       self.setRange(0,99999999)

# Create a subclass of QMainWindow to setup the calculator's GUI
class FormWindow(QMainWindow):
    """View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Millionnaire Cal')
        self.setGeometry(500, 350, 330, 280)
        # Set the central widget and the general formLayout
        self.generalLayout = QVBoxLayout()

        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Add titles
        self.generalLayout.addWidget(QLabel('<h1><center>When will you become a<br>millionaire?</center></h1>'))
        self.generalLayout.addWidget(QLabel('<center>Use this calculator to estimate how long it will take your<br>savings and investments to grow to become a millionnaire.</center>'))

        # Create the form and the results
        self._createForm()
        self.generalLayout.addWidget(QLabel('<center><b>Please note:</b> <i>Inflation rates and taxes are not factored<br>in. Additionally, the investment return will vary year on year.</i></center>'))
        self._createBtns()
    
    def _createForm(self):
        """Create the form"""
        # Create the form widget
        self.formLayout = QFormLayout()

        self.CurrencyCombo = QComboBox()
        self.currencyOptions = self.CurrencyCombo.currentText()
        self.CurrencyCombo.addItems(["USD", "GBP", "NZD"])
        self.formLayout.addRow('Currency:', self.CurrencyCombo)

        # Define currency symbol
        currencyStr = self.CurrencyCombo.currentText()
        currency_symbol = '$'
        #self._setCurrencySymbol(currency_symbol, currencyStr)


        self.ageField = QSpinBox()
        self.formLayout.addRow('Age:', self.ageField)
        self.ageField.setValue(18)
        self.currentBalField = CustomSpinBox()
        self.formLayout.addRow(f'Current balance (?):', self.currentBalField)
        self.annInvestmentField = CustomSpinBox()
        self.formLayout.addRow(f'Annual investment (?):', self.annInvestmentField)
        self.interestField = QDoubleSpinBox()
        self.formLayout.addRow('Annual return (%):', self.interestField)
        
        self.generalLayout.addLayout(self.formLayout)

    def _setCurrencySymbol(currency_symbol, currencyStr):
        '''Sets the symbol based on currency selection from drop down'''
        if currencyStr == 'GBP':
            currency_symbol = '£'
        
            return currency_symbol

    def _clearForm(self):
        """Clears form"""
        self.ageField.setValue(18)
        self.currentBalField.clear()
        self.annInvestmentField.clear()
        self.interestField.clear()
    
    def _createBtns(self):
        """Create form buttons"""
        self.btns = QGridLayout()
        clearBtn = QPushButton("Clear")
        self.btns.addWidget(clearBtn, 0, 0)
        submitBtn = QPushButton("Submit")
        self.btns.addWidget(submitBtn, 0, 1)
        self.generalLayout.addLayout(self.btns)
        submitBtn.clicked.connect(self._generateResults)
        clearBtn.clicked.connect(self._clearForm)
    
    
    def _generateResults(self, checked):
        # Create instance of results window
        self.resultsWindow = ResultsWindow()

        # Convert widgets to workable formats
        ageInt = int(self.ageField.text())
        balanceInt = int(self.currentBalField.text())
        investmentInt = int(self.annInvestmentField.text())
        interestInt = float(self.interestField.text())
        currencyStr = self.CurrencyCombo.currentText()

        # Define currency symbol
        self.currency_symbol = '$'
        if currencyStr == 'GBP':
            self.currency_symbol = '£'

        # Pass data from form to results window
        self.resultsWindow.ageText.setText(f"You are {self.ageField.text()} years old.")
        self.resultsWindow.currentBalanceText.setText(f"Your current balance is {self.currentBalField.text()}")
        self.resultsWindow.annualInvestmentText.setText(f"With an annual investment of {self.annInvestmentField.text()}")
        self.resultsWindow.interestText.setText(f"And earning an interest rate of {self.interestField.text()}%")
        self.resultsWindow.CurrencyText.setText(f"Your currency is set as {self.CurrencyCombo.currentText()}.")

        # Generate window
        self.resultsWindow.show()

    
    

class ResultsWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Results')
        self.setGeometry(900, 350, 530, 600)
        layout = QVBoxLayout()
        self.title = QLabel("<h1>Results: </h1>")

        # Create fields for data to be recieved from form
        self.CurrencyText = QLabel()
        self.ageText = QLabel()
        self.currentBalanceText = QLabel()
        self.annualInvestmentText = QLabel()
        self.interestText = QLabel()

        self.link = QLabel('<a href="https://en.wikipedia.org/wiki/Millionaire">What is a millionnaire?</a>')
        self.link.setOpenExternalLinks(True)
        # Add data to layout

        layout.addWidget(self.title)
        layout.addWidget(self.CurrencyText)
        layout.addWidget(self.ageText)
        layout.addWidget(self.currentBalanceText)
        layout.addWidget(self.annualInvestmentText)
        layout.addWidget(self.interestText)
        layout.addWidget(self.link)
        # Set layout 
        self.setLayout(layout)


    def _calModel():
        pass
    
    # def _printResults(self):
    #     """Prints results in new window box"""
    #     self.show()

    
# Client code
def _main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Theme
    pycalc.setStyle('Fusion')
    
    # Colour
    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.darkCyan)
    qp.setColor(QPalette.Button, Qt.gray)
    pycalc.setPalette(qp)

    # Show the calculator's GUI
    formView = FormWindow()
    formView.show()
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    _main()