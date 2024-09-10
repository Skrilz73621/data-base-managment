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

    # Сообщение о успешной вставке данных
    print("Таблица students успешно создана и записи добавлены.")

    # Удаление студента с id = 3
    delete_query = '''
    DELETE FROM students WHERE id = 3;
    '''
    cursor.execute(delete_query)
    connection.commit()
    print("\nСтудент с id = 3 удалён.")

    # Запрос всех студентов, чей возраст больше 20
    select_query = '''
    SELECT * FROM students WHERE age > 20;
    '''
    cursor.execute(select_query)
    records = cursor.fetchall()

    print("\nСтуденты старше 20 лет:")
    if records:
        for row in records:
            print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}, Оценка: {row[3]}")
    else:
        print("Студентов старше 20 лет не найдено.")

    # Добавление нового столбца email
    add_column_query = '''
    ALTER TABLE students
    ADD COLUMN email TEXT;
    '''
    cursor.execute(add_column_query)
    connection.commit()
    print("\nСтолбец email добавлен в таблицу students.")

    # Проверка схемы таблицы
    schema_query = '''
    PRAGMA table_info(students);
    '''
    cursor.execute(schema_query)
    schema = cursor.fetchall()

    print("\nСхема таблицы students:")
    for column in schema:
        print(f"Column ID: {column[0]}, Name: {column[1]}, Type: {column[2]}")

except sqlite3.Error as error:
    # Обработка ошибки
    print("Ошибка при работе с SQLite:", error)

finally:
    if connection:
        # Закрываем соединение
        connection.close()
        print("Соединение с SQLite закрыто.")
