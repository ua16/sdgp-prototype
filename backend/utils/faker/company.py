from .names.last_names import last_names
from .names.locations import locations
from .names.roads import roads
from random import choice
from random import randint

com_ends = ["LLC", "Inc", "Corp", "Pvt Ltd"]
email_providers = ["supermail.com", "kmail.net", "mail.com", "letters.net"]

class Company:
    def __init__(self) -> None:
        self.uniq_name = choice(last_names)
        self.com_end = choice(com_ends)
        self.name = f"{self.uniq_name} {self.com_end}"
        self.email = f"{self.uniq_name}{self.com_end}@{choice(email_providers)}"
        self.city = choice(locations)
        self.road = choice(roads)
        self.address = f"{randint(1,500)}, {self.road} , {self.city}"
        self.phone = f"+{randint(1, 99)}-{''.join([str(randint(0,9)) for _ in range(9)])}"
