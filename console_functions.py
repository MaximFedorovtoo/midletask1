import datetime
from note_manager import NoteManager

manager = NoteManager()


def print_menu():
    print("\033[36mNote App")
    print("1. Create a note")
    print("2. Read notes")
    print("3. Find note by id")
    print("4. Edit a note")
    print("5. Delete a note")
    print("0. Exit\033[0m")


def color_green(text):
    color_text = f'\033[32m{text}\033[0m'
    return color_text


def color_red(text):
    color_text = f'\033[3;31m{text}\033[0m'
    return color_text


def crate():
    title = input(color_green("Enter note title: "))
    content = input(color_green("Enter note content: "))
    manager.create_note(title, content)


def read():
    try:
        filter_choice = input(color_green("Do you want to filter notes by date? (Y/N): "))
        if filter_choice.upper() == "Y":
            year = input(color_green("Enter year format YYYY : "))
            while not year.isdigit() or len(year) != 4:
                print(color_red('You enter wrong format data'))
                year = input(color_green("Enter year format YYYY : "))
            month = input(color_green("Enter month format MM: "))
            while not month.isdigit() or len(month) != 2:
                print(color_red('You enter wrong format data'))
                month = input(color_green("Enter month format MM: "))
            day = input(color_green("Enter day format DD: "))
            while not day.isdigit() or len(day) != 2:
                print(color_red('You enter wrong format data'))
                day = input(color_green("Enter day format DD: "))
            filter_date = f"{year}-{month}-{day}"
            filter_date = datetime.datetime.strptime(filter_date, "%Y-%m-%d").date()
            manager.read_notes(filter_date=filter_date)
        else:
            manager.read_notes()
    except ValueError:
        print(color_red("You have an error in the date"))


def find():
    try:
        note_id = int(input(color_green("Enter note ID: ")))
        note = manager.get_note_by_id(note_id)
        if note:
            print(color_green("Note details:"))
            print(color_green(note))
        else:
            print(color_red("Note not found."))
    except ValueError:
        print(color_red("The entered ID must be a number"))


def delete():
    try:
        note_id = int(input(color_green("Enter note ID: ")))
        manager.delete_note(note_id)
    except ValueError:
        print(color_red("The entered ID must be a number"))


def edit():
    try:
        note_id = int(input(color_green("Enter note ID: ")))
        new_title = input(color_green("Enter new note title: "))
        new_content = input(color_green("Enter new note content: "))
        manager.edit_note(note_id, new_title, new_content)
    except ValueError:
        print(color_red("The entered ID must be a number"))
