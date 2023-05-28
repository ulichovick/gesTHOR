#!/usr/bin/python3
import dnf

base = dnf.Base()
base.read_all_repos()
base.fill_sack()

q = base.sack.query()
a = q.available()
a = a.filter(name='bleachbit', latest = 1)

print("Available dnf packages:")
for pkg in a:  # a only gets evaluated here
    print('Package {}'.format(pkg))
    print('Package name {}'.format(pkg.name))
    print('Repo name {}'.format(pkg.reponame))
    print('Arch {}'.format(pkg.arch))
    print('Version {}'.format(pkg.version))
    print('Description {}'.format(pkg.description))
