import os
import subprocess
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

    def AddPackages(self, button):
        to_install_pkg = results_avail.get_selection()
        to_install_pkg.connect('changed', self.on_tree_selection_changed)
        (model, pathlist) =  to_install_pkg.get_selected_rows()
        for path in pathlist :
            tree_iter = model.get_iter(path)
            print("to Add", model.get_iter(path))
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
        pkgs = ' '.join(self.pkg_to_install)
        print("pkgs to be installed: ", pkgs)
        try:
            subprocess.call(['pkexec',"sudo", "-u", "root", "python3", cwd, "--package", pkgs])
            label_res_ins.set_text(str("Paquetes instalados exitosamente: "+pkgs))
        except subprocess.CalledProcessError as e:
            print(e.output)
        Instalando_spinner.stop()
        return True

    def Installing_pkgs(self, button):
        to_install_pkgs = pkgs_to_install.get_selection()
        to_install_pkgs.connect('changed', self.installing)
        self.pkg_to_install = []
        (model, pathlist) =  to_install_pkgs.get_selected_rows()
        for path in pathlist :
            tree_iters = model.get_iter(path)
            print("to install", model.get_iter(path))
            self.pkg_to_install.append(model.get_value(tree_iters,0))
        print("package to install", self.pkg_to_install)
        thread = Thread(target=self.install_in_another_thread)
        thread.daemon = True
        thread.start()

    def installing(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter != None:
            print ("You selected", model[treeiter][0])



#-----------------------------Espacio reservado para pestaña de desinstalar-----------------------------


    def unins_spin(self):
        desinstalando_spinner.start()
        label_res_ins.set_text("Instalando")
        return False

    def onButtonInstalledPressed(self, button):
        res_install.clear()
        installed_filters = installed_filter.get_text()
        installed_spinner.start()
        installed_data = query_local_packages(installed_filters)
        for pkg in installed_data:
            res_install.append([str(pkg)])
        installed_spinner.stop()

    def add_pkgs_to_uninstall(self, button):
        to_install_pkg = resultados_instalados.get_selection()
        to_install_pkg.connect('changed', self.on_tree_selection_changed)
        (model, pathlist) =  to_install_pkg.get_selected_rows()
        for path in pathlist :
            tree_iter = model.get_iter(path)
            print("to Add", model.get_iter(path))
            a_desinstalar.append([str(model.get_value(tree_iter,0))])

    def uninstall_in_another_thread(self):
        GLib.idle_add(self.another_spin)
        cwd = os.getcwd()
        cwd = cwd + "/dnf_uninstall.py"
        pkgs = ' '.join(self.pkg_to_uninstall)
        print("pkgs to be installed: ", pkgs)
        try:
            subprocess.call(['pkexec', "--user", "root", "sudo", "-u", "root", "python3", cwd, "--package", pkgs])
            resultado_desins.set_text(str("Paquetes desinstalados exitosamente: "+pkgs))
        except subprocess.CalledProcessError as e:
            print(e.output)
        desinstalando_spinner.stop()
        return True

    def desinstalar_pkgs(self, button):
        to_uninstall_pkgs = desinstalando.get_selection()
        to_uninstall_pkgs.connect('changed', self.installing)
        self.pkg_to_uninstall = []
        (model, pathlist) =  to_uninstall_pkgs.get_selected_rows()
        for path in pathlist :
            tree_iters = model.get_iter(path)
            print("to install", model.get_iter(path))
            self.pkg_to_uninstall.append(model.get_value(tree_iters,0))
        print("package to install", self.pkg_to_uninstall)
        thread = Thread(target=self.uninstall_in_another_thread)
        thread.daemon = True
        thread.start()


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


#-------------------------------elementos de pestaña de desinstalar-------------------------------


resultados_instalados = builder.get_object("pkgs_instalados")
a_desinstalar = builder.get_object("pkgs_a_desins")
desinstalando = builder.get_object("pkgs_a_desinstalar")
resultado_desins = builder.get_object("resultado_desins")
desinstalando_spinner = builder.get_object("desinstalando")
window.show_all()

Gtk.main()
