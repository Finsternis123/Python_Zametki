import csv
import time

# Файл, в который будут сохраняться заметки
file_name = "notes.csv"

# Словарь для хранения заметок
notes = {}

def load_notes_from_file():
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                notes[row['ID']] = {'text': row['Text'], 'date': row['Date']}
    except FileNotFoundError:
        # Если файл не найден, он будет создан при сохранении первой заметки
        pass

def save_notes_to_file():
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Text', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for note_id, note_data in notes.items():
            writer.writerow({'ID': note_id, 'Text': note_data['text'], 'Date': note_data['date']})

def create_note():
    note_id = input("Введите ID заметки: ")
    note_text = input("Введите текст заметки: ")
    note_date = time.strftime('%Y-%m-%d %H:%M:%S')  # Текущая дата и время
    notes[note_id] = {"text": note_text, "date": note_date}
    save_notes_to_file()
    print("Заметка успешно создана!")

def edit_note():
    note_id = input("Введите ID заметки для редактирования: ")
    if note_id in notes:
        new_note_text = input("Введите новый текст заметки: ")
        notes[note_id]["text"] = new_note_text
        save_notes_to_file()
        print("Заметка успешно отредактирована!")
    else:
        print("Заметка с таким ID не найдена.")

def delete_note():
    note_id = input("Введите ID заметки для удаления: ")
    if note_id in notes:
        del notes[note_id]
        save_notes_to_file()
        print("Заметка успешно удалена!")
    else:
        print("Заметка с таким ID не найдена.")

def show_all_notes():
    if not notes:
        print("Нет доступных заметок.")
        return

    for note_id, note_data in notes.items():
        print(f"ID: {note_id}, Текст: {note_data['text']}, Дата создания: {note_data['date']}")

def main():
    load_notes_from_file()

    while True:
        print("\n--- Меню приложения заметок ---")
        print("1. Создать заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Показать все заметки")
        print("5. Выйти из приложения")

        choice = input("Введите номер действия: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            show_all_notes()
        elif choice == "5":
            print("Выход из приложения...")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()