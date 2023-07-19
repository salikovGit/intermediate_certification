from uuid import uuid1
from datetime import datetime


def create_note(title, body):
    note = [str(uuid1())[0:3], title, body, datetime.now().strftime("%Y-%b-%d %H:%M:%S")]
    return note

