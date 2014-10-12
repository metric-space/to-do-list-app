import sys # just for testing purpose, not for the module itself
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):

	def __init__(self,parent=None):

		self.inner_list = {}
		self.external_function = None

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

	def updateUi(self):


		text = unicode(self.lineEdit.text())

		if self.chosen != None:
			egg = self.inner_list[self.chosen]
			egg[0] = text
			egg[1].setText(text)
			self.chosen = None
			print "debug : %s " %self.inner_list
		else:
			egg = QListWidgetItem(self.listBr)
			self.inner_list[len(self.inner_list)]=[text,egg]
			egg.setText(text)
			egg.setTextColor(Qt.blue)
			self.listBr.addItem(egg)

		self.lineEdit.setText("")                       # to clear the entry line

		if self.external_function:
			self.external_function()

	def update2(self):
		egg = self.listBr.currentItem()

		# stupid linear algorithm
		for i in self.inner_list:
			if self.inner_list[i][1] == egg:
				self.chosen = i
		# change algorithm 

		self.lineEdit.setText(egg.text())

	def populate(self,list=None):
		if list == None or list == {}:
			pass
		else:
			try:
				counter = 0
				print list
				for item in list.values():
					# for the time being I am assuming the list consists of strings
					egg = QListWidgetItem(self.listBr)
					egg.setText(item)
					egg.setTextColor(Qt.blue)
					self.listBr.addItem(egg)
					self.inner_list[counter]=[item,egg]
					counter+=1
			except:
				print "something wrong happened"
				pass


	def generate_content(self):
		egg = []
		for i in self.inner_list:
			egg.append(self.inner_list[i][0])
		return egg

	def set_external_function(self,f):
		self.external_function=f

if __name__=='__main__':
	app = QApplication(sys.argv)
	form = Form()
	form.populate(["Luke","likes","girls","but","is","too"])
	form.show()
	app.exec_()

