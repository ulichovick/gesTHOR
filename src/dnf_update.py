import dnf
import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("-p", "--package")
#args = parser.parse_args()

def install_packages():
    """
    Actualiza los paquetes instalados usando DNF
    
    Returns:
        str: Una cadena de texto indicando el nombre del/los paquete/s a instalar.
    """
    base = dnf.Base()
    base.read_all_repos()
    base.fill_sack()
    q = base.sack.query()
    i = q.upgrades()
    packages = list(i)
    print("packages to update: \n")
    print(packages)
    base.upgrade_all()
    base.resolve()
    print("Downloading packages...")
#    base.download_packages(base.transaction.install_set)
#    base.do_transaction()
    print("E")
    return True

if __name__ == "__main__":
    install_packages()