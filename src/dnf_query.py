import apt
import sys
import queue

my_queue = queue.Queue()

def store_in_queue(f):
    def wrapper(*args):
        my_queue.put(f(*args))
    return wrapper

def query_local_packages(filtr):
    pkg_name = filtr
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    pkg = cache[pkg_name]
    if pkg.is_installed:
        print(type(pkg))
        return pkg
    else:
        return "paquete no instalado"

@store_in_queue
def query_available_packages(filtr):
    pkg_name = filtr

    cache = apt.cache.Cache()
    cache.update()
    cache.open()

    try:
        pkg = cache[pkg_name]
    except Exception as err:
        print(err)
        return "paquete no encontrado"
    return pkg

if __name__ == "__main__":
    pkg_to_install = query_available_packages("screenfetch")
