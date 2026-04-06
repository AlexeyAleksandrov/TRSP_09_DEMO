# Пример 3: Создание миграций

## Описание
Демонстрация создания миграций с помощью Alembic (автоматическая генерация и ручное создание).

## Структура проекта
```
example_03_migrations/
├── alembic/
│   ├── versions/         # Папка для миграций
│   ├── env.py            # Настройка окружения Alembic
│   ├── script.py.mako    # Шаблон для генерации миграций
│   └── README
├── database.py           # Модель SQLAlchemy (Article)
├── alembic.ini           # Конфигурация Alembic
├── requirements.txt      # Зависимости проекта
└── README.md             # Документация
```

## Установка

1. Создайте базу данных PostgreSQL:
```sql
CREATE DATABASE demo_migrations_db;
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Модель Article

Модель для демонстрации миграций:
- `id`: уникальный идентификатор (primary key)
- `title`: заголовок статьи
- `content`: содержание статьи (Text)
- `author`: автор статьи
- `created_at`: дата создания (автоматически)

## Пошаговая инструкция

### Шаг 1: Создание первой миграции (автоматически)

Создайте миграцию, которая создаст таблицу `articles`:

```bash
alembic revision --autogenerate -m "create articles table"
```

Alembic автоматически сгенерирует файл миграции в папке `alembic/versions/`.

**Что происходит:**
- Alembic сравнивает модели SQLAlchemy с текущим состоянием БД
- Генерирует код для функций `upgrade()` и `downgrade()`
- Создает уникальный идентификатор ревизии

### Шаг 2: Просмотр созданной миграции

Откройте файл миграции в `alembic/versions/` и изучите его структуру:

```python
def upgrade() -> None:
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('author', sa.String(length=100), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('articles')
```

### Шаг 3: Применение миграции

Примените миграцию к базе данных:

```bash
alembic upgrade head
```

**Результат:** Таблица `articles` будет создана в базе данных.

### Шаг 4: Проверка статуса

Проверьте текущую версию базы данных:

```bash
alembic current
```

Просмотрите историю всех миграций:

```bash
alembic history --verbose
```

### Шаг 5: Изменение модели и создание новой миграции

Теперь добавим новое поле в модель `Article`. Откройте `database.py` и добавьте поле:

```python
class Article(Base):
    __tablename__ = 'articles'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    # НОВОЕ ПОЛЕ:
    is_published: Mapped[bool] = mapped_column(default=False)
```

Создайте новую миграцию:

```bash
alembic revision --autogenerate -m "add is_published field"
```

Примените миграцию:

```bash
alembic upgrade head
```

## Ручное создание миграции

Иногда автогенерация не подходит. Создайте пустую миграцию:

```bash
alembic revision -m "custom migration"
```

Откройте созданный файл и вручную напишите код:

```python
def upgrade() -> None:
    op.add_column('articles', sa.Column('views_count', sa.Integer(), server_default='0'))

def downgrade() -> None:
    op.drop_column('articles', 'views_count')
```

## Полезные команды

| Команда | Описание |
|---------|----------|
| `alembic revision --autogenerate -m "message"` | Автоматическое создание миграции |
| `alembic revision -m "message"` | Ручное создание пустой миграции |
| `alembic upgrade head` | Применить все миграции |
| `alembic current` | Показать текущую версию БД |
| `alembic history` | Показать историю миграций |
| `alembic downgrade -1` | Откатить одну миграцию назад |

## Ограничения автогенерации

Alembic **НЕ** всегда обнаруживает:
- Изменение типа столбца
- Изменение имени таблицы/столбца
- Изменение ограничений (constraints)

В таких случаях нужно создавать миграции вручную или редактировать автогенерированные.

## Практическое задание

1. Создайте первую миграцию для таблицы `articles`
2. Примените её к БД
3. Добавьте поле `is_published` в модель
4. Создайте и примените вторую миграцию
5. Проверьте историю миграций командой `alembic history`
