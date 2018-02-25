from PyQt5 import QtGui

Memory = 'gui_memory.json'
Rows = range(4)
Cols = range(2)

class Geometry:
    mainLeft = 225
    mainTop = 100
    mainWidth = 900
    mainHeight = 125
    Main = (mainLeft, mainTop, mainWidth, mainHeight)

    docLeft = 260
    docTop = 150
    docWidth = 750
    docHeight = 250
    Document = (docLeft, docTop, docWidth, docHeight)


class Colors:
    LineLight = """ background: rgba(210, 220, 160, 80%);
        font-size: 16px;
        border-radius: 2px;
        padding: 3px, 3px """
    LineDark = """ background: rgba(200, 200, 150, 50%);
        font-size: 16px;
        border-radius: 5px;
        padding: 3px, 3px """
    ButtonLight = """ background: rgba(210, 220, 160, 80%);
        border-radius: 3px; """
    ButtonDark = """ background: rgba(200, 200, 150, 50%);
        border-radius: 3px; """

    rgb0 = (0, 120, 0)
    rgb1 = (0, 0, 0)
    gradient = (10, 10, 10, 300)
    gradient = QtGui.QLinearGradient(*gradient)
    gradient.setColorAt(0.0, QtGui.QColor(*rgb0))
    gradient.setColorAt(1.0, QtGui.QColor(*rgb1))
    Palette = QtGui.QPalette()
    Palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))


class MacOS:
    EnterKey   = 16777220 ### QtCore.Qt.Key_Enter
    EscapeKey  = 16777216
    CommandKey = 16777249
    ControlKey = 16777250
    OptionKey  = 16777251


class Windows:
    pass


class Linux:
    pass


ConfigOS = MacOS
