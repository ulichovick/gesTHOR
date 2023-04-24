#!/usr/bin/sudo /usr/bin/python3
import dnf
import dnf.cli
import queue
import os

my_queue = queue.Queue()

def store_in_queue(f):
    def wrapper(*args):
        my_queue.put(f(*args))
    return wrapper

def query_local_packages(filtr):
    base = dnf.Base()
    base.fill_sack()
    q = base.sack.query()
    i = q.installed()
    print(filtr)
    if filtr:
        i = i.filter(name=filtr)
    #else:
    #    i = i.filter(name="dnf")
    packages = list(i)  # i only gets evaluated here
    print("Installed dnf package:")
    r = q.run()
    print(packages)
    return packages

#@store_in_queue
def query_available_packages(filtr):
    base = dnf.Base()
    base.read_all_repos()
    base.fill_sack()
    q = base.sack.query()
    i = q.available()
    if filtr:
        k = i.filter(name=filtr)
        j = k.filter(pkg=k)
    else:
        i = i.filter(pkg="dnf")   
        j = j.filter(pkg=i)
    packages = list(k)  # i only gets evaluated here
    packages_2 = list(j)
    print("Available dnf package:")
    r = q.run()
    print(packages)
    print(packages_2)
    return packages_2

def install_packages(pkg):
    base = dnf.Base()
    base.conf.read()
    dnf.cli.demand.DemandSheet
    base.setup_loggers()
    base.read_all_repos()
    base.fill_sack()
    q = base.sack.query()
    i = q.filter(name=pkg)
    packages = list(i)
    packages_to = []
    for pkg in packages:
        packages_to = pkg
    print("i ", packages_to)
    #pkg_to_install = base.download_packages(packages_to)
    print("pkg_to_install", packages_to)
    base.install(str(packages_to))
    base.resolve()
    base.download_packages(base.transaction.install_set)
    base.do_transaction()
    
    return pkg

if __name__ == "__main__":
    #pkg_to_install = query_available_packages("screenfetch")
    install_packages("screenfetch")