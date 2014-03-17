import os
import platform
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_laddereditor_window
import qrc_resources

class LadderDiagramScene(QGraphicsScene):
   def __init__(self, parent = None):
      super(LadderDiagramScene, self).__init__(parent)

   def mousePressEvent(self, mouseEvent):
      pass

   def mouseReleaseEvent(self, mouseEvent):
      pass

   def mouseMoveEvent(self, mouseEvent):
      pass
