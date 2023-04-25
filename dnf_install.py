import dnf
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--package")
args = parser.parse_args()

def install_packages():
    print("PACKAGES: ", args.package)
    pkg = args.package.split()
    base = dnf.Base()
    base.read_all_repos()
    base.fill_sack()
    print("pkg_to_install", pkg)
    base.install_specs(pkg)
    base.resolve()
    base.download_packages(base.transaction.install_set)
    base.do_transaction()
    return pkg

if __name__ == "__main__":
    install_packages()