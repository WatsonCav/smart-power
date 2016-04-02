# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRecloser.ui'
#
# Created: Sun Feb  8 22:33:29 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys
from Cadastro import CadastroDialog

class sceneRecloserDialog(QtGui.QGraphicsScene):
    def __init__ (self, rect):
        super(sceneRecloserDialog, self).__init__(rect)
        pass

class RecloserDialog(QtGui.QWidget):
    def __init__(self, item):
        super(RecloserDialog, self).__init__()
        self.dialog = QtGui.QDialog(self)
        self.elementTitle = "Interrupção"
        self.item = item
        self.scene = self.item.scene()
        self.setupUi(self.dialog)
        self.dialog.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(380, 210)
        sc = 11.0
        #Dialog.resize(380, 80+33*sc)
        Dialog.setFixedSize(380, 80+33*sc)

        #CW1
        ###
        #Define a tabWidget que contém as configurações
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 360, 20+33*sc))
        self.tabWidget.setObjectName("tabWidget")
        ###

        #Define o tamanho da caixa dialogo
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 40+33*sc, 341, 32))
        #Define o tamanho do layout dos botões do dialogo
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.cadastro = QtGui.QPushButton('Cadastrar Novo')
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.addButton(self.cadastro, QtGui.QDialogButtonBox.ActionRole)
        self.buttonBox.clicked.connect(self.cadastrar)


        #CW1
        ###
        ### Define e configura as Tabs Tipo e Configuração
        ### A aba configuração varia com cada tipo de elemento. Sempre que um novo
        ### elemento for selecionado na aba Tipo, esta aba sofrerá alterações.
        self.widgetType = QtGui.QWidget()
        self.widgetConfig = QtGui.QWidget()
        self.widgetType.setGeometry(QtCore.QRect(11, 11, 300, (33*sc)-80))
        self.widgetConfig.setGeometry(QtCore.QRect(11, 11, 300, (33*sc)-80))
        self.widgetType.setObjectName("widgetType")
        self.widgetConfig.setObjectName("widgetConfig")        


        ###
        #Define a Tab Tipo e o seu Layout 
        self.formLayoutType = QtGui.QFormLayout(self.widgetType)
        self.formLayoutType.setContentsMargins(7, 5, 7, 7)
        self.formLayoutType.setObjectName("formLayoutType")
        self.tabWidget.addTab(self.widgetType,u"Tipo")

        self.subWidgetType = QtGui.QWidget()
        self.subWidgetType.setObjectName("subWidgetType")
        self.formLayoutType.setWidget(2, QtGui.QFormLayout.LabelRole, self.subWidgetType)
        self.subFormLayoutType = QtGui.QFormLayout(self.subWidgetType)
        self.formLayoutType.setObjectName("subFormLayoutType")

        self.tipoElementoCheck = QtGui.QButtonGroup()
        self.tipoElementoCheck.addButton(QtGui.QCheckBox(u"Chave",self.widgetConfig), 0)        
        self.tipoElementoCheck.addButton(QtGui.QCheckBox(u"Chave autom.",self.widgetConfig), 1)
        self.tipoElementoCheck.addButton(QtGui.QCheckBox(u"Disjuntor",self.widgetConfig), 2)
        self.tipoElementoCheck.addButton(QtGui.QCheckBox(u"Religador",self.widgetConfig), 3)
        self.tipoElementoCheck.addButton(QtGui.QCheckBox(u"Rel. e TC/TP",self.widgetConfig), 4)
        self.tipoElementoCheck.setExclusive(True)
        self.tipoElementoCheck.buttons()[self.item.chave.tipo].setChecked(True)

        for item in self.tipoElementoCheck.buttons():
            item.setObjectName("tipoElementoCheck"+str(self.tipoElementoCheck.id(item)))
            self.subFormLayoutType.setWidget((self.tipoElementoCheck.id(item)), QtGui.QFormLayout.LabelRole, item)
        self.tipoElementoCheck.buttonClicked[int].connect(self.setElementTitle)

        #definição da propriedade TIPO DE ELEMENTO INTERRUPTOR:
        self.tipoElementoLabel = QtGui.QLabel(self.widgetConfig)
        self.tipoElementoLabel.setObjectName("tipoElementoLabel")
        self.formLayoutType.setWidget(1, QtGui.QFormLayout.LabelRole, self.tipoElementoLabel)

        #definição da propriedade NOME
        self.identificaOLabel = QtGui.QLabel(self.widgetConfig)
        self.identificaOLabel.setObjectName("identificaOLabel")
        self.formLayoutType.setWidget(0, QtGui.QFormLayout.LabelRole, self.identificaOLabel)
        self.identificaOLineEdit = QtGui.QLineEdit(self.widgetConfig)
        self.identificaOLineEdit.setObjectName("identificaOLineEdit")
        self.identificaOLineEdit.setPlaceholderText(self.item.text.toPlainText())
        self.formLayoutType.setWidget(0, QtGui.QFormLayout.FieldRole, self.identificaOLineEdit)
        self.identificaOLineEdit.textChanged.connect(self.en_dis_button)

        #definição do ícone do elemento
        self.elementScene = QtGui.QGraphicsScene( 0, 0, 33, 33)
        self.elementView = QtGui.QGraphicsView(self.elementScene)
        #self.elementView.resize(0,0,75,75)
        self.formLayoutType.setWidget(2, QtGui.QFormLayout.FieldRole, self.elementView)


        ###
        #Define a Tab Configuração e o seu Layout
        self.formLayout = QtGui.QFormLayout(self.widgetConfig)
        self.formLayout.setContentsMargins(7, 5, 7, 7)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget.addTab(self.widgetConfig,u"Configuração")

        #definição da propriedade CORRENTE NOMINAL
        self.correnteNominalLabel = QtGui.QLabel(self.widgetConfig)
        self.correnteNominalLabel.setObjectName("correnteNominalLabel")
        self.correnteNominalLineEdit = QtGui.QLineEdit(self.widgetConfig)
        self.correnteNominalLineEdit.setObjectName("correnteNominalLineEdit")
        self.correnteNominalLineEdit.setText(str(self.item.chave.ratedCurrent))
        self.correnteNominalLineEdit.textEdited.connect(self.custom)

        #definição da propriedade CAPACIDADE DE INTERRUPÇÃO
        self.capacidadeDeInterrupOLabel = QtGui.QLabel(self.widgetConfig)
        self.capacidadeDeInterrupOLabel.setObjectName("capacidadeDeInterrupOLabel")
        self.capacidadeDeInterrupOLineEdit = QtGui.QLineEdit(self.widgetConfig)
        self.capacidadeDeInterrupOLineEdit.setObjectName("capacidadeDeInterrupOLineEdit")
        self.capacidadeDeInterrupOLineEdit.setText(str(self.item.chave.breakingCapacity))
        self.capacidadeDeInterrupOLineEdit.textEdited.connect(self.custom)

        #definição da propriedade Nº DE SEQUENCIA DE RELIGAMENTO
        self.nDeSequNciasDeReligamentoLabel = QtGui.QLabel(self.widgetConfig)
        self.nDeSequNciasDeReligamentoLabel.setObjectName("nDeSequNciasDeReligamentoLabel")
        self.nDeSequNciasDeReligamentoLineEdit = QtGui.QLineEdit(self.widgetConfig)
        self.nDeSequNciasDeReligamentoLineEdit.setObjectName("nDeSequNciasDeReligamentoLineEdit")
        self.nDeSequNciasDeReligamentoLineEdit.setText(str(self.item.chave.recloseSequences))
        self.nDeSequNciasDeReligamentoLineEdit.textEdited.connect(self.custom)

        #definição dos campos void para preenchimento de espaços vazios
        self.voidText = QtGui.QWidget()
        self.voidText.setObjectName("voidText")
        self.voidButton = QtGui.QWidget()
        self.voidButton.setObjectName("voidButton")
        
        # Definição da COMBOBOX
        self.testeLabel = QtGui.QLabel(self.widgetConfig)
        self.testeLabel.setObjectName("testeLabel")
        self.testeLineEdit = QtGui.QComboBox(self.widgetConfig)
        self.testeLineEdit.setObjectName("testeEdit")
        self.testeLineEdit.addItems(self.scene.dict_prop.keys())
        self.testeLineEdit.insertItem(0,"Custom")
        index = self.testeLineEdit.findText(self.item.text_config)
        # if index < 0:
        #     index = 0
        self.testeLineEdit.setCurrentIndex(index)
        self.testeLineEdit.currentIndexChanged.connect(self.update_values)

        # Seleciona quais propriedades estarão disponíveis para o tipo de elemento.   
        self.setConfigTab(self.item.chave.tipo)


        lista_comp = [int(self.capacidadeDeInterrupOLineEdit.text()), int(self.correnteNominalLineEdit.text()), int(self.nDeSequNciasDeReligamentoLineEdit.text())]
        print lista_comp

        if self.identificaOLineEdit.text() == "":
            print self.buttonBox.buttons()
            self.buttonBox.buttons()[0].setEnabled(False)
        else:
            self.buttonBox.buttons()[0].setEnabled(True)
        if self.identificaOLineEdit.placeholderText() != "":
            self.buttonBox.buttons()[0].setEnabled(True)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def setConfigTab(self, id):
        ### precisa conectar ao sinal de mudança de elemento
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.correnteNominalLabel)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.correnteNominalLineEdit)

        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.capacidadeDeInterrupOLabel)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.capacidadeDeInterrupOLineEdit)
        
        if (id!=3):
            self.formLayout.removeWidget(self.nDeSequNciasDeReligamentoLabel)
            self.nDeSequNciasDeReligamentoLabel.setVisible(False)

            self.formLayout.removeWidget(self.nDeSequNciasDeReligamentoLineEdit)
            self.nDeSequNciasDeReligamentoLineEdit.setVisible(False)

            self.formLayout.removeWidget(self.testeLineEdit)
            self.testeLineEdit.setVisible(False)

            self.formLayout.removeWidget(self.testeLabel)
            self.testeLabel.setVisible(False)

        else:
            self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.nDeSequNciasDeReligamentoLabel)
            self.nDeSequNciasDeReligamentoLabel.setVisible(True)

            self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.nDeSequNciasDeReligamentoLineEdit)
            self.nDeSequNciasDeReligamentoLineEdit.setVisible(True)
            
            self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.testeLineEdit)
            self.testeLineEdit.setVisible(True)

            self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.testeLabel)
            self.testeLabel.setVisible(True)


    def en_dis_button(self):

        if self.identificaOLineEdit.text() == "":
            #print self.buttonBox.buttons()
            self.buttonBox.buttons()[0].setEnabled(False)
        else:
            self.buttonBox.buttons()[0].setEnabled(True)

    def setElementTitle(self):
        for item in self.tipoElementoCheck.buttons():
            if item.isChecked():
                self.elementTitle = str(item.text())
                self.setConfigTab(self.tipoElementoCheck.id(item))
                #print item.text()
                #print self.elementTitle
        self.retranslateUi(self.dialog)


    def update_values(self, index):

        if index == 0:
            return

        self.correnteNominalLineEdit.setText(str(self.scene.dict_prop[self.testeLineEdit.currentText()]['Corrente Nominal']))
        self.capacidadeDeInterrupOLineEdit.setText(str(self.scene.dict_prop[self.testeLineEdit.currentTReligadorext()]['Capacidade de Interrupcao']))
        self.nDeSequNciasDeReligamentoLineEdit.setText(str(self.scene.dict_prop[self.testeLineEdit.currentText()]['Sequencia']))


    def custom(self):
        self.testeLineEdit.setCurrentIndex(0)

    def setFormaDialog(self):
        self.dialog.resize(530,370)


    def cadastrar(self, button):
        role = self.buttonBox.buttonRole(button)
        if role == QtGui.QDialogButtonBox.ActionRole:


            cadastro = CadastroDialog()
            if cadastro.dialog.result() == 1:
                if cadastro.nomeDoCadastroLineEdit.text() == '':
                    return
                self.scene.create_dict_recloser(
                    self.correnteNominalLineEdit.text(),
                    self.capacidadeDeInterrupOLineEdit.text(),
                    self.nDeSequNciasDeReligamentoLineEdit.text(),
                    cadastro.nomeDoCadastroLineEdit.text())
                self.testeLineEdit.addItem(cadastro.nomeDoCadastroLineEdit.text())
                self.testeLineEdit.setCurrentIndex(self.testeLineEdit.count()-1)



    def teste(self):
        print "teste"


    def retranslateUi(self, Dialog):

        #Tradução dos nomes dados aos objetos para os nomes gráficos do programa
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", self.elementTitle + " - Propriedades", None, QtGui.QApplication.UnicodeUTF8))
        #print "ok"
        self.identificaOLabel.setText(QtGui.QApplication.translate("Dialog", "Identificação:", None, QtGui.QApplication.UnicodeUTF8))
        self.correnteNominalLabel.setText(QtGui.QApplication.translate("Dialog", "Corrente Nominal (A): ", None, QtGui.QApplication.UnicodeUTF8))
        self.capacidadeDeInterrupOLabel.setText(QtGui.QApplication.translate("Dialog", "Capacidade de Interrupção (kA):", None, QtGui.QApplication.UnicodeUTF8))
        self.nDeSequNciasDeReligamentoLabel.setText(QtGui.QApplication.translate("Dialog", "Nº de Sequências de Religamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoElementoLabel.setText(QtGui.QApplication.translate("Dialog", "Tipo de interruptor:", None, QtGui.QApplication.UnicodeUTF8))
        self.testeLabel.setText(QtGui.QApplication.translate("Dialog", "Fabricante:", None, QtGui.QApplication.UnicodeUTF8))

    if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        dialogReligador = RecloserDialog()
        sys.exit(app.exec_())