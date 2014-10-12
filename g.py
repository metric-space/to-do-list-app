import sys # just for testing purpose, not for the module itself
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):

	def __init__(self,parent=None):
		super(Form,self).__init__(parent)
		self.listBr = QListWidget();
		self.lineEdit=QLineEdit(" ")
		layout = QVBoxLayout()
		layout.addWidget(self.listBr)
		layout.addWidget(self.lineEdit)
		self.setLayout(layout)

		# -- SIGNAL and SLOT stuff --
		self.chosen =None
		self.connect(self.lineEdit ,SIGNAL("returnPressed()"),self.updateUi)
		self.connect(self.listBr ,SIGNAL("itemClicked(QListWidgetItem*)"),self.update2)

		self.setWindowTitle('to do app')

	def updateUi(self,function=None):

		if function == None:
			function = lambda x:x                   # basic id function

		text = unicode(self.lineEdit.text())
		transformed_text = function(text)

		if self.chosen:
			self.chosen.setText(transformed_text)
			self.chosen = None
		else:
			egg = QListWidgetItem(self.listBr)
			egg.setText(transformed_text)
			egg.setTextColor(Qt.blue)
			self.listBr.addItem(egg)

		self.lineEdit.setText("")                       # to clear the entry line

	def update2(self):
		egg = self.listBr.currentItem()
		self.chosen = egg
		self.lineEdit.setText(egg.text())

	def populate(self,list=None):
		if list == None or list == []:
			pass
		else:
			try:
				for item in list:
					# for the time being I am assuming the list consists of strings
					egg = QListWidgetItem(self.listBr)
					egg.setText(item)
					egg.setTextColor(Qt.blue)
					self.listBr.addItem(egg)
			except:
				print "something wrong happened"
				pass
if __name__=='__main__':
	app = QApplication(sys.argv)
	form = Form()
	form.populate(["Luke","likes","girls","but","is","too"])
	form.show()
	app.exec_()

