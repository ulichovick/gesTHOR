import gi
from threading import Thread
from dnf_test import query_local_packages, query_available_packages, my_queue
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def spin(self):
        available_spinner.start()
        return False

    def another_thread(self):
        available_filters = available_filter.get_text()
        GLib.idle_add(self.spin)
        self.data = query_available_packages(available_filters)
        self.pkgs = my_queue.get()
        available_spinner.stop()
        for pkg in self.pkgs:
            res_avail.append([str(pkg)])
        return self.data

    def onButtonAvailablePressed(self, button):
        res_avail.clear()
        thread = Thread(target=self.another_thread)
        thread.daemon = True
        thread.start()

    def onButtonInstalledPressed(self, button):
        res_install.clear()
        installed_filters = installed_filter.get_text()
        installed_spinner.start()
        installed_data = query_local_packages(installed_filters)
        for pkg in installed_data:
            res_install.append([str(pkg)])
        installed_spinner.stop()

builder = Gtk.Builder()
builder.add_from_file("test.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
installed_filter = builder.get_object("installed_filter")
available_filter = builder.get_object("available_filter")
available_spinner = builder.get_object("available_spinner")
installed_spinner = builder.get_object("installed_spinner")
res_install = builder.get_object("resultados_installe")
res_avail = builder.get_object("resultados_availabl")

window.show_all()

Gtk.main()
