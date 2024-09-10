import sqlite3

try:
    # Подключаемся к базе данных school.db
    connection = sqlite3.connect('school.db')

    # Создаем объект курсора
    cursor = connection.cursor()

    # Сообщение об успешном соединении
    print("Соединение с базой данных успешно установлено!")

except sqlite3.Error as error:
    # Обработка ошибки подключения
    print("Ошибка при подключении к SQLite:", error)

finally:
    if connection:
        # Закрываем соединение
        connection.close()
        print("Соединение с SQLite закрыто.")
