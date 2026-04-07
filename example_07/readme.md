# Пример 7: Полный цикл работы с миграциями

## Структура проекта
```
example_07/
├── alembic/
│   ├── versions/
│   │   ├── 001_create_students_table.py       # Создание таблицы студентов
│   │   ├── 002_create_courses_table.py        # Создание таблицы курсов
│   │   ├── 003_add_student_fields.py          # Добавление полей студента
│   │   ├── 004_seed_courses.py                # Заполнение курсов
│   │   └── 005_seed_students.py               # Заполнение студентов
│   ├── env.py
│   ├── script.py.mako
│   └── README
├── database.py           # Модели SQLAlchemy (Student, Course)
├── alembic.ini           # Конфигурация Alembic
├── requirements.txt      # Зависимости
├── .env.example          # Пример переменных окружения
└── README.md             # Документация
```

## Модели базы данных

### Student (Студент)
- `id`: уникальный идентификатор
- `first_name`: имя студента
- `last_name`: фамилия студента
- `email`: электронная почта (уникальная)
- `group_number`: номер группы (добавляется в миграции 003)
- `enrollment_year`: год поступления (добавляется в миграции 003)

### Course (Курс)
- `id`: уникальный идентификатор
- `name`: название курса (уникальное)
- `code`: код курса (уникальный)
- `credits`: количество кредитов
- `description`: описание курса

## Предварительные требования

### 1. Установите PostgreSQL
Убедитесь, что PostgreSQL установлен и запущен на вашем компьютере.

### 2. Создайте базу данных

Подключитесь к PostgreSQL и создайте базу данных:

```sql
CREATE DATABASE TRSP_09_DEMO_university;
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

## Выполнение миграций

### Этап 1: Настройка Alembic

**Что уже сделано:** Alembic инициализирован командой `alembic init alembic`

**:**
- `alembic.ini` — конфигурационный файл с URL базы данных
- `alembic/env.py` — файл окружения, подключающий модели SQLAlchemy
- `alembic/versions/` — папка для миграций

**Команда для проверки:**
```bash
alembic current
```

Вывод должен быть пустым (миграции ещё не применены).

---

### Этап 2: Первая миграция - создание таблицы студентов

**Миграция 001** создаёт таблицу `students` с базовыми полями.

**Применить миграцию:**
```bash
alembic upgrade 001
```

**Проверить в PostgreSQL:**
```sql
\dt                          -- Показать все таблицы
\d students                  -- Описание таблицы students
SELECT * FROM students;      -- Таблица пустая
```

**Проверить версию:**
```bash
alembic current
```

Вывод: `001 (head)`

---

### Этап 3: Вторая миграция - создание таблицы курсов

**Миграция 002** создаёт таблицу `courses`.

**Применить миграцию:**
```bash
alembic upgrade +1
```

**Проверить:**
```sql
\d courses
```

**Просмотр истории:**
```bash
alembic history
```

Вы увидите:
```
001 -> 002 (head), create courses table
<base> -> 001, create students table
```

---

### Этап 4: Третья миграция - добавление полей студента

**Миграция 003** добавляет поля `group_number` и `enrollment_year` в таблицу `students`.

**Применить:**
```bash
alembic upgrade head
```

Эта команда применит все оставшиеся миграции до последней (003, 004, 005).

**Проверить структуру:**
```sql
\d students
```

Вы увидите новые поля: `group_number` и `enrollment_year`.

---

### Этап 5: Заполнение данными (Seeding)

**Миграции 004 и 005** заполняют таблицы начальными данными.

**Миграция 004:** Добавляет 8 курсов (ТРСП, ОАиП, БД и т.д.)
**Миграция 005:** Добавляет 10 студентов

**Проверить данные:**
```sql
-- Все курсы
SELECT * FROM courses;

-- Все студенты
SELECT * FROM students;

-- Студенты группы ЭФБО-01-25
SELECT first_name, last_name, group_number FROM students 
WHERE group_number = 'ЭФБО-01-25';

-- Курсы по количеству кредитов
SELECT name, credits FROM courses 
ORDER BY credits DESC;
```

---

### Этап 6: Управление версиями

**Посмотреть текущую версию:**
```bash
alembic current
```

**Посмотреть всю историю:**
```bash
alembic history --verbose
```

**Посмотреть детали конкретной миграции:**
```bash
alembic show 003
```

---

### Этап 7: Откаты миграций

#### 7.1 Откат на одну версию назад

Откатите последнюю миграцию (005 - seeding студентов):

```bash
alembic downgrade -1
```

**Проверьте:**
```sql
SELECT * FROM students;  -- Таблица должна быть пустой
SELECT * FROM courses;   -- Курсы остались
```

**Вернуть обратно:**
```bash
alembic upgrade +1
```

#### 7.2 Откат на несколько версий

Откатитесь на 2 версии назад (до миграции 003):

```bash
alembic downgrade -2
```

**Проверьте:**
```sql
\d students  -- Поля group_number и enrollment_year должны исчезнуть
SELECT * FROM courses;  -- Таблица пустая
```

#### 7.3 Откат к конкретной версии

Откатитесь к самой первой миграции:

```bash
alembic downgrade 001
```

**Проверьте:**
```sql
\dt  -- Останется только таблица students и alembic_version
```

#### 7.4 Полный откат

Откатите все миграции:

```bash
alembic downgrade base
```

**Проверьте:**
```sql
\dt  -- Только служебная таблица alembic_version
```

#### 7.5 Применение всех миграций снова

Восстановите все миграции:

```bash
alembic upgrade head
```

---

### Этап 8: Работа с зависимостями миграций

Откройте любой файл миграции в `alembic/versions/` и изучите параметры:

```python
revision: str = '003'
down_revision: Union[str, None] = '002'  # На какую миграцию опирается
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
```

**down_revision** указывает на предыдущую миграцию в цепочке.

---

## Полезные команды (шпаргалка)

### Основные команды

| Команда | Описание |
|---------|----------|
| `alembic current` | Показать текущую версию БД |
| `alembic history` | Показать историю миграций |
| `alembic history --verbose` | Подробная история |
| `alembic upgrade head` | Применить все миграции |
| `alembic upgrade +N` | Применить N миграций вперёд |
| `alembic upgrade <revision>` | Перейти на конкретную версию |
| `alembic downgrade -N` | Откатить N миграций назад |
| `alembic downgrade <revision>` | Откатиться к версии |
| `alembic downgrade base` | Откатить все миграции |
| `alembic show <revision>` | Показать детали миграции |

### Создание новых миграций

| Команда | Описание |
|---------|----------|
| `alembic revision --autogenerate -m "message"` | Автоматическое создание |
| `alembic revision -m "message"` | Ручное создание пустой миграции |
