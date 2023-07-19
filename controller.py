import model
import view


def menu() -> None:
    while True:
        view.print_menu()
        user_input = input('\033[35mEnter one of possible commands:\033[0m ')

        if user_input.lower() == 'add':
            model.add_note()

        if user_input.lower() == 'show':
            model.show_notes()

        if user_input.lower() == 'edit':
            model.edit_note()

        if user_input.lower() == 'delete':
            model.delete_note()

        elif user_input.lower() == 'exit':
            break
