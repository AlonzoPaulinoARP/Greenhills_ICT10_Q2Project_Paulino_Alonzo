from pyscript import display, document


grade7 = {'Josua Ortiz', 'Sean Smith', 'Nathan Pascua'}
grade8 = {'Robert Isais', 'Dan Perez', 'Mia Manalo'}
grade9 = {'Joaquin Villar', 'Connor Cheng', 'Xydris Cruz'}
grade10 = {'Alonzo Paulino', 'Rachmiel Lozada', 'Pocholo Comanda'}
master_set = grade7 | grade8 | grade9 | grade10

def add_member(e):
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    master_set.add(first + " " + last)
    display(f"{master_set} Total Members: {len(master_set)}", target='add')