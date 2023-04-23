import dnf
import queue
import os
import subprocess
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

@store_in_queue
def query_available_packages(filtr):
    base = dnf.Base()
    base.read_all_repos()
    base.fill_sack()
    q = base.sack.query()
    i = q.available()
    if filtr:
        i = i.filter(name=filtr)
    else:
        i = i.filter(name="dnf")   
    packages = list(i)  # i only gets evaluated here
    print("Available dnf package:")
    r = q.run()
    print(packages)
    return packages

def install_packages(pkg):
    os.system(f'pkexec sudo -u root dnf -y install {pkg} ')
    #subprocess.call(['pkexec',f'sudo dnf install {pkg} -y '])
    print("installing: ", pkg) 
    #packages = list(i)  # i only gets evaluated here
    print("installed dnf packages:")
    
    return pkg

if __name__ == "__main__":
    install_packages("screenfetch-3.9.1-8.fc38.noarch")