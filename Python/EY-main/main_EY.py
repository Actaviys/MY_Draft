import Commands_Functions
allcommands = \
""" 
- help - Всі команди
- A - Підключитись до Arduino
- yt - Відкриваю ютуб 
- qq - Вихід з програми
- S - Скріпти (По назві)
- SC - Створюю скріпт (name, text_script)
- T - Перекладач

"""



def parse_input(user_input):
    """ 
    Функція для парсингу команд
    """
    cmd, *args = user_input.split()  # Розбиваю команду2
    cmd = cmd.strip()  # Записую команду в окрему змінну
    return cmd, *args  # Повертаю команду і аргументи


def main():  # Основна функція з циклом

    print("Welcome to the assistant bot!")
    while True:  # Основний цикл для постійного запиту команд
        user_input = input("Enter a command: ")  # Запитую команду

        try:  # Якщо є команда то виконую перевірки
            # Зберігаю результат парсингу в змінні
            command, *args = parse_input(user_input)

            match command:  # Команди

                case "help" | "допомога":  # Команда з списком команд
                    print(allcommands)

                case "A" | "Ф": Commands_Functions.connect_to_Arduino(args) # Підключитись до Ардуіно
                
                case "yt" | "не": Commands_Functions.youtube_open_func(args) # Відкриває ютуб 
                
                case "S" | "І": Commands_Functions.script_comand_read(args) # Запускає скріпти
                case "SC" |"ІС": Commands_Functions.create_and_save_as_bat(args) # Створюю скріпт
                
                case "T" | "Е" : Commands_Functions.wb.open("https://translate.google.com/?sl=uk&tl=en&op=translate") # Перекладач
                
                case "w" | "ц": Commands_Functions.basic_func_open_qt_window(args)
                
                
                
                
                case "qq" | "йй": print("Exit"); break # Виходжу з програми
                case _:  # Якщо команда не роспізнана
                    print("Invalid command!!!")
        except:
            # Якщо команда відсутня виводжу підказку
            print("Incorrect command... \nEnter 'help'")

if __name__ == "__main__": # Для циклу
    main()