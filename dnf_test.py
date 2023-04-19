import dnf

def query_local_packages(filtr):
    base = dnf.Base()
    base.fill_sack()
    q = base.sack.query()
    i = q.installed()
    print(filtr)
    if filtr:
        i = i.filter(name=filtr)    
    packages = list(i)  # i only gets evaluated here
    print("Installed dnf package:")
    r = q.run()
    print(packages)
    return packages

def query_available_packages(filtr):
    base = dnf.Base()
    base.read_all_repos()
    base.fill_sack()
    q = base.sack.query()
    i = q.available()
    print(filtr)
    if filtr:
        i = i.filter(name=filtr)    
    packages = list(i)  # i only gets evaluated here
    print("Available dnf package:")
    r = q.run()
    return packages

if __name__ == "__main__":
    query_local_packages("neovim")