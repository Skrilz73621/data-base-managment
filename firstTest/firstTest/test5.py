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
        grade REAL,
        email TEXT
    );
    '''
    
    # Выполнение запроса на создание таблицы
    cursor.execute(create_table_query)

    # SQL-запрос для вставки данных
    insert_query = '''
    INSERT INTO students (id, name, age, grade) 
    VALUES (?, ?, ?, ?)
    ON CONFLICT(id) DO NOTHING;
    '''  # Используем ON CONFLICT, чтобы избежать повторной вставки данных, если они уже существуют.

    # Данные для вставки
    students_data = [
        (1, 'Alice', 20, 3.8),
        (2, 'Bob', 21, 3.5),
        (3, 'Charlie', 22, 3.9)
    ]

    # Вставляем данные в таблицу
    cursor.executemany(insert_query, students_data)
    connection.commit()  # Сохраняем изменения

    print("Таблица students успешно создана и записи добавлены.")

    # Попытка вставить дубликат записи с id = 1
    try:
        duplicate_insert_query = '''
        INSERT INTO students (id, name, age, grade) 
        VALUES (1, 'Duplicate Alice', 25, 4.0);
        '''
        cursor.execute(duplicate_insert_query)
        connection.commit()  # Сохраняем изменения
    except sqlite3.IntegrityError as error:
        print("\nОшибка при вставке дубликата записи с id = 1:", error)

    # Начало транзакции для обновления оценок студентов с age > 20
    try:
        connection.execute('BEGIN')  # Явно начинаем транзакцию

        update_query = '''
        UPDATE students
        SET grade = 4.0
        WHERE age > 20;
        '''
        cursor.execute(update_query)

        # Применяем изменения
        connection.commit()
        print("\nОценки студентов с возрастом > 20 успешно обновлены на 4.0.")

    except sqlite3.Error as error:
        # Откат транзакции в случае ошибки
        connection.rollback()
        print("\nОшибка при обновлении оценок студентов, транзакция отменена:", error)

except sqlite3.Error as error:
    # Общая обработка ошибок SQLite
    print("Ошибка при работе с SQLite:", error)

finally:
    if connection:
        # Закрываем соединение
        connection.close()
        print("Соединение с SQLite закрыто.")
