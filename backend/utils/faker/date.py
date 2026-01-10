from datetime import datetime, timedelta
from random import randint

current_time = datetime.now()

def now() -> datetime:
    return current_time

def soon() -> datetime:
    return current_time + timedelta(days=randint(1,7), hours=randint(1,23))

def near_future() -> datetime:
    return current_time + timedelta(weeks=randint(1, 3), days=randint(1,7))

def future() -> datetime:
    return current_time + timedelta(weeks=randint(3,10), days=randint(1,7))

def recent() -> datetime:
    return current_time - timedelta(days=randint(1,7), hours=randint(1,23))

def past() -> datetime:
    return current_time - timedelta(days=randint(400, 800))

