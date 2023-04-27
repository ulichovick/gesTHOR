import dnf


def uninstall_packages(pkgs):
    pkgs = pkgs
    base = dnf.Base()
    base.read_all_repos()
    base.fill_sack()
    print("pkg_to_remove", pkgs)
    for pkg in pkgs:
        base.remove(pkg)
        base.resolve()
    base.do_transaction()
    return pkgs

if __name__ == "__main__":
    uninstall_packages()