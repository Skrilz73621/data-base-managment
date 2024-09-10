import sqlite3

try:
    # Подключаемся к базе данных school.db
    connection = sqlite3.connect('school.db')

    # Создаем объект курсора
    cursor = connection.cursor()

    # SQL-запрос для создания таблицы students
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL
    );
    '''

    # Выполнение запроса
    cursor.execute(create_table_query)
    connection.commit()  # Сохраняем изменения

    # Сообщение об успешном создании таблицы
    print("Таблица students успешно создана (если её не существовало).")

except sqlite3.Error as error:
    # Обработка ошибки
    print("Ошибка при работе с SQLite:", error)

finally:
    if connection:
        # Закрываем соединение
        connection.close()
        print("Соединение с SQLite закрыто.")
