#!/usr/bin/python
import os
import platform
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import qrc_resources

from ladderdiagramscene import *

__version__ = "0.0.1"

class LadderEditorWindow(QMainWindow):
   def __init__(self):
      super(LadderEditorWindow, self).__init__()

      self.createActions()
      self.createMenus()
      self.createToolbars()

      self.view = QGraphicsView()
      self.view.setDragMode(QGraphicsView.RubberBandDrag)
      self.view.setRenderHint(QPainter.Antialiasing)
      self.view.setRenderHint(QPainter.TextAntialiasing)

      self.scene = LadderDiagramScene(self.view)
      self.scene.setSceneRect(QRectF(0, 0, 5000, 5000))
      
      self.view.setScene(self.scene)
      
      self.scene.addText("Hello!");

      self.setCentralWidget(self.view)
      self.setWindowTitle("Ladder Diagram Editor")

   def createActions(self):
      self.select = QAction(QIcon(":select.png"),
            "Select Object", self, statusTip = "Select object",
            triggered =  self.on_select_click, checkable = True)
      self.left_power_rail = QAction(QIcon(":left_power_rail.png"),
            "Create Left Power Rail", self, statusTip = "Create Left Power Rail",
            triggered =  self.on_left_power_rail, checkable = True)
      self.right_power_rail = QAction(QIcon(":right_power_rail.png"),
            "Create Right Power Rail", self, statusTip = "Create Right Power Rail",
            triggered =  self.on_right_power_rail, checkable = True)
      self.vertical_or = QAction(QIcon(":vertical_or.png"),
            "Create Vertical OR Connection", self, statusTip = "Create Vertical OR Connection",
            triggered =  self.on_vertical_or, checkable = True)
      self.contacts = QAction(QIcon(":contacts.png"),
            "Create Contacts", self, statusTip = "Create Contacts",
            triggered =  self.on_contacts, checkable = True)
      self.exitAction = QAction("E&xit", self, shortcut="Ctrl+X",
            statusTip = "Quit Ladder Diagram Editor", triggered = self.close)
      self.aboutAction = QAction("A&bout", self, shortcut="Ctrl+B",
            triggered = self.about)

   def createMenus(self):
      self.fileMenu  = self.menuBar().addMenu("&File")
      self.fileMenu.addAction(self.exitAction)

      self.editMenu  = self.menuBar().addMenu("&Edit")
      self.editMenu.addAction(self.select)
      self.editMenu.addAction(self.left_power_rail)
      self.editMenu.addAction(self.right_power_rail)
      self.editMenu.addAction(self.vertical_or)
      self.editMenu.addAction(self.contacts)

      self.aboutMenu = self.menuBar().addMenu("&Help")
      self.aboutMenu.addAction(self.aboutAction)

   def createToolbars(self):
      self.fileToolBar = self.addToolBar("File")

      self.ladderEditGroup = QActionGroup(self)
      self.ladderEditGroup.addAction(self.select)
      self.ladderEditGroup.addAction(self.left_power_rail)
      self.ladderEditGroup.addAction(self.right_power_rail)
      self.ladderEditGroup.addAction(self.vertical_or)
      self.ladderEditGroup.addAction(self.contacts)

      self.editToolBar = self.addToolBar("Edit")
      self.editToolBar.addAction(self.select)
      self.editToolBar.addAction(self.left_power_rail)
      self.editToolBar.addAction(self.right_power_rail)
      self.editToolBar.addAction(self.vertical_or)
      self.editToolBar.addAction(self.contacts)

   def about(self):
      QMessageBox.about(self, "Ladder Diagram Editor",
                "The <b>Ladder Diagram Editor</b> for PLC programming.")

   def on_select_click(self):
      pass
   def on_left_power_rail(self):
      pass
   def on_right_power_rail(self):
      pass
   def on_vertical_or(self):
      pass
   def on_contacts(self):
      pass


if __name__ == '__main__':
   import sys

   app = QApplication(sys.argv)

   app.setOrganizationName("KongJa Studio Ltd.")
   app.setOrganizationDomain("kongjastudio.com")
   app.setApplicationName("Ladder Editor")

   mainWindow = LadderEditorWindow()
   mainWindow.setGeometry(100, 100, 800, 500)
   mainWindow.show()

   sys.exit(app.exec_())
