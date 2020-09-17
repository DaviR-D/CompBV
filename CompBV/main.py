from threading import Thread
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from resultHandler import difHandler
from compare import comp


resultListCache = []
folderListCache = []
userOptionCopy = False
userOptionDelete = False


class Comp(Gtk.Window):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("interface/comp.glade")
        builder.add_from_file("interface/window2.glade")
        self.mainWindow = builder.get_object("window1")
        self.resultWindow = builder.get_object("window2")
        self.resultText = builder.get_object("text")
        self.mainWindow.set_title("Backup Verificator")
        self.mainButton = builder.get_object("bt1")
        self.copyButton = builder.get_object("copyButton")
        self.deleteButton = builder.get_object("deleteButton")
        self.select1 = builder.get_object("select1")
        self.select2 = builder.get_object("select2")
        self.confirmDialog = builder.get_object("dialog")
        self.mainWindow.connect("delete-event", Gtk.main_quit)
        self.textbuffer = self.resultText.get_buffer()
        builder.connect_signals(self)
        self.resultList = ""
        self.contResults = 0

    # Método usado para armazenar os resultados e mostrá-los
    def addResults(self, results):
        for file in results:
            self.resultList = self.resultList + file + '\n'
            self.contResults = self.contResults + 1

        self.textbuffer = self.resultText.get_buffer()
        self.textbuffer.set_text(self.resultList)

    def onMainButtonClicked(self, widget):
        global resultListCache
        global folderListCache
        global userOptionCopy
        global userOptionDelete

        self.varReset()
        self.resultWindowReset()

        f1 = self.select1.get_filename()
        f2 = self.select2.get_filename()

        resultListCache, folderListCache = comp.folderManager(f1, f2, 1)
        self.addResults(resultListCache)

    def onCopyButtonClicked(self, widget):
        global resultListCache
        global folderListCache
        global userOptionCopy
        global userOptionDelete

        self.confirmDialog.set_text("Você tem certeza que deseja COPIAR TODOS os arquivos diferentes?")
        self.copyButton.set_label("Sim")
        self.deleteButton.set_label("Não")

        if userOptionCopy is True:
            difHandler.copy(resultListCache, folderListCache)
            self.resultWindow.destroy()
            self.resultWindowReset()
            resultListCache = []
            folderListCache = []
            return

        if userOptionDelete is True:
            self.resultWindow.destroy()
            self.resultWindowReset()
            return

        userOptionCopy = True

    def onDeleteButtonClicked(self, widget):
        global resultListCache
        global folderListCache
        global userOptionCopy
        global userOptionDelete

        self.confirmDialog.set_text("Você tem certeza que deseja DELETAR TODOS os arquivos diferentes?")
        self.copyButton.set_label("Não")
        self.deleteButton.set_label("Sim")

        if userOptionDelete is True:
            difHandler.delete(resultListCache)
            self.resultWindow.destroy()
            self.resultWindowReset()
            resultListCache = []
            folderListCache = []
            return

        if userOptionCopy is True:
            self.resultWindow.destroy()
            self.resultWindowReset()
            return

        userOptionDelete = True

    # Zera as variáveis
    def varReset(self):
        global resultListCache
        global folderListCache

        resultListCache = []
        folderListCache = []
        self.textbuffer = self.resultText.get_buffer()
        self.textbuffer.set_text("")
        self.resultList = ""
        self.contResults = 0

    # Redeclara os objetos da segunda janela
    def resultWindowReset(self):
        global userOptionCopy
        global userOptionDelete

        builder = Gtk.Builder()
        builder.add_from_file("interface/window2.glade")
        self.resultWindow = builder.get_object("window2")
        self.resultText = builder.get_object("text")
        self.copyButton = builder.get_object("copyButton")
        self.deleteButton = builder.get_object("deleteButton")
        self.confirmDialog = builder.get_object("dialog")
        userOptionCopy = False
        userOptionDelete = False
        builder.connect_signals(self)
        self.resultWindow.set_default_size(700,300)
        self.resultWindow.show_all()


win = Comp()
win.mainWindow.show()
Gtk.main()
