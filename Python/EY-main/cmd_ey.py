import time
import Commands_Functions
allcommands = \
""" 
- help --> Всі команди
- yt --> Відкриваю ютуб 
- qq --> Вихід з програми
- T --> Перекладач
- w --> Відкриваю нове вікно QT

- f - Відкриваю різні файли
- A - Підключитись до Arduino
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

                case "h" | "р":  # Команда з списком команд #
                    print(allcommands)
                case "yt" | "не": Commands_Functions.youtube_open_func(args) # Відкриває ютуб #
                case "T" | "Е" : Commands_Functions.wb.open("https://translate.google.com/?sl=uk&tl=en&op=translate") # Перекладач #
                case "w" | "ц": Commands_Functions.basic_func_open_qt_window(args) # Відкриваю нове вікно QT #
                
                case "PC" | "ЗС": Commands_Functions.pc_read_information(args) # Виводжу інформацію про комп'ютер
                
                case "M" | "Ь": 
                    import main
                
                

                # case "f" | "а": Commands_Functions.open_other_files() # Відкриваю різні файли
                
                
                case "qq" | "йй": print("Пака :)"); time.sleep(0.5); break # Виходжу з програми #
                case _:  # Якщо команда не роспізнана #
                    print("Invalid command!!!")
        except:
            # Якщо команда відсутня виводжу підказку #
            print("Incorrect command... \nEnter 'help'")

if __name__ == "__main__": # Для циклу
    main()