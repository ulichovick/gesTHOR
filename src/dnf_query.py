import dnf
import dnf.cli
import queue

my_queue = queue.Queue()

def store_in_queue(f):
    def wrapper(*args):
        my_queue.put(f(*args))
    return wrapper

def query_local_packages(filtr):
    """
    Consulta en el sistema el paquete indicado

    Args:
        filtr (str): Paquete a buscar en el sistema
    
    Returns:
        packages (list): Lista de paquetes que coinciden con la busqueda
    """
    base = dnf.Base()
    base.fill_sack()
    q = base.sack.query()
    i = q.installed()
    print(filtr)
    if filtr:
        i = i.filter(name=filtr)
    packages = list(i)
    print("Installed dnf package:")
    r = q.run()
    print(packages)
    return packages

@store_in_queue
def query_available_packages(filtr):
    """
    Consulta en los repositorios el paquete indicado

    Args:
        filtr (str): Paquete a buscar en el sistema
    
    Returns:
        packages (list): Lista de paquetes que coinciden con la busqueda
    """
    base = dnf.Base()
    base.read_all_repos()
    base.fill_sack()
    q = base.sack.query()
    i = q.available()
    if filtr:
        i = i.filter(name=filtr)
    else:
        i = i.filter(name="dnf")   
    packages = list(i)
    print("Available dnf package:")
    r = q.run()
    print(packages)
    return packages

if __name__ == "__main__":
    pkg_to_install = query_available_packages("screenfetch")
