import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from resultHandler import dif_handler
from compare import comp


result_list_cache = []
folder_list_cache = []
user_option_copy = False
user_option_delete = False


class Comp(Gtk.Window):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("interface/comp.glade")
        builder.add_from_file("interface/window2.glade")
        self.main_window = builder.get_object("window1")
        self.result_window = builder.get_object("window2")
        self.result_text = builder.get_object("text")
        self.main_window.set_title("Backup Verificator")
        self.main_button = builder.get_object("bt1")
        self.copy_button = builder.get_object("copy_button")
        self.delete_button = builder.get_object("delete_button")
        self.select1 = builder.get_object("select1")
        self.select2 = builder.get_object("select2")
        self.confirm_dialog = builder.get_object("dialog")
        self.main_window.connect("delete-event", Gtk.main_quit)
        self.textbuffer = self.result_text.get_buffer()
        builder.connect_signals(self)
        self.result_list = ""
        self.cont_results = 0

    # Método usado para armazenar os resultados e mostrá-los
    def add_results(self, results):
        for file in results:
            self.result_list = self.result_list + file + '\n'
            self.cont_results = self.cont_results + 1

        self.textbuffer = self.result_text.get_buffer()
        self.textbuffer.set_text(self.result_list)

    def on_main_button_clicked(self, widget):
        global result_list_cache
        global folder_list_cache
        global user_option_copy
        global user_option_delete

        self.var_reset()
        self.result_window_reset()

        f1 = self.select1.get_filename()
        f2 = self.select2.get_filename()
        result_list_cache, folder_list_cache = comp.compFolders(f1, f2)
        self.add_results(result_list_cache)

    def on_copy_button_clicked(self, widget):
        global result_list_cache
        global folder_list_cache
        global user_option_copy
        global user_option_delete

        self.confirm_dialog.set_text("Você tem certeza que deseja COPIAR TODOS os arquivos diferentes?")
        self.copy_button.set_label("Sim")
        self.delete_button.set_label("Não")

        if user_option_copy is True:
            dif_handler.copy(result_list_cache, folder_list_cache)
            self.result_window.destroy()
            self.result_window_reset()
            result_list_cache = []
            folder_list_cache = []
            return

        if user_option_delete is True:
            self.result_window.destroy()
            self.result_window_reset()
            return

        user_option_copy = True

    def on_delete_button_clicked(self, widget):
        global result_list_cache
        global folder_list_cache
        global user_option_copy
        global user_option_delete

        self.confirm_dialog.set_text("Você tem certeza que deseja DELETAR TODOS os arquivos diferentes?")
        self.copy_button.set_label("Não")
        self.delete_button.set_label("Sim")

        if user_option_delete is True:
            dif_handler.delete(result_list_cache)
            self.result_window.destroy()
            self.result_window_reset()
            result_list_cache = []
            folder_list_cache = []
            return

        if user_option_copy is True:
            self.result_window.destroy()
            self.result_window_reset()
            return

        user_option_delete = True

    # Zera as variáveis
    def var_reset(self):
        global result_list_cache
        global folder_list_cache

        result_list_cache = []
        folder_list_cache = []
        self.textbuffer = self.result_text.get_buffer()
        self.textbuffer.set_text("")
        self.result_list = ""
        self.cont_results = 0

    # Redeclara os objetos da segunda janela
    def result_window_reset(self):
        global user_option_copy
        global user_option_delete

        builder = Gtk.Builder()
        builder.add_from_file("interface/window2.glade")
        self.result_window = builder.get_object("window2")
        self.result_text = builder.get_object("text")
        self.copy_button = builder.get_object("copy_button")
        self.delete_button = builder.get_object("delete_button")
        self.confirm_dialog = builder.get_object("dialog")
        user_option_copy = False
        user_option_delete = False
        builder.connect_signals(self)
        self.result_window.show_all()


win = Comp()
win.main_window.show()
Gtk.main()
