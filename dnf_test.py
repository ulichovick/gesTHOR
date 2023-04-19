import dnf




def test_dnf_query(filtr):
    base = dnf.Base()
    base.fill_sack()
    q = base.sack.query()
    i = q.installed()
    print(filtr)
    if filtr != "":
        i = i.filter(name=filtr)    
    packages = list(i)  # i only gets evaluated here
    paquetes = []
    print("Installed dnf package:")
    for pkg in packages:
        print(pkg, pkg.reponame)
    return packages

if __name__ == "__main__":
    test_dnf_query("neovim")