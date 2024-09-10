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

    # Обновляем оценку студента с id = 2
    update_query = '''
    UPDATE students
    SET grade = 3.7
    WHERE id = 2;
    '''

    # Выполнение запроса на обновление
    cursor.execute(update_query)
    connection.commit()

    # Сообщение об успешном обновлении
    print("\nОценка студента с id = 2 успешно обновлена на 3.7.")

    # SQL-запрос для выборки обновленной записи студента с id = 2
    select_updated_query = '''
    SELECT * FROM students WHERE id = 2;
    '''

    # Выполнение запроса
    cursor.execute(select_updated_query)

    # Получаем обновленную запись
    updated_record = cursor.fetchone()

    # Проверяем, существует ли запись
    if updated_record:
        # Выводим обновленную запись
        print("\nОбновлённая запись студента с id = 2:")
        print(f"ID: {updated_record[0]}, Имя: {updated_record[1]}, Возраст: {updated_record[2]}, Оценка: {updated_record[3]}")
    else:
        print("Запись с id = 2 не найдена.")

except sqlite3.Error as error:
    # Обработка ошибки
    print("Ошибка при работе с SQLite:", error)

finally:
    if connection:
        # Закрываем соединение
        connection.close()
        print("Соединение с SQLite закрыто.")
