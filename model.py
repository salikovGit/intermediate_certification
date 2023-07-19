import notes
import db
import view


def title_input():
    title = input("\033[35mInput title:\033[0m\n")
    return title


def body_input():
    body = input("\033[35mInput body:\033[0m\n")
    return body


def uid_input():
    uid = input("\033[35mInput id:\033[0m\n")
    return uid


def add_note():
    title = title_input()
    body = body_input()
    note = notes.create_note(title, body)
    db.write_note(note)
    view.saved()


def show_notes():
    notes_list = db.read_note()
    for note in notes_list:
        view.print_color_note(note)
    print('\n')


def delete_note():
    notes_list = db.read_note()
    for note in notes_list:
        view.print_short_color_note(note)
    uid = uid_input()
    if db.check_id(uid):
        db.delete_note(uid)
        view.note_deleted(uid)
        notes_list = db.read_note()
        for note in notes_list:
            view.print_color_note(note)
    else:
        view.not_found(uid)
    print('\n')


def edit_note():
    notes_list = db.read_note()
    for note in notes_list:
        view.print_color_note(note)
    uid = uid_input()
    if db.check_id(uid):
        db.edit_note(uid)
        view.note_edited(uid)
        notes_list = db.read_note()
        for note in notes_list:
            view.print_color_note(note)
    else:
        view.not_found(uid)
    print('\n')
