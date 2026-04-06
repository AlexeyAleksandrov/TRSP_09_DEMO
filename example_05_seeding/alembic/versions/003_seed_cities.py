"""seed cities

Revision ID: 003
Revises: 002
Create Date: 2026-04-07 01:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Text

revision: str = '003'
down_revision: Union[str, None] = '002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

cities_table = table(
    'cities',
    column('id', Integer),
    column('name', String),
    column('country_code', String),
    column('population', Integer),
    column('description', Text)
)


def upgrade() -> None:
    initial_cities = [
        {'id': 1, 'name': 'Москва', 'country_code': 'RUS', 'population': 12500000, 
         'description': 'Столица России, крупнейший город страны'},
        {'id': 2, 'name': 'Санкт-Петербург', 'country_code': 'RUS', 'population': 5400000,
         'description': 'Культурная столица России'},
        {'id': 3, 'name': 'Нью-Йорк', 'country_code': 'USA', 'population': 8400000,
         'description': 'Крупнейший город США'},
        {'id': 4, 'name': 'Лос-Анджелес', 'country_code': 'USA', 'population': 4000000,
         'description': 'Город ангелов, центр киноиндустрии'},
        {'id': 5, 'name': 'Пекин', 'country_code': 'CHN', 'population': 21500000,
         'description': 'Столица Китая'},
        {'id': 6, 'name': 'Шанхай', 'country_code': 'CHN', 'population': 27000000,
         'description': 'Крупнейший город Китая'},
        {'id': 7, 'name': 'Берлин', 'country_code': 'DEU', 'population': 3600000,
         'description': 'Столица Германии'},
        {'id': 8, 'name': 'Париж', 'country_code': 'FRA', 'population': 2200000,
         'description': 'Столица Франции, город любви'},
        {'id': 9, 'name': 'Токио', 'country_code': 'JPN', 'population': 14000000,
         'description': 'Столица Японии, современный мегаполис'},
        {'id': 10, 'name': 'Лондон', 'country_code': 'GBR', 'population': 9000000,
         'description': 'Столица Великобритании'},
    ]
    
    op.bulk_insert(cities_table, initial_cities)


def downgrade() -> None:
    op.execute("DELETE FROM cities WHERE id BETWEEN 1 AND 10")
