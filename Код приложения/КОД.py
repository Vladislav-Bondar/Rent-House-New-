import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

while True:

 class Elements:
     def hide_log_el(self):
        self.ui.line1.hide()
        self.ui.line2.hide()
        self.ui.arrow.hide()

     def show_log_el(self):
        self.ui.line1.show()
        self.ui.line2.show()
        self.ui.arrow.show()

     def hide_catalog_el(self):
        self.ui.people.hide()
        self.ui.addp.hide()
        self.ui.add.hide()
        self.ui.sub.hide()
        self.ui.text.hide()
        self.ui.dataLine.hide()
        self.ui.cityLine.hide()
        self.ui.search.hide()
        self.ui.city.hide()
        self.ui.date.hide()
        self.ui.person.hide()
        self.ui.chikago.hide()

     def show_catalog_el(self):
        self.ui.people.show()
        self.ui.dataLine.show()
        self.ui.cityLine.show()
        self.ui.search.show()
        self.ui.main_label.show()
        self.ui.city.show()
        self.ui.date.show()
        self.ui.person.show()
        self.ui.chikago.show()

     def change_el_show(self):
         self.ui.exit.show()

     def change_el_hide(self):
         self.ui.exit.hide()

        
 """ All house """
 class House:
     def result_searchChikago(self, event): #Chikago
         self.ui.moscow_click.hide()
         self.ui.Berlin_click.hide()
         self.ui.london_click.hide()
         self.ui.new_click.hide()
         self.ui.showIN.hide()
         self.ui.dateLINE.hide()
         self.ui.dateLine.hide()
         self.ui.Brontext_2.show()
         self.ui.Brontext.show()
         self.ui.showIN.show()
         self.ui.showOUT.show()
         self.ui.descr.hide()
         self.ui.rew.hide()
         self.ui.com.hide()
         self.ui.comment.hide()
         self.ui.main_label.show()
         self.ui.back.show()
         self.hide_catalog_el()
         self.ui.hotel.show()
         self.ui.BronButton.hide()
         self.ui.back.mousePressEvent = self.catalog
         self.ui.main_label.setPixmap(QtGui.QPixmap('chikago.png'))
         self.ui.back.show()         
         self.show_catalog_el
         self.ui.hotel.mousePressEvent = self.describe
         self.ui.send.hide()

     def result_New(self, event):#New
         self.ui.showIN.hide()
         self.ui.dateLINE.hide()
         self.ui.dateLine.hide()
         self.ui.Brontext_2.show()
         self.ui.Brontext.show()
         self.ui.showIN.show()
         self.ui.showOUT.show()
         self.ui.descr.hide()
         self.ui.rew.hide()
         self.ui.com.hide()
         self.ui.comment.hide()
         self.ui.main_label.show()
         self.ui.back.show()
         self.hide_catalog_el()
         self.ui.hotel.show()
         self.ui.BronButton.hide()
         self.ui.back.mousePressEvent = self.catalog
         self.ui.main_label.setPixmap(QtGui.QPixmap('new.png'))
         self.ui.back.show()         
         self.show_catalog_el
         self.ui.send.hide()
         self.ui.hotel.hide()
         self.ui.Brontext.hide()
         self.ui.Brontext_2.hide()
         self.ui.new_click.hide()
         self.ui.Berlin_click.hide()
         self.ui.moscow_click.hide()
         self.ui.london_click.hide()

     def result_Berlin(self, event):#Berlin
         self.ui.dateLINE.hide()
         self.ui.dateLine.hide()
         self.ui.Brontext_2.show()
         self.ui.Brontext.show()
         self.ui.showIN.hide()
         self.ui.showOUT.hide()
         self.ui.descr.hide()
         self.ui.rew.hide()
         self.ui.com.hide()
         self.ui.comment.hide()
         self.ui.main_label.show()
         self.ui.back.show()
         self.hide_catalog_el()
         self.ui.hotel.show()
         self.ui.BronButton.hide()
         self.ui.back.mousePressEvent = self.catalog
         self.ui.main_label.setPixmap(QtGui.QPixmap('Berlin.png'))
         self.ui.back.show()         
         self.show_catalog_el
         self.ui.send.hide()
         self.ui.hotel.hide()
         self.ui.Brontext.hide()
         self.ui.Brontext_2.hide()
         self.ui.Berlin_click.hide()
         self.ui.new_click.hide()
         self.ui.moscow_click.hide()
         self.ui.london_click.hide()

     def result_Moscow(self, event):#Moscow
         self.ui.dateLINE.hide()
         self.ui.dateLine.hide()
         self.ui.Brontext_2.show()
         self.ui.Brontext.show()
         self.ui.showIN.hide()
         self.ui.showOUT.hide()
         self.ui.descr.hide()
         self.ui.rew.hide()
         self.ui.com.hide()
         self.ui.comment.hide()
         self.ui.main_label.show()
         self.ui.back.show()
         self.hide_catalog_el()
         self.ui.hotel.show()
         self.ui.BronButton.hide()
         self.ui.back.mousePressEvent = self.catalog
         self.ui.main_label.setPixmap(QtGui.QPixmap('moscow.png'))
         self.ui.back.show()         
         self.show_catalog_el
         self.ui.send.hide()
         self.ui.hotel.hide()
         self.ui.Brontext.hide()
         self.ui.Brontext_2.hide()
         self.ui.Berlin_click.hide()
         self.ui.new_click.hide()
         self.ui.moscow_click.hide()
         self.ui.london_click.hide()

     def result_London(self, event):#London
         self.ui.dateLINE.hide()
         self.ui.dateLine.hide()
         self.ui.Brontext_2.show()
         self.ui.Brontext.show()
         self.ui.showIN.hide()
         self.ui.showOUT.hide()
         self.ui.descr.hide()
         self.ui.rew.hide()
         self.ui.com.hide()
         self.ui.comment.hide()
         self.ui.main_label.show()
         self.ui.back.show()
         self.hide_catalog_el()
         self.ui.hotel.show()
         self.ui.BronButton.hide()
         self.ui.back.mousePressEvent = self.catalog
         self.ui.main_label.setPixmap(QtGui.QPixmap('Lond.png'))
         self.ui.back.show()         
         self.show_catalog_el
         self.ui.send.hide()
         self.ui.hotel.hide()
         self.ui.Brontext.hide()
         self.ui.Brontext_2.hide()
         self.ui.Berlin_click.hide()
         self.ui.new_click.hide()
         self.ui.moscow_click.hide()
         self.ui.london_click.hide()

     def hotelch(self, event):#For chikago
         self.ui.dateLINE.hide()         
         self.ui.dateLine.hide()
         self.ui.descr.show()
         self.ui.BronButton.hide()
         self.ui.back.mousePressEvent = self.result_searchChikago
         self.ui.main_label.setPixmap(QtGui.QPixmap('отзывы.png'))
         self.ui.bron.setPixmap(QtGui.QPixmap('Забронировать.png'))
         self.ui.descr.setPixmap(QtGui.QPixmap('Описание.png'))
         self.ui.comment.show()
         self.ui.hotel.hide()
         self.ui.com.show()     
         self.ui.send.show()
         self.ui.rew.hide()
         self.ui.send.mousePressEvent = self.comment_set       
         self.ui.bron.show()
         self.ui.showIN.hide()
         self.ui.showOUT.hide()
         self.ui.bron.mousePressEvent = self.bron
         self.ui.descr.mousePressEvent = self.describe

     def bron(self, event): #Bron chikago
         self.ui.showIN.hide()
         self.ui.main_label.setPixmap(QtGui.QPixmap('бронь.png'))
         self.ui.rew.setPixmap(QtGui.QPixmap('Отзывы1.png'))
         self.ui.bron.hide()
         self.ui.rew.show()
         self.ui.rew.mousePressEvent = self.hotelch
         self.ui.com.hide()     
         self.ui.send.hide()
         self.ui.descr.show()
         self.ui.comment.hide()
         self.ui.BronButton.show()
         self.ui.dateLINE.show()
         self.ui.dateLine.show()
         self.ui.BronButton.clicked.connect(self.datebron)
         self.ui.back.mousePressEvent = self.result_searchChikago

     def datebron(self, event): #Date Chikago
         self.ui.Brontext.show
         self.textIn = self.ui.dateLINE.text()
         self.textOut = self.ui.dateLine.text()
         self.ui.showIN.setText(self.textIn)
         self.ui.showOUT.setText(self.textOut)

     def describe (self, event): #describe Chikago
         self.ui.showIN.hide()
         self.ui.showOUT.hide()
         self.ui.Brontext_2.hide()
         self.ui.Brontext.hide()
         self.ui.BronButton.hide()
         self.ui.dateLINE.hide()
         self.ui.dateLine.hide()
         self.ui.main_label.setPixmap(QtGui.QPixmap('describe.png'))
         self.ui.descr.hide()
         self.ui.bron.show()
         self.ui.rew.show()
         self.ui.com.hide()     
         self.ui.send.hide()        
         self.ui.hotel.hide()
         self.ui.rew.mousePressEvent = self.hotelch
         self.ui.bron.mousePressEvent = self.bron
         self.ui.back.mousePressEvent = self.result_searchChikago

     def comment_set(self, event):
         self.text5 = self.ui.com.text()
         self.ui.comment.setText(self.text5)
     

 """ All city """
 class Catalog(House): 
     def catalog(self, event):
         self.ui.london_click.show()
         self.ui.moscow_click.show()
         self.ui.Berlin_click.show()
         self.ui.new_click.show()
         self.ui.back.hide()
         self.ui.comment.hide()
         self.ui.bron.hide()
         self.cityList = ['москва', 'чикаго', 'нью-йорк', 'берлин', 'лондон']
         self.hide_log_el()
         self.show_catalog_el()
         self.ui.main_label.setPixmap(QtGui.QPixmap('main_label.png'))
         self.ui.add.hide()
         self.ui.sub.hide()
         self.ui.photo.show()
         self.change_el_hide()
         self.ui.photo.mousePressEvent = self.menu
         self.ui.main.setPixmap(QtGui.QPixmap('font3.png'))
         self.ui.people.setPixmap(QtGui.QPixmap('people.png'))
         self.ui.people.mousePressEvent = self.peopleadd
         self.ui.search.clicked.connect(self.search)
         self.ui.chikago.mousePressEvent = self.result_searchChikago
         self.ui.new_click.mousePressEvent = self.result_New
         self.ui.Berlin_click.mousePressEvent = self.result_Berlin
         self.ui.moscow_click.mousePressEvent = self.result_Moscow
         self.ui.london_click.mousePressEvent = self.result_London
         self.ui.profile.hide()
         self.ui.hide.hide()
         self.ui.hotel.hide()

     def menu(self, event): #menu people
         self.ui.photo.hide()     
         self.ui.exit.show()
         self.ui.profile.show()
         self.ui.hide.show()
         self.ui.hide.mousePresseEvent = self.hideprof
         self.ui.exit.mousePressEvent = self.forLogin

     def hideprof(self, event): #hide menu
         self.change_el_hide()
         self.exit.hide()
         self.hide.hide()
         self.profile.hide()


     def search(self,event): #search city
         self.text3 = self.ui.cityLine.text().lower()
         self.text4 = self.ui.dataLine.text()
         if self.text3 in self.cityList:
             if self.text3 == 'чикаго':
                 self.ui.search.clicked.connect(self.result_searchChikago)
             elif self.text3 =='нью-йорк':
                 self.ui.search.clicked.connect(self.result_New)
             elif self.text3 == 'берлин':
                 self.ui.search.clicked.connect(self.result_Berlin)
             elif self.text3 == 'москва':
                 self.ui.search.clicked.connect(self.result_Moscow)
             elif self.text3 == 'лондон':
                 self.ui.search.clicked.connect(self.result_London)


     def peopleadd(self, event): #add people what will live in house
         self.ui.addp.setPixmap(QtGui.QPixmap('people2.png'))
         self.ui.add.setPixmap(QtGui.QPixmap('add (1).png'))
         self.ui.sub.setPixmap(QtGui.QPixmap('minus (1).png'))
         self.ui.addp.show()
         self.ui.add.show()
         self.ui.sub.show()
         self.ui.add.mousePressEvent = self.add
         self.ui.sub.mousePressEvent = self.sub         
         self.ui.text.show()
         self.ui.people.mousePressEvent = self.hide_add_people

     def add(self,event): #add people
         self.ui.text.setText('2')
         self.ui.add.mousePressEvent = self.add
         self.ui.sub.mousePressEvent = self.sub

     def sub(self,event): #sub people
         self.ui.text.setText('1')
         self.ui.add.mousePressEvent = self.add
         self.ui.sub.mousePressEvent = self.sub

     def hide_add_people(self, event): #func for hide tool for add/sub people
         self.ui.addp.hide()
         self.ui.sub.hide()
         self.ui.text.hide()
         self.ui.people.mousePressEvent = self.catalog

 """ Main class """
 class Sign_in (Catalog, Elements):
    def __init__(self):        
        self.ui = uic.loadUi('qt.ui')
        self.ui.main.setPixmap(QtGui.QPixmap('font.jpg'))
        self.ui.cont.setPixmap(QtGui.QPixmap('cont.png'))
        self.ui.cont.mousePressEvent = self.forLogin
        self.hide_log_el()
        self.hide_catalog_el()
        self.ui.photo.hide()
        self.ui.profile.hide()
        self.ui.back.hide()
        self.ui.main_label.hide()
        self.ui.exit.hide()
        self.ui.hide.hide()
        self.ui.hotel.hide()
        self.ui.com.hide()
        self.ui.send.hide()
        self.ui.bron.hide()
        self.ui.show()
        self.ui.rew.hide()
        self.ui.descr.hide()
        self.ui.dateLINE.hide()
        self.ui.dateLine.hide()
        self.ui.BronButton.hide()
        self.ui.Brontext.hide()
        self.ui.showIN.hide()
        self.ui.Brontext_2.hide()
        self.ui.new_click.hide()
        self.ui.Berlin_click.hide()
        self.ui.moscow_click.hide()
        self.ui.london_click.hide()

    def admin_log(self, event):
        self.text1 = self.ui.line1.text()
        self.text2 = self.ui.line2.text()
        if self.text1 == 'admin':
            if self.text2 == '123':
                self.ui.arrow.mousePressEvent = self.catalog
        else:
            pass
    
    def forLogin(self, event):
        self.ui.london_click.hide()
        self.ui.Berlin_click.hide()
        self.hide_catalog_el
        self.ui.rew.hide()
        self.change_el_hide()
        self.ui.cont.hide()
        self.show_log_el()
        self.hide_catalog_el()
        self.ui.profile.hide()
        self.ui.main_label.hide()
        self.ui.chikago.hide()
        self.ui.hotel.hide()
        self.ui.comment.hide()
        self.ui.com.hide()
        self.ui.send.hide()
        self.ui.bron.hide()
        self.ui.descr.hide()
        self.ui.back.hide()
        self.ui.dateLINE.hide()
        self.ui.dateLine.hide()
        self.ui.BronButton.hide()
        self.ui.Brontext.hide()
        self.ui.Brontext_2.hide()
        self.ui.showIN.hide()
        self.ui.new_click.hide()
        self.ui.moscow_click.hide()
        self.ui.main.setPixmap(QtGui.QPixmap('font2.jpg'))
        self.ui.arrow.mousePressEvent = self.admin_log




 if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Sign_in()
    sys.exit(app.exec_())  
