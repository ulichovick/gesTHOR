import os
import subprocess
import gi
from threading import Thread
from dnf_test import query_local_packages, query_available_packages, my_queue
from dnf_install import install_packages
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


    def pressedInstall(self, button):
        to_install_pkg = results_avail.get_selection()
        to_install_pkg.connect('changed', self.on_tree_selection_changed)
        (model, pathlist) =  to_install_pkg.get_selected_rows()
        for path in pathlist :
            tree_iter = model.get_iter(path)
            print("to install", model.get_iter(path))
            to_install.append([str(model.get_value(tree_iter,0))])

    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter != None:
            print ("You selected", model[treeiter][0])

    def another_spin(self):
        Instalando_spinner.start()
        label_res_ins.set_text("Instalando")
        return False

    def install_in_another_thread(self):
        GLib.idle_add(self.another_spin)
        cwd = os.getcwd()
        cwd = cwd + "/dnf_install.py"
        print("pkgs to be installed: ", self.pkg_installing)
        #installed = install_packages(self.pkg_installing)
        #test = os.system(f'pkexec python3 dnf_install.py -p {self.pkg_installing} ')
        try:
            subprocess.call(['pkexec',"sudo", "-u", "root", "python3", cwd, "-p", self.pkg_installing ])
            label_res_ins.set_text(str("Paquetes instalados exitosamente "+self.pkg_installing))
        except subprocess.CalledProcessError as e:
            print(e.output)
        print("paquete instalado exitosamente!")
        Instalando_spinner.stop()
        return True

    def Installing_pkgs(self, button):
        to_install_pkgs = pkgs_to_install.get_selection()
        to_install_pkgs.connect('changed', self.installing)
        (model, pathlist) =  to_install_pkgs.get_selected_rows()
        for path in pathlist :
            tree_iters = model.get_iter(path)
            print("to install", model.get_iter(path))
        self.pkg_installing = str(model.get_value(tree_iters,0))
        thread = Thread(target=self.install_in_another_thread)
        thread.daemon = True
        thread.start()

    def installing(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter != None:
            print ("You selected", model[treeiter][0])
        

builder = Gtk.Builder()
builder.add_from_file("test.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
installed_filter = builder.get_object("installed_filter")
available_filter = builder.get_object("available_filter")
available_spinner = builder.get_object("available_spinner")
installed_spinner = builder.get_object("installed_spinner")
Instalando_spinner = builder.get_object("Instalando")
res_install = builder.get_object("resultados_installe")
to_install = builder.get_object("resultados_avail_ins")
res_avail = builder.get_object("resultados_availabl")
results_avail = builder.get_object("resultados_avail")
pkgs_to_install = builder.get_object("resultados_avail_install")
label_res_ins = builder.get_object("Resultado Ins")


window.show_all()

Gtk.main()
