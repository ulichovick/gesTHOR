import apt
import apt_pkg
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--package")
args = parser.parse_args()

def uninstall_packages():
    print("PACKAGES: ", args.package)
    pkgs = args.package.split()
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    for pk in pkgs:
        print("PACKAGE TO REMOVE: ", pk)
        pkg = cache[pk]
        pkg.mark_delete()
    cache.commit()
    return pkgs

if __name__ == "__main__":
    uninstall_packages()