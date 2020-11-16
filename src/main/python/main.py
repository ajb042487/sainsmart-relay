import sys, os.path

sys.path.append('net' + os.sep)
sys.path.append('sainsmart' + os.sep)

from net.tcpclient import TcpClient
from sainsmart.relayethernet import RelayEthernet

from copy import deepcopy

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit

class ButtonHandler():

    def __init__(self):
        self.relayHandler = None
        self.buttonIndex = None

    def setController(self, relayController):
        self.relayHandler = relayController

    def setIndex(self, index):
        self.buttonIndex = index

    def enableOne(self):
        self.relayHandler.enable(self.buttonIndex)

    def disableOne(self):
        self.relayHandler.disable(self.buttonIndex)

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = QMainWindow()
    widget = QWidget(window)
    layout = QVBoxLayout()
    menubar = QHBoxLayout()

    hostLabel = QLabel("Host: 192.168.1.4")
    portLabel = QLabel("Port: 3000")

    menubar.addWidget(hostLabel)
    menubar.addWidget(portLabel)

    menubar.setAlignment(Qt.AlignTop)
    layout.addLayout(menubar)

    relaySize = 16
    relayPlaceHolder = QHBoxLayout()

    relayControl = RelayEthernet()
    relayControl.setAddress("192.168.1.4")
    relayControl.setPort("3000")

    relayEnableButton = QPushButton("Enable All")
    relayEnableButton.clicked.connect(relayControl.enableAll)
    relayPlaceHolder.addWidget(relayEnableButton)

    relayDisableButton = QPushButton("Disable All")
    relayDisableButton.clicked.connect(relayControl.disableAll)
    relayPlaceHolder.addWidget(relayDisableButton)
    layout.addLayout(relayPlaceHolder)

    halfRange = int(relaySize/2)
    handlers = [ButtonHandler() for i in range(relaySize)]
    for x in range(halfRange):

        relayRow = QHBoxLayout()

        handlers[x].setController(relayControl)
        handlers[x].setIndex(x + 1)
        relayEnableButtonEven = QPushButton("Enable " + str(x + 1))
        relayEnableButtonEven.clicked.connect(handlers[x].enableOne)
        relayRow.addWidget(relayEnableButtonEven)

        relayDisableButtonEven = QPushButton("Disable " + str(x + 1))
        relayDisableButtonEven.clicked.connect(handlers[x].disableOne)
        relayRow.addWidget(relayDisableButtonEven)

        handlers[x + halfRange].setController(relayControl)
        handlers[x + halfRange].setIndex(x + 1 + halfRange)
        relayEnableButtonOdd = QPushButton("Enable " + str(x + 1 + halfRange))
        relayEnableButtonOdd.clicked.connect(handlers[x + halfRange].enableOne)
        relayRow.addWidget(relayEnableButtonOdd)

        relayDisableButtonOdd = QPushButton("Disable " + str(x + 1 + halfRange))
        relayDisableButtonOdd.clicked.connect(handlers[x + halfRange].disableOne)
        relayRow.addWidget(relayDisableButtonOdd)

        layout.addLayout(relayRow)

    layout.addStretch()
    widget.setLayout(layout)
    window.setCentralWidget(widget)
    window.setWindowTitle(appctxt.app.applicationName() + " (v" + appctxt.app.applicationVersion() + ")")
    window.setMinimumSize(350,250)
    window.show()

    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
