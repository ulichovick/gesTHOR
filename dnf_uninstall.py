import dnf
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--package")
args = parser.parse_args()

def uninstall_packages():
    print("PACKAGES: ", args.package)
    pkgs = args.package.split()
    base = dnf.Base()
    base.read_all_repos()
    base.fill_sack()
    print("pkg_to_remove", pkgs)
    #base.install_specs(pkg)
    for pkg in pkgs:
        base.remove(pkg)
        base.resolve()
    base.do_transaction()
    return pkg

if __name__ == "__main__":
    uninstall_packages()