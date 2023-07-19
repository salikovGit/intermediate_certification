import csv
import datetime

import model


def init_db():
    with open('db.csv', mode="w", encoding='utf-8') as db:
        file_writer = csv.writer(db, delimiter=",", lineterminator="\r")
        file_writer.writerow(['ID', 'Title', 'Body', 'Time'])


def write_note(note):
    with open('db.csv', mode="a", encoding='utf-8') as db:
        file_writer = csv.writer(db, delimiter=",", lineterminator="\r")
        file_writer.writerow(note)


def read_note():
    with open('db.csv', mode="r", encoding='utf-8') as db:
        file_reader = csv.reader(db, delimiter=',')
        notes = []
        for row in file_reader:
            if len(row) == 4:
                notes.append(row)
        return notes


def check_id(uid):
    with open('db.csv', mode="r", encoding='utf-8') as db:
        file_writer = csv.reader(db, delimiter=',')
        notes = []
        for row in file_writer:
            notes.append(row)
        id_found = False
        for note in notes:
            if len(note) == 4:
                if note[0] == uid:
                    id_found = True
        return id_found


def delete_note(uid):
    notes = read_note()
    new_notes = []
    for row in notes:
        if row[0] != uid:
            new_notes.append(row)
    with open('db.csv', mode="w+", encoding='utf-8') as db:
        file_writer = csv.writer(db, delimiter=",", lineterminator="\r")
        for row in new_notes:
            file_writer.writerow(row)


def edit_note(uid):
    notes = read_note()
    new_notes = []
    for row in notes:
        if row[0] == uid:
            row[2] = model.body_input()
            row[3] = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")
        new_notes.append(row)
    with open('db.csv', mode="w+", encoding='utf-8') as db:
        file_writer = csv.writer(db, delimiter=",", lineterminator="\r")
        for row in new_notes:
            file_writer.writerow(row)
