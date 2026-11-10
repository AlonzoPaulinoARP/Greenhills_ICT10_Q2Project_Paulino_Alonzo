# student club member checker
from pyscript import display, document


def check_name(e):
    document.getElementById('verify').innerHTML = ' '
    fname = document.getElementById('first_name').value
    lname = document.getElementById('last_name').value
    members_fname = ['Julianne', 'Dwayne', 'Pocholo', 'Rachmiel', 'Aisha', 'Alonzo', 'Jesse']
    members_lname = ['Canuday', 'Chua', 'Comanda', 'Lozada', 'Padua', 'Paulino', 'Villante']
    member_checker = fname in members_fname and lname in members_lname

    display_message = (f'Sorry {fname} {lname}, you are not part of this club. Try another one.', f'Welcome {fname} {lname}, you are part of the OBMC Math Guild led by Mr. Louise Robin Ferma.')
    
    display(display_message[member_checker], target='verify')