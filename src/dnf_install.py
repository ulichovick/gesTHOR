import apt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--package")
args = parser.parse_args()

def install_packages():
    print("PACKAGES: ", args.package)
    pkgs = args.package.split()
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    for pk in pkgs:
        print("PACKAGE TO INSTALL: ", pk)
        pkg = cache[pk]
        pkg.mark_install()
    cache.commit()
    return pk

if __name__ == "__main__":
    install_packages()