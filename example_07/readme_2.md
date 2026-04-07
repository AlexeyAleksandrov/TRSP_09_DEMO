# Быстрый старт example_07

## Подготовка (один раз)

1. **Создайте БД:**
```sql
CREATE DATABASE TRSP_09_DEMO_university;
```

2. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

## Демонстрация для студентов (пошагово)

### Шаг 1: Проверка начального состояния
```bash
alembic current
```
Результат: пусто (миграций нет)

---

### Шаг 2: Первая миграция
```bash
alembic upgrade 001
```
Создана таблица `students`

**Проверка в psql:**
```sql
\d students
```

---

### Шаг 3: Вторая миграция
```bash
alembic upgrade +1
```
Создана таблица `courses`

**История:**
```bash
alembic history
```

---

### Шаг 4: Применить все остальные
```bash
alembic upgrade head
```
Добавлены поля в `students`
Заполнены курсы
Заполнены студенты

**Проверка данных:**
```sql
SELECT * FROM students;
SELECT * FROM courses;
```

---

### Шаг 5: Откат на 1 версию назад
```bash
alembic downgrade -1
```
Студенты удалены

**Проверка:**
```sql
SELECT * FROM students;  -- Пустая
```

---

### Шаг 6: Откат на 2 версии
```bash
alembic downgrade -2
```
Курсы удалены
Поля group_number и enrollment_year удалены

**Проверка:**
```sql
\d students  -- Нет полей group_number, enrollment_year
```

---

### Шаг 7: Вернуть всё обратно
```bash
alembic upgrade head
```
Все миграции применены
Данные восстановлены

---

### Шаг 8: Полный откат
```bash
alembic downgrade base
```
Все таблицы удалены

**Восстановление:**
```bash
alembic upgrade head
```

---

## Команды-шпаргалка

```bash
# Просмотр
alembic current              # Текущая версия
alembic history              # История миграций
alembic history --verbose    # Подробная история

# Применение
alembic upgrade head         # Все миграции
alembic upgrade +N           # N миграций вперёд
alembic upgrade 003          # До версии 003

# Откат
alembic downgrade -N         # N миграций назад
alembic downgrade 003        # До версии 003
alembic downgrade base       # Все миграции
```

---

## SQL-запросы

```sql
-- Все студенты группы ЭФБО-01-25
SELECT first_name, last_name, group_number 
FROM students 
WHERE group_number = 'ЭФБО-01-25';

-- Студенты 2024 года поступления
SELECT first_name, last_name, enrollment_year 
FROM students 
WHERE enrollment_year = 2024;

-- Курсы по убыванию кредитов
SELECT name, credits 
FROM courses 
ORDER BY credits DESC;

-- Количество студентов по группам
SELECT group_number, COUNT(*) as count 
FROM students 
GROUP BY group_number;
```

---

## Различные сценарии

### Сценарий 1: Полный цикл (10 мин)
1. `alembic upgrade head` - применить всё
2. Показать данные в БД
3. `alembic downgrade -2` - откатить 2 версии
4. Показать, что изменилось
5. `alembic upgrade head` - восстановить

### Сценарий 2: Пошаговое применение (15 мин)
1. `alembic upgrade 001` - только студенты
2. `alembic upgrade 002` - добавить курсы
3. `alembic upgrade 003` - поля студента
4. `alembic upgrade 004` - данные курсов
5. `alembic upgrade 005` - данные студентов
6. После каждого шага показывать изменения в БД

### Сценарий 3: Откаты и восстановление (10 мин)
1. `alembic upgrade head` - применить всё
2. `alembic downgrade -1` - откатить студентов
3. Показать пустую таблицу students
4. `alembic upgrade +1` - восстановить
5. `alembic downgrade base` - полный откат
6. `alembic upgrade head` - полное восстановление


