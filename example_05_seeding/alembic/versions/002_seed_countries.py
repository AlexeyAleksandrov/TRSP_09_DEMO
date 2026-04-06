"""seed countries

Revision ID: 002
Revises: 001
Create Date: 2026-04-07 01:10:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

revision: str = '002'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

countries_table = table(
    'countries',
    column('id', Integer),
    column('name', String),
    column('code', String),
    column('capital', String),
    column('population', Integer)
)


def upgrade() -> None:
    initial_countries = [
        {'id': 1, 'name': 'Россия', 'code': 'RUS', 'capital': 'Москва', 'population': 146000000},
        {'id': 2, 'name': 'США', 'code': 'USA', 'capital': 'Вашингтон', 'population': 331000000},
        {'id': 3, 'name': 'Китай', 'code': 'CHN', 'capital': 'Пекин', 'population': 1400000000},
        {'id': 4, 'name': 'Германия', 'code': 'DEU', 'capital': 'Берлин', 'population': 83000000},
        {'id': 5, 'name': 'Франция', 'code': 'FRA', 'capital': 'Париж', 'population': 67000000},
        {'id': 6, 'name': 'Япония', 'code': 'JPN', 'capital': 'Токио', 'population': 126000000},
        {'id': 7, 'name': 'Великобритания', 'code': 'GBR', 'capital': 'Лондон', 'population': 67000000},
        {'id': 8, 'name': 'Италия', 'code': 'ITA', 'capital': 'Рим', 'population': 60000000},
    ]
    
    op.bulk_insert(countries_table, initial_countries)


def downgrade() -> None:
    op.execute("DELETE FROM countries WHERE code IN ('RUS', 'USA', 'CHN', 'DEU', 'FRA', 'JPN', 'GBR', 'ITA')")
