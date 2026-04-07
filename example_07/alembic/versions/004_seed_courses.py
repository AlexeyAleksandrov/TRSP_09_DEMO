"""seed courses

Revision ID: 004
Revises: 003
Create Date: 2026-04-07 10:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

revision: str = '004'
down_revision: Union[str, None] = '003'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

courses_table = table(
    'courses',
    column('id', Integer),
    column('name', String),
    column('code', String),
    column('credits', Integer),
    column('description', String)
)


def upgrade() -> None:
    initial_courses = [
        {
            'id': 1,
            'name': 'Технологии разработки серверных приложений',
            'code': 'TRSP',
            'credits': 4,
            'description': 'Изучение современных технологий разработки серверных приложений с использованием Python и FastAPI'
        },
        {
            'id': 2,
            'name': 'Основы алгоритмизации и программирования',
            'code': 'OAIP',
            'credits': 5,
            'description': 'Основы программирования на языке C/C++'
        },
        {
            'id': 3,
            'name': 'Базы данных',
            'code': 'DB',
            'credits': 4,
            'description': 'Проектирование и работа с реляционными базами данных'
        },
        {
            'id': 4,
            'name': 'Объектно-ориентированное программирование',
            'code': 'OOP',
            'credits': 4,
            'description': 'Принципы ООП и их применение на практике'
        },
        {
            'id': 5,
            'name': 'Веб-программирование',
            'code': 'WEB',
            'credits': 3,
            'description': 'Разработка веб-приложений с использованием HTML, CSS, JavaScript'
        },
        {
            'id': 6,
            'name': 'Компьютерные сети',
            'code': 'NET',
            'credits': 3,
            'description': 'Принципы работы компьютерных сетей и сетевых протоколов'
        },
        {
            'id': 7,
            'name': 'Операционные системы',
            'code': 'OS',
            'credits': 4,
            'description': 'Архитектура и принципы работы операционных систем'
        },
        {
            'id': 8,
            'name': 'Математический анализ',
            'code': 'MATH',
            'credits': 5,
            'description': 'Высшая математика для программистов'
        }
    ]
    
    op.bulk_insert(courses_table, initial_courses)


def downgrade() -> None:
    op.execute("DELETE FROM courses WHERE code IN ('TRSP', 'OAIP', 'DB', 'OOP', 'WEB', 'NET', 'OS', 'MATH')")
