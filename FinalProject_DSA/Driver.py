import sys
from datetime import datetime
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView,QMessageBox
from PyQt5.QtCore import QAbstractTableModel, QVariant, pyqtSignal
from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt
import time
import LogIn
from LogIn import HashTable
import ManagerLogIn
import ADDItems
from ADDItems import FoodLinkedList
import validations
import sortingSystem
import BSTsearching 
from BSTsearching import BinarySearchTree
import feedbackgive
from feedbackgive import FeedbackStack
import FeedBackView
import Orders
from Orders import OrderQueue
import customerbill
from customerbill import BillQueue
import managerBills
from managerBills import ManageQueue

class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.ui = loadUi('Main.ui', self)
        self.hash_table=HashTable()
        self.food_list = FoodLinkedList()
        self.bst = BinarySearchTree()
        self.bill=BillQueue()
        self.managebill=ManageQueue()
        self.feedback=FeedbackStack()
        self.order_queue = OrderQueue()
        self.feedback_stack=[]
        self.customerName= None
        self.firstindex=None
        self.index=None
        self.feedback.read_csv_and_store1('feedbacks.csv')
        read_csv_and_store('Resturant1.csv', self.food_list)
        self.read_csv_and_store_bst('Resturant1.csv', self.bst)
        FeedBackView.read_feedback_csv('feedbacks.csv',self.feedback_stack)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_16)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_26)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_27)
        self.selected_row_index = None  
        self.lastPressedButton = None 
        self.ui.pushButton_2.clicked.connect(lambda: (self.setLastPressedButton('pushButton_2'), self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))[0])
        self.ui.pushButton.clicked.connect(lambda: (self.setLastPressedButton('pushButton'), self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))[0])
        self.ui.pushButton_7.clicked.connect(self.onButton7Clicked)
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_10))
        self.ui.pushButton_34.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_18))
        self.ui.pushButton_33.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_19))
        self.ui.pushButton_35.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_28))
        self.ui.pushButton_37.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_29))
        self.ui.pushButton_38.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_40.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_9))
        self.ui.pushButton_41.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_42.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_9))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        # self.ui.pushButton_71.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_68.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_15))
        self.ui.pushButton_69.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_83.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_99.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
       
        self.ui.pushButton_76.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_12))
        self.ui.pushButton_74.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_13))
        self.ui.pushButton_75.clicked.connect(self.onButton75Clicked)
        self.ui.pushButton_80.clicked.connect(self.onButtonClicked80)
        self.ui.pushButton_81.clicked.connect(self.onbuttonclick81)
        self.ui.pushButton_78.clicked.connect(self.onbuttonclick78)
        self.ui.pushButton_70.clicked.connect(self.onButton70Clicked)
        self.ui.pushButton_8.clicked.connect(self.SignUP)    
        self.ui.pushButton_9.clicked.connect(self.AddItems)
        self.ui.pushButton_22.clicked.connect(self.refresh)
        self.ui.pushButton_21.clicked.connect(self.refresh2)
        self.ui.pushButton_29.clicked.connect(self.refresh4)
        self.ui.pushButton_19.clicked.connect(self.refresh3)
        self.ui.pushButton_24.clicked.connect(self.refreshSearch)
        self.ui.pushButton_25.clicked.connect(self.refreshSearchGuest)
        self.ui.pushButton_23.clicked.connect(self.refreshSearchAsAdmin)
        self.ui.pushButton_20.clicked.connect(self.refreshSearchingBST)
        self.ui.pushButton_16.clicked.connect(self.Feedback)
        self.ui.pushButton_94.clicked.connect(self.onbuttonclick36)
        self.ui.pushButton_39.clicked.connect(self.onButton39Clicked)
        self.ui.pushButton_98.clicked.connect(self.onButton98Clicked)
        self.ui.pushButton_82.clicked.connect(self.onButton82Clicked)
        self.ui.pushButton_36.clicked.connect(self.onButton36Clicked)
        self.ui.pushButton_90.clicked.connect(self.onButtonClicked90)
        self.ui.pushButton_32.clicked.connect(self.giveOrders)
        self.ui.pushButton_14.clicked.connect(self.proceed)
        self.ui.pushButton_91.clicked.connect(self.Maangebills)
        self.ui.pushButton_17.clicked.connect(self.billPaid)
        self.ui.pushButton_17.clicked.connect(self.billPaid)
        self.ui.pushButton_77.clicked.connect(self.customerbill)
       
    
   
    def load_table(self, table_view_name, file_path='resturant1.csv'):
       
            table_view = getattr(self, table_view_name, None)
            if table_view is not None:
                with open(file_path, "r", encoding="utf-8") as fileInput:
                    data1 = list(csv.reader(fileInput))
                    model = TableModel(data1) 
                    table_view.setModel(model)
                    selectionModel=table_view.selectionModel()
                    selectionModel.selectionChanged.connect(self.onSelectionChanged)
                    selectionModel=table_view.selectionModel()
                    selectionModel.selectionChanged.connect(self.onSelectionChanged1)
                    selectionModel=table_view.selectionModel()
                    selectionModel.selectionChanged.connect(self.onSelectionChanged2)
                    selectionModel=table_view.selectionModel()
                    selectionModel.selectionChanged.connect(self.onSelectionChanged3)
            else:
                print(f"TableView with name '{table_view_name}' not found.")
    def Maangebills(self):
        try:
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_22)        
            self.tableView_10.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.managebill.writefile()
            self.load_table('tableView_10','bills.csv')
        except:
            QMessageBox.critical(self, "Error", f"An error occurred: no orders")

    
    def onButton70Clicked(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_20)        
        self.tableView_7.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        FeedBackView.read_output_csv('output.csv')
        self.load_table('tableView_7','output.csv')
        self.ui.pushButton_27.clicked.connect(self.viewfeedback)
        
    def onButton98Clicked(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_23)        
        self.tableView_12.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        FeedBackView.read_output_csv('output.csv')
        self.load_table('tableView_12','output.csv')
        self.ui.pushButton_30.clicked.connect(self.viewfeedbackASGuest)
             
    def onButton82Clicked(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_11)        
        self.tableView_8.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        FeedBackView.read_output_csv('output.csv')
        self.load_table('tableView_8','output.csv')
        self.ui.pushButton_31.clicked.connect(self.viewfeedbackAsAdmin)


    def onButton75Clicked(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_7)        
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table('tableView_2')
        self.ui.pushButton_12.clicked.connect(self.Sort)

    def onbuttonclick81(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_8)
        
        tableView=self.ui.stackedWidget_3.findChild(QtWidgets.QTableView,'tableView_3')
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table('tableView_3')
        selectionModel=tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.onSelectionChanged1)
        self.ui.pushButton_13.clicked.connect(self.update)
    def onSelectionChanged1(self,table):
            tableView=self.ui.stackedWidget_3.findChild(QtWidgets.QTableView,'tableView_3')
            selectedIndexes=tableView.selectedIndexes()
            if selectedIndexes:
                selectedRow=selectedIndexes[0].row()
                text=tableView.model().index(selectedRow,0).data()
                text1=tableView.model().index(selectedRow,1).data()
                text2=tableView.model().index(selectedRow,2).data()
                text3=tableView.model().index(selectedRow,3).data()
                text4=tableView.model().index(selectedRow,4).data()
                text5=tableView.model().index(selectedRow,5).data()
                self.plainTextEdit_11.setPlainText(text)   
                self.plainTextEdit_16.setPlainText(text1)  
                self.plainTextEdit_15.setPlainText(text2)  
                self.plainTextEdit_2.setPlainText(text4)  
                self.plainTextEdit_14.setPlainText(text3)  
                if text5 == '5':
                    self.ui.radioButton_8.setChecked(True)
                elif text5 == '4':
                    self.ui.radioButton_9.setChecked(True)
                elif text5 == '3':
                    self.ui.radioButton_10.setChecked(True)
                elif text5 == '2':
                    self.ui.radioButton_11.setChecked(True)
                elif text5 == '1':
                    self.ui.radioButton_12.setChecked(True) 

    def get_selected_rating(self):
        # Return the text of the selected radio button
        if self.ui.radioButton_8.isChecked():
            return '5'
        elif self.ui.radioButton_9.isChecked():
            return '4'
        elif self.ui.radioButton_10.isChecked():
            return '3'
        elif self.ui.radioButton_11.isChecked():
            return '2'
        elif self.ui.radioButton_12.isChecked():
            return '1'
        else:
            return 'N/A'  
    def clear_input_fields(self):
        self.ui.plainTextEdit_11.clear()
        self.ui.plainTextEdit_16.clear()
        self.ui.plainTextEdit_15.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_14.clear()
        self.ui.radioButton_8.setAutoExclusive(False)
        self.ui.radioButton_9.setAutoExclusive(False)
        self.ui.radioButton_10.setAutoExclusive(False)
        self.ui.radioButton_11.setAutoExclusive(False)
        self.ui.radioButton_12.setAutoExclusive(False)

        self.ui.radioButton_8.setChecked(False)
        self.ui.radioButton_9.setChecked(False)
        self.ui.radioButton_10.setChecked(False)
        self.ui.radioButton_11.setChecked(False)
        self.ui.radioButton_12.setChecked(False)

        self.ui.radioButton_8.setAutoExclusive(True)
        self.ui.radioButton_9.setAutoExclusive(True)
        self.ui.radioButton_10.setAutoExclusive(True)
        self.ui.radioButton_11.setAutoExclusive(True)
        self.ui.radioButton_12.setAutoExclusive(True)
    def update(self):
        try:
            item_id_to_update = self.ui.plainTextEdit_11.toPlainText()
            is_name_valid=validations.name_validation2(self.ui.plainTextEdit_16.toPlainText())
            is_price_valid=validations.price_validation(self.ui.plainTextEdit_2.toPlainText())
            is_category_valid=validations.name_validation2(self.ui.plainTextEdit_15.toPlainText())

            if not item_id_to_update:
                QMessageBox.warning(self, "Error", "please select a row to update by clicking on it in the table.")
                self.clear_input_fields()

            if not is_name_valid:
                QMessageBox.warning(self, "Error", "Invalid name format.")
                self.clear_input_fields()

            if not is_price_valid:
                QMessageBox.warning(self, "Error", "Invalid price format.")
                self.clear_input_fields()

            if not is_category_valid:
                QMessageBox.warning(self, "Error", "Invalid category format.")
                self.clear_input_fields()
            if is_name_valid and is_category_valid and is_price_valid:
                new_data = {
                    'Name': self.ui.plainTextEdit_16.toPlainText(),
                    'Category': self.ui.plainTextEdit_15.toPlainText(),
                    'Price': self.ui.plainTextEdit_2.toPlainText(),
                    'Ingredients': self.ui.plainTextEdit_14.toPlainText(),
                    'Rating': self.get_selected_rating()
                }

                self.food_list.update_menu_item(item_id_to_update, new_data)
                self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.load_table('tableView_3')
                QMessageBox.information(self, "Success", "Item updated successfully")
                self.clear_input_fields()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.clear_input_fields()
            

    def onButtonClicked80(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_14)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableView=self.ui.stackedWidget_3.findChild(QtWidgets.QTableView,'tableView')
        searchBar=self.ui.stackedWidget_3.findChild(QtWidgets.QWidget, "plainTextEdit_12")
        

        
        self.load_table('tableView')
        selectionModel=tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.onSelectionChanged)

        deleteBtn=self.ui.stackedWidget_3.findChild(QtWidgets.QWidget,'pushButton_10')
        deleteBtn.clicked.connect(self.delete)
    def onButtonClicked90(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_17)
        self.tableView_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableView=self.ui.stackedWidget_3.findChild(QtWidgets.QTableView,'tableView_6')
       
        self.load_table('tableView_6','restaurant_orders.csv')
        selectionModel=tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.onSelectionChanged2)
        self.ui.pushButton_15.clicked.connect(self.ordercomplete)

    def onSelectionChanged(self,table):
            searchBar=self.ui.stackedWidget_3.findChild(QtWidgets.QWidget, "plainTextEdit_12")
            tableView=self.ui.stackedWidget_3.findChild(QtWidgets.QTableView,'tableView')
            selectedIndexes=tableView.selectedIndexes()
            if selectedIndexes:
                selectedRow=selectedIndexes[0].row()
                text=tableView.model().index(selectedRow,0).data()
                searchBar.setPlainText(text)

    def onSelectionChanged2(self,table):
            tableView=self.ui.stackedWidget_3.findChild(QtWidgets.QTableView,'tableView_6')
            selectedIndexes=tableView.selectedIndexes()
            if selectedIndexes:
                selectedRow=selectedIndexes[0].row()
                self.firstindex=tableView.model().index(selectedRow,1).data()
               
    def ordercomplete(self):
        self.order_queue.remove_order(self.firstindex)
        self.tableView_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table('tableView_6','restaurant_orders.csv')
        QMessageBox.information(self, "Success", "Item deleted successfully")

    def onSelectionChanged3(self,table):
            tableView=self.ui.stackedWidget_3.findChild(QtWidgets.QTableView,'tableView_10')
            selectedIndexes=tableView.selectedIndexes()
            if selectedIndexes:
                selectedRow=selectedIndexes[0].row()
                self.index=tableView.model().index(selectedRow,0).data()
               
    def billPaid(self):
        self.managebill.remove_bill(self.index)
        self.tableView_10.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table('tableView_10','bills.csv')
        QMessageBox.information(self, "Success", "order compeleted successfully")    

                          
            
    def delete(self):
            try:
                searchBar=self.ui.stackedWidget_3.findChild(QtWidgets.QWidget, "plainTextEdit_12")
                text = searchBar.toPlainText()
                if not text:
                    raise ValueError("Please select an item to delete by clicking on it in the table.")

                self.food_list.delete_menu_item(text)
                self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.load_table('tableView')
                QMessageBox.information(self, "Success", "Item deleted successfully")
                searchBar.clear()

            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
                searchBar.clear()


    def Sort(self):
        try:

            algo = self.comboBox_10.currentText()
            mode = self.radioButton_6.isChecked()
            col = self.comboBox_11.currentText()
            isSorted = False
            types = ['ascending', 'descending']
            radios = [self.radioButton_20, self.radioButton_21]
            type_to_pass = None
            for i in range(0, 2):
                if radios[i].isChecked():
                    type_to_pass = types[i]
                    break

            if algo == 'Select Sorting Algorithm' and col =='Select Column' and not any(radio.isChecked() for radio in radios):
                QMessageBox.information(self, "error", "please select  algorithm and column and sorting order")

            elif algo == 'Select Sorting Algorithm':
                QMessageBox.information(self, "error", "please select  algorithm first")
            elif col == 'Select Column':
                QMessageBox.information(self, "error", "please select  column no first")
            elif not any(radio.isChecked() for radio in radios):
                QMessageBox.information(self, "error", "please select a sorting order")
            if (algo in ['Pigeonhole Sort', 'Radix Sort']) and (
                    col in ['Name', 'Category', 'Ingredients']):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Error')
                msg.setText('The selected sorting algorithm is not applicable to string data.')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                sortingSystem.dataSorter(algo, col, type_to_pass)
                QMessageBox.information(self, "Success", "the column is sorted")

                isSorted = True
                self.ui.load_table('tableView_2','resturantsort.csv')
        except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")  

    def refresh(self):
        self.ui.load_table('tableView_2','Resturant1.csv')

    def refresh2(self):
        self.ui.load_table('tableView_4','Resturant1.csv') 
    def refreshSearchingBST(self):
        self.ui.load_table('tableView_5','Resturant1.csv')     

    def refresh4(self):
        self.ui.load_table('tableView_11','Resturant1.csv')     

    def refresh3(self):
        self.ui.load_table('tableView_13','Resturant1.csv')        

    def setLastPressedButton(self, buttonName):
        self.lastPressedButton = buttonName
    
    def onButton7Clicked(self):
        
        print("Last Pressed Button:", self.lastPressedButton)
        
        if self.lastPressedButton == 'pushButton_2':
            self.signInManager()
           
        elif self.lastPressedButton == 'pushButton':
            self.SignIN()

    def SignUP(self):
            try:
                username = self.plainTextEdit_7.toPlainText()
                password = self.plainTextEdit_6.toPlainText()
                role = "customer"

                if not username and not password:
                    raise ValueError("Please enter a username and password.")

                elif not username:
                    raise ValueError("Please enter a username.")

                elif not password:
                    raise ValueError("Please enter a password.")
                if not LogIn.is_valid_username(username):
                    raise ValueError("Invalid username. Your username must contain at least 4 characters.")
                self.plainTextEdit_7.clear()
                self.plainTextEdit_6.clear()    

                if LogIn.isexist(self, username):
                    raise ValueError("User already exists.")
                self.plainTextEdit_7.clear()
                self.plainTextEdit_6.clear()    

                if not LogIn.is_valid_password(password):
                    raise ValueError("Invalid password. Password must be at least 6 characters and contain at least 1 digit.")
                self.plainTextEdit_7.clear()
                self.plainTextEdit_6.clear()    
       
                LogIn.register(self,username, password, role)
                self.plainTextEdit_7.clear()
                self.plainTextEdit_6.clear()
                QMessageBox.information(self, "Success", "User added successfully")
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
       
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def SignIN(self):
     try:   
        print("Customer is here")   
        username=self.plainTextEdit_5.toPlainText()
        password=self.plainTextEdit_4.toPlainText()

        if not username and not password:
                    raise ValueError("Please enter a username and password.")

        elif not username:
            raise ValueError("Please enter a username.")

        elif not password:
            raise ValueError("Please enter a password.")
        
        if LogIn.login(self,username,password) is True:
            QMessageBox.information(self, "Success", "Customer logged in successfully")
            self.customerName=self.plainTextEdit_5.toPlainText()
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            self.plainTextEdit_5.clear()
            self.plainTextEdit_4.clear()
        else:
            raise ValueError("Incorrect username or password")
            self.plainTextEdit_5.clear()
            self.plainTextEdit_4.clear()

     except Exception as e:
        QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
       
        self.plainTextEdit_5.clear()
        self.plainTextEdit_4.clear()


    def signInManager(self):
     try:   
            print("Manager is here")
            username = self.plainTextEdit_5.toPlainText()
            password = self.plainTextEdit_4.toPlainText()
            role = 'Manager'
            if not username and not password:
                    raise ValueError("Please enter a username and password.")

            elif not username:
                raise ValueError("Please enter a username.")

            elif not password:
                raise ValueError("Please enter a password.")
            
            if ManagerLogIn.loginM(self, username, password, role) is True:
                QMessageBox.information(self, "Success", "Manager logged in successfully")
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)
                self.plainTextEdit_5.clear()
                self.plainTextEdit_4.clear()
              
            else:
                raise ValueError("Incorrect username or password")
                self.plainTextEdit_5.clear()
                self.plainTextEdit_4.clear()

     except Exception as e:
        QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        self.plainTextEdit_5.clear()
        self.plainTextEdit_4.clear()
  

    def AddItems(self):
        try:
            ItemID = self.plainTextEdit_8.toPlainText()
            name = self.plainTextEdit_9.toPlainText()
            category = self.plainTextEdit_10.toPlainText()
            price = self.plainTextEdit.toPlainText()
            ingrediants = self.plainTextEdit_13.toPlainText()
            types = ['5', '4', '3', '2', '1']
            radios = [self.radioButton_3, self.radioButton_4, self.radioButton_5, self.radioButton_6, self.radioButton_7]
            type_to_pass = None
            for i in range(0, 5):
                if radios[i].isChecked():
                    type_to_pass = types[i]
                    break
            if self.food_list.item_id_exists(ItemID):
                raise ValueError("Item id exists already... please choose unique id")
            if not ItemID and not name and not category and not price and not ingrediants:
                raise ValueError("Please fill the given fields first.")

            elif not ItemID:
                 raise ValueError("Please enter Item ID.")
            elif not name:
                 raise ValueError("Please enter Item name.")
            elif not category:
                 raise ValueError("Please enter category.")
            elif not price:
                 raise ValueError("Please enter price.")
            elif not ingrediants:
                 raise ValueError("Please enter ingrediants.")  

            elif not any(radio.isChecked() for radio in radios):
                 raise ValueError("Please select the time required to cook.")

            if not ItemID or not name or not category or not price or not ingrediants:
                 raise ValueError("Please fill in all the text boxes.")                          
            isprice=validations.price_validation(price)
            isitemId=validations.int_validation(ItemID)
            isName=validations.name_validation(name)
            iscategory=validations.name_validation(category)
            
            if (isprice and isitemId and isName and iscategory )==True:
                 self.food_list.add_menu_item(ItemID, name, category, ingrediants, price, type_to_pass)
                 QMessageBox.information(self, "Success", "Item added successfully")
                 self.plainTextEdit_8.clear()
                 self.plainTextEdit_9.clear()
                 self.plainTextEdit_10.clear()
                 self.plainTextEdit.clear()
                 self.plainTextEdit_13.clear()
                 if any(radio.isChecked() for radio in radios):
                        for radio in radios:
                            radio.setChecked(False)
            else:
                if not isprice:
                    raise ValueError("Price should contains digits ..please enter digits")
                if not isitemId:
                     raise ValueError("Item Id should contains digits ..please enter digits")
                if not isName :
                    raise ValueError("Item name should not contains digits ")
                if not iscategory :
                    raise ValueError("category should not contains digits ...")
                     
                self.plainTextEdit_8.clear()
                self.plainTextEdit_9.clear()
                self.plainTextEdit_10.clear()
                self.plainTextEdit.clear()
                self.plainTextEdit_13.clear()
                if any(radio.isChecked() for radio in radios):
                    for radio in radios:
                        radio.setChecked(False)
                
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
            self.plainTextEdit_8.clear()
            self.plainTextEdit_9.clear()
            self.plainTextEdit_10.clear()
            self.plainTextEdit.clear()
            self.plainTextEdit_13.clear()
            if any(radio.isChecked() for radio in radios):
                for radio in radios:
                     radio.setChecked(False)

    def viewfeedbackAsAdmin(self):
        try:
            searchterm=self.plainTextEdit_24.toPlainText()
       
            if not searchterm:
                raise ValueError("please first fill the bar")
            else:    
                self.feedback.search_and_display(searchterm)
                QMessageBox.information(self,"success", "Feedback searched successfully")
                self.ui.load_table('tableView_8','searched_data.csv')
                self.plainTextEdit_24.clear()
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e)) 
            self.plainTextEdit_24.clear()   
    def refreshSearchAsAdmin(self):
        self.ui.load_table('tableView_8','output.csv')
# -------------------------------------------cutomer functions--------------------------------------
    def onbuttonclick78(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)        
        self.tableView_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table('tableView_5')
        self.ui.pushButton_26.clicked.connect(self.searching)

    def searching(self):
        try:
            searchtext = self.plainTextEdit_17.toPlainText()
            result = self.bst.search_and_store_all_to_csv(searchtext,'bstsearching_output.csv')

            if result:
                QMessageBox.information(self, 'Success', 'Item searched successfully')
                self.tableView_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.load_table('tableView_5','bstsearching_output.csv')

                self.plainTextEdit_17.clear()
            else:
                raise ValueError("Data not present")
                self.plainTextEdit_17.clear()
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))
            self.plainTextEdit_17.clear()

    def read_csv_and_store_bst(self,filename, bst):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bst.insert(
                    row['Item_ID'],
                    row['Name'],
                    row['Category'],
                    row['Ingredients'],
                    row['Price'],
                    row['Rating']
                )


    def Feedback(self):
        try:
            foodid=self.plainTextEdit_20.toPlainText()
            isid=validations.int_validation(foodid)
            if not isid:
                raise ValueError("please  enter id in digits ")
                
                self.plainTextEdit_20.clear()
            fedback=self.plainTextEdit_28.toPlainText()
            types = ['5', '4', '3', '2', '1']
            radios = [self.radioButton_27, self.radioButton_28, self.radioButton_29, self.radioButton_30, self.radioButton_31]
            type_to_pass = None
            for i in range(0, 5):
                if radios[i].isChecked():
                    type_to_pass = types[i]
                    break
            if not type_to_pass :
                return "N/A"        
            if not foodid and not fedback:
                raise ValueError("please fill the fileds ")     
            elif not foodid:
                raise ValueError("please enter food id to give feedback ") 
            elif not fedback:
                raise ValueError("please write feedback ") 

            food_item = self.food_list.find_food_by_id(foodid)
            if not food_item:
                raise ValueError("Item with ID  not found in the restaurant menu.")
            else:
           
                self.feedback.add_feedback(self.customerName,foodid,fedback,type_to_pass)  
                QMessageBox.information(self,"success", "Feedback added successfully") 
                self.feedback.write_feedback_to_csv('feedbacks.csv') 
                FeedBackView.view_feedbacks_from_stack(self.feedback_stack)
                self.plainTextEdit_20.clear()
                self.plainTextEdit_28.clear()  
                self.clearRating()  
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))
            self.plainTextEdit_20.clear()
            self.plainTextEdit_28.clear()
            self.clearRating()

    def viewfeedback(self):
        try:
            searchterm=self.plainTextEdit_23.toPlainText()
       
            if not searchterm:
                raise ValueError("please first fill the bar")
            else:    
                self.feedback.search_and_display(searchterm)
                QMessageBox.information(self,"success", "Feedback searched successfully")
                self.ui.load_table('tableView_7','searched_data.csv')
                self.plainTextEdit_23.clear()
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e)) 
            self.plainTextEdit_23.clear()   
    def refreshSearch(self):
        self.ui.load_table('tableView_7','output.csv')

    def clearRating(self):
        self.ui.radioButton_27.setAutoExclusive(False)
        self.ui.radioButton_28.setAutoExclusive(False)
        self.ui.radioButton_29.setAutoExclusive(False)
        self.ui.radioButton_30.setAutoExclusive(False)
        self.ui.radioButton_31.setAutoExclusive(False)

        self.ui.radioButton_27.setChecked(False)
        self.ui.radioButton_28.setChecked(False)
        self.ui.radioButton_29.setChecked(False)
        self.ui.radioButton_30.setChecked(False)
        self.ui.radioButton_31.setChecked(False)

        self.ui.radioButton_27.setAutoExclusive(True)
        self.ui.radioButton_28.setAutoExclusive(True)
        self.ui.radioButton_29.setAutoExclusive(True)
        self.ui.radioButton_30.setAutoExclusive(True)
        self.ui.radioButton_31.setAutoExclusive(True)


    def SortCustomer(self):
        try:

            algo = self.comboBox_8.currentText()
            
            col = self.comboBox_9.currentText()
            isSorted = False
            types = ['ascending', 'descending']
            radios = [self.radioButton_14, self.radioButton_13]
            type_to_pass = None
            for i in range(0, 2):
                if radios[i].isChecked():
                    type_to_pass = types[i]
                    break

            if algo == 'Select Sorting Algorithm' and col =='Select Column' and not any(radio.isChecked() for radio in radios):
                QMessageBox.information(self, "error", "please select  algorithm and column and sorting order")

            elif algo == 'Select Sorting Algorithm':
                QMessageBox.information(self, "error", "please select  algorithm first")
            elif col == 'Select Column':
                QMessageBox.information(self, "error", "please select  column no first")
            elif not any(radio.isChecked() for radio in radios):
                QMessageBox.information(self, "error", "please select a sorting order")
            if (algo in ['Pigeonhole Sort', 'Radix Sort']) and (
                    col in ['Name', 'Category', 'Ingredients']):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Error')
                msg.setText('The selected sorting algorithm is not applicable to string data.')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                sortingSystem.dataSorter(algo, col, type_to_pass)
                QMessageBox.information(self, "Success", "the column is sorted")

                isSorted = True
                self.ui.load_table('tableView_4','resturantsort.csv')
        except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")  
    def onButton36Clicked(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)        
        self.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table('tableView_4')
        self.ui.pushButton_11.clicked.connect(self.SortCustomer)
  
    def clearRatingorders(self):
        self.ui.radioButton_15.setAutoExclusive(False)
        self.ui.radioButton_16.setAutoExclusive(False)
        self.ui.radioButton_17.setAutoExclusive(False)
        self.ui.radioButton_18.setAutoExclusive(False)
        self.ui.radioButton_19.setAutoExclusive(False)

        self.ui.radioButton_15.setChecked(False)
        self.ui.radioButton_16.setChecked(False)
        self.ui.radioButton_17.setChecked(False)
        self.ui.radioButton_18.setChecked(False)
        self.ui.radioButton_19.setChecked(False)

        self.ui.radioButton_15.setAutoExclusive(True)
        self.ui.radioButton_16.setAutoExclusive(True)
        self.ui.radioButton_17.setAutoExclusive(True)
        self.ui.radioButton_18.setAutoExclusive(True)
        self.ui.radioButton_19.setAutoExclusive(True)



    def giveOrders(self):
        try:
            item_id=self.plainTextEdit_18.toPlainText()
            validid=validations.int_validation(item_id)
            quantity=self.plainTextEdit_29.toPlainText()
            validquantity=validations.int_validation(quantity)
            if not item_id and not quantity:
                raise ValueError("please enter in id and quantity for order")
            elif not validid:
                raise ValueError("please enter id in digits")
            elif not validquantity:
                raise ValueError("please enter in digits")
            elif not item_id:
                raise ValueError("please enter id first to give order")
            elif not quantity:
                raise ValueError("please enter quantity of your order")  
                 
            else:            
                current = self.food_list.head
                while current:
                    if current.item_id == item_id:
                        self.plainTextEdit_21.setPlainText(current.name)
                        self.plainTextEdit_22.setPlainText(current.Category)
                        self.plainTextEdit_3.setPlainText(current.Ingrediants)
                        self.plainTextEdit_19.setPlainText(current.Price)
                        rating = int(current.rating)
                        if rating == 5:
                            self.radioButton_15.setChecked(True)
                        elif rating == 4:
                            self.radioButton_16.setChecked(True)
                        elif rating == 3:
                            self.radioButton_17.setChecked(True)
                        elif rating == 2:
                            self.radioButton_18.setChecked(True)
                        elif rating == 1:
                            self.radioButton_19.setChecked(True)
                        
                        self.order_queue.enqueOrder(self.customerName, {
                            'Item_ID': current.item_id,
                            'Name': current.name,
                            'Category': current.Category,
                            'Ingredients': current.Ingrediants,
                            'Price': current.Price,
                            'Rating': current.rating
                        }, quantity)
                      
                        break
                    current = current.next_node
                else:
                    raise ValueError("Item with ID not found in the restaurant file.")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e)) 
            self.plainTextEdit_18.clear()   
            self.plainTextEdit_18.clear()       
    def proceed(self):
        try:
            item_id=self.plainTextEdit_18.toPlainText()
            validid=validations.int_validation(item_id)
            quantity=self.plainTextEdit_29.toPlainText()
            validquantity=validations.int_validation(quantity)
            
            if not item_id and not quantity:
                raise ValueError("please enter in id and quantity for order")
            elif not validid:
                raise ValueError("please enter id in digits")
            elif not validquantity:
                raise ValueError("please enter in digits")
            elif not item_id:
                raise ValueError("please enter id first to give order")
            elif not quantity:
                raise ValueError("please enter quantity of your order")  
            elif not self.plainTextEdit_21.toPlainText().strip() and not self.plainTextEdit_22.toPlainText().strip() and not  self.plainTextEdit_19.toPlainText().strip() and not self.plainTextEdit_3.toPlainText().strip():
                raise ValueError("please confirm your order")  
         
            else:
                self.order_queue.process_orders()
                QMessageBox.information(self,'success','you ordered succeddfully')
                self.plainTextEdit_18.clear()
                self.plainTextEdit_29.clear()
                self.plainTextEdit_21.clear()
                self.plainTextEdit_22.clear()
                self.plainTextEdit_3.clear()
                self.plainTextEdit_19.clear()
                self.clearRatingorders()
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e)) 
            self.plainTextEdit_18.clear()
            self.plainTextEdit_29.clear()
            self.plainTextEdit_21.clear()
            self.plainTextEdit_22.clear()
            self.plainTextEdit_3.clear()
            self.plainTextEdit_19.clear()
            self.clearRatingorders()


    def customerbill(self):
        try:
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_21) 
            self.tableView_9.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.bill.search_customer_bills(self.customerName)
            self.load_table('tableView_9','searched_bills.csv')
            QMessageBox.information(self,'success','your didnot have paid bill yet')
          
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))
          

      

# ---------------------------------------------GUest secreen--------------------------------------
    
    def onbuttonclick36(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_24)        
        self.tableView_13.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table('tableView_13')
        self.ui.pushButton_28.clicked.connect(self.searchingGuest)

    def searchingGuest(self):
        try:
            searchtext = self.plainTextEdit_36.toPlainText()
            result = self.bst.search_and_store_all_to_csv(searchtext,'bstsearching_output.csv')

            if result:
                QMessageBox.information(self, 'Success', 'Item searched successfully')
                self.tableView_13.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.load_table('tableView_13','bstsearching_output.csv')

                self.plainTextEdit_36.clear()
            else:
                raise ValueError("Data not present")
                self.plainTextEdit_36.clear()
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))
            self.plainTextEdit_36.clear()


    def SortGuest(self):
        try:

            algo = self.comboBox_12.currentText()
            
            col = self.comboBox_13.currentText()
            isSorted = False
            types = ['ascending', 'descending']
            radios = [self.radioButton_22, self.radioButton_23]
            type_to_pass = None
            for i in range(0, 2):
                if radios[i].isChecked():
                    type_to_pass = types[i]
                    break

            if algo == 'Select Sorting Algorithm' and col =='Select Column' and not any(radio.isChecked() for radio in radios):
                QMessageBox.information(self, "error", "please select  algorithm and column and sorting order")

            elif algo == 'Select Sorting Algorithm':
                QMessageBox.information(self, "error", "please select  algorithm first")
            elif col == 'Select Column':
                QMessageBox.information(self, "error", "please select  column no first")
            elif not any(radio.isChecked() for radio in radios):
                QMessageBox.information(self, "error", "please select a sorting order")
            if (algo in ['Pigeonhole Sort', 'Radix Sort']) and (
                    col in ['Name', 'Category', 'Ingredients']):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Error')
                msg.setText('The selected sorting algorithm is not applicable to string data.')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                sortingSystem.dataSorter(algo, col, type_to_pass)
                QMessageBox.information(self, "Success", "the column is sorted")

                isSorted = True
                self.ui.load_table('tableView_11','resturantsort.csv')
        except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")  
    def onButton39Clicked(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_25)        
        self.tableView_11.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table('tableView_11')
        self.ui.pushButton_18.clicked.connect(self.SortGuest)


    def viewfeedbackASGuest(self):
        try:
            searchterm=self.plainTextEdit_35.toPlainText()
       
            if not searchterm:
                raise ValueError("please first fill the bar")
            else:    
                self.feedback.search_and_display(searchterm)
                QMessageBox.information(self,"success", "Feedback searched successfully")
                self.ui.load_table('tableView_12','searched_data.csv')
                self.plainTextEdit_35.clear()
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e)) 
            self.plainTextEdit_35.clear()   
    def refreshSearchGuest(self):
        self.ui.load_table('tableView_12','output.csv')    
# --------------------------classess--------------------------------------------
class TableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        if self._data:
            return len(self._data[0])
        return 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        elif role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return self._data[row][col]
        else:
            return QVariant()  
    def headerData(self, p_int, Qt_Orientation, role=None):
        return self._data[0]             


class FoodNode:
    def __init__(self, item_id, name, Category, Ingrediants, Price, rating):
        self.item_id = item_id
        self.name = name
        self.Category = Category
        self.Ingrediants =Ingrediants
        self.Price = Price
        self.rating = rating
        self.next_node = None

class FoodLinkedList:
    def __init__(self):
        self.head = None

    def add_food(self, item_id, name, Category, Ingrediants, Price, rating):
        new_food = FoodNode(item_id, name, Category, Ingrediants, Price, rating)
        new_food.next_node = self.head
        self.head = new_food 

    def get_item_id_at_index(self, index):
        current = self.head
        for _ in range(index):
            current = current.next_node
        return current.item_id

    def item_id_exists(self, item_id):
        current = self.head
        while current:
            if current.item_id == item_id:
                return True
            current = current.next_node
        return False 
   
    def find_food_by_id(self, item_id):
        current = self.head
        while current:
            if current.item_id == item_id:
                return current
            current = current.next_node
        return None
    def delete_menu_item(self, item_id_to_delete):
        current = self.head
        previous = None
        isinteger=validations.int_validation(item_id_to_delete)
        if isinteger:
            while current:
                if current.item_id == item_id_to_delete:
                    if previous is None:
                        self.head = current.next_node
                    else:
                        previous.next_node = current.next_node
                    break

                previous = current
                current = current.next_node
            else:
                raise ValueError(f"Item with ID {item_id_to_delete} not found")
        else:
            raise ValueError("please enter digit ....")        

        with open('Resturant1.csv', 'w', newline='') as csvfile:
                fieldnames = ['Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                current = self.head
                while current:
                    writer.writerow({
                        'Item_ID': current.item_id,
                        'Name': current.name,
                        'Category': current.Category,
                        'Ingredients': current.Ingrediants,
                        'Price': current.Price,
                        'Rating': current.rating
                    })
                    current = current.next_node

    def update_menu_item(self, item_id_to_update, new_data):
        current = self.head
        found = False

        while current:
            if current.item_id == item_id_to_update:
               
                current.name = new_data.get('Name', current.name)
                current.Category = new_data.get('Category', current.Category)
                current.Ingrediants = new_data.get('Ingredients', current.Ingrediants)
                current.Price = new_data.get('Price', current.Price)
                current.rating = new_data.get('Rating', current.rating)

                print(f"Menu item with ID {item_id_to_update} updated.")
                found = True
                break  
            
           
            current = current.next_node
        if not found:
             raise ValueError("ID not found")
        if found:
            menu_items = []
            with open('Resturant1.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                menu_items = list(reader)

            for item in menu_items:
                if item['Item_ID'] == item_id_to_update:
                  
                    item.update({
                       
                        'Name': new_data.get('Name', item['Name']),
                        'Category': new_data.get('Category', item['Category']),
                        'Ingredients': new_data.get('Ingredients', item['Ingredients']),
                        'Price': new_data.get('Price', item['Price']),
                        'Rating': new_data.get('Rating', item['Rating'])
                    })
                  

          
            with open('Resturant1.csv', 'w', newline='') as csvfile:
                fieldnames = ['Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                writer.writerows(menu_items)

            return

        print(f"Menu item with ID {item_id_to_update} not found.")
        return
        
    def add_menu_item(self, item_id, name, Category, Ingrediants, Price, rating):
        new_menu_item = FoodNode(item_id, name, Category, Ingrediants, Price, rating)

        if not self.head:
            self.head = new_menu_item
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_menu_item

        with open('Resturant1.csv', 'a', newline='') as csvfile:
            fieldnames = ['Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                'Item_ID': new_menu_item.item_id,
                'Name': new_menu_item.name,
                'Category': new_menu_item.Category,
                'Ingredients': new_menu_item.Ingrediants,
                'Price': new_menu_item.Price,
                'Rating': new_menu_item.rating
            })


def read_csv_and_store(filename, linked_list):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"Reading row: {row}")
            linked_list.add_food(
                row['Item_ID'],
                row['Name'],
                row['Category'],
                row['Ingredients'],
                row['Price'],
                row['Rating']
            )


if __name__ == "__main__":
    import sys
   
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
