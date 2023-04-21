import gi
from dnf_test import query_local_packages, query_available_packages

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonAvailablePressed(self, button):
        res_avail.clear()
        available_filters = available_filter.get_text()
        print(available_filters)
        available_spinner.start()
        available_data = query_available_packages(available_filters)
        for pkg in available_data:
            res_avail.append([str(pkg)])
        available_spinner.stop()
    
    def onButtonInstalledPressed(self, button):
        res_install.clear()
        installed_filters = installed_filter.get_text()
        print(installed_filters)
        installed_data = query_local_packages(installed_filters)
        for pkg in installed_data:
            res_install.append([str(pkg)])

builder = Gtk.Builder()
builder.add_from_file("test.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
installed_filter = builder.get_object("installed_filter")
available_filter = builder.get_object("available_filter")
available_spinner = builder.get_object("available_spinner")
res_install = builder.get_object("resultados_installe")
res_avail = builder.get_object("resultados_availabl")

window.show_all()

Gtk.main()
