"""seed students

Revision ID: 005
Revises: 004
Create Date: 2026-04-07 10:40:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

revision: str = '005'
down_revision: Union[str, None] = '004'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

students_table = table(
    'students',
    column('id', Integer),
    column('first_name', String),
    column('last_name', String),
    column('email', String),
    column('group_number', String),
    column('enrollment_year', Integer)
)


def upgrade() -> None:
    initial_students = [
        {
            'id': 1,
            'first_name': 'Александр',
            'last_name': 'Иванов',
            'email': 'ivanov@example.com',
            'group_number': 'ЭФБО-01-25',
            'enrollment_year': 2023
        },
        {
            'id': 2,
            'first_name': 'Мария',
            'last_name': 'Петрова',
            'email': 'petrova@example.com',
            'group_number': 'ЭФБО-01-25',
            'enrollment_year': 2023
        },
        {
            'id': 3,
            'first_name': 'Дмитрий',
            'last_name': 'Сидоров',
            'email': 'sidorov@example.com',
            'group_number': 'ЭФБО-02-25',
            'enrollment_year': 2023
        },
        {
            'id': 4,
            'first_name': 'Елена',
            'last_name': 'Козлова',
            'email': 'kozlova@example.com',
            'group_number': 'ЭФБО-02-25',
            'enrollment_year': 2023
        },
        {
            'id': 5,
            'first_name': 'Сергей',
            'last_name': 'Новиков',
            'email': 'novikov@example.com',
            'group_number': 'ЭФБО-01-25',
            'enrollment_year': 2024
        },
        {
            'id': 6,
            'first_name': 'Анна',
            'last_name': 'Морозова',
            'email': 'morozova@example.com',
            'group_number': 'ЭФБО-01-25',
            'enrollment_year': 2024
        },
        {
            'id': 7,
            'first_name': 'Игорь',
            'last_name': 'Волков',
            'email': 'volkov@example.com',
            'group_number': 'ЭФБО-02-25',
            'enrollment_year': 2024
        },
        {
            'id': 8,
            'first_name': 'Ольга',
            'last_name': 'Соколова',
            'email': 'sokolova@example.com',
            'group_number': 'ЭФБО-02-25',
            'enrollment_year': 2024
        },
        {
            'id': 9,
            'first_name': 'Алексей',
            'last_name': 'Лебедев',
            'email': 'lebedev@example.com',
            'group_number': 'ЭФБО-01-25',
            'enrollment_year': 2025
        },
        {
            'id': 10,
            'first_name': 'Татьяна',
            'last_name': 'Семёнова',
            'email': 'semenova@example.com',
            'group_number': 'ЭФБО-02-25',
            'enrollment_year': 2025
        }
    ]
    
    op.bulk_insert(students_table, initial_students)


def downgrade() -> None:
    op.execute("DELETE FROM students WHERE id BETWEEN 1 AND 10")
