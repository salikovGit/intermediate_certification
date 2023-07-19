def print_menu():
    print("\033[34mPossible commands:")
    print("ADD, SHOW, EDIT, DELETE, EXIT\033[0m\n")


def print_note(note):
    print(f"UID: {note[0]}, Title: {note[1]}, Body: {note[2]}, Last change time: {note[3]}")


def print_color_note(note):
    print("\033[34mUID: \033[0m{}, \033[34mTitle: \033[0m{}, \033[34mBody: \033[0m{}, \033[34mLast change time: "
          "\033[0m".format(note[0], note[1], note[2], note[3]))


def print_short_color_note(note):
    print("\033[34mUID: \033[0m{}, \033[34mTitle: \033[0m{}, \033[34mLast change time: "
          "\033[0m{}'n".format(note[0], note[1], note[3]))


def not_found(uid):
    print("\033[31mNote with ID {} not found!\033[0m\n".format(uid))


def note_deleted(uid):
    print("\n\033[32mNote with ID \033[34m{}\033[32m has been deleted\nActual notes list:\033[0m".format(uid))


def note_edited(uid):
    print("\n\033[32mNote with ID \033[34m{}\033[32m has been edited\nActual notes list:\033[0m".format(uid))


def saved():
    print("\033[32mYour note has been successfully saved\033[0m\n".format())
