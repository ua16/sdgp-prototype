from .names.last_names import last_names
from random import choice

com_ends = ["LLC", "Inc", "Corp", "Pvt Ltd"]

def name():
    return f"{choice(last_names)} {choice(com_ends)}"
