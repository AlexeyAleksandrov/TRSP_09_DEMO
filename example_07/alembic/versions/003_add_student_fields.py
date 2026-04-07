"""add student fields

Revision ID: 003
Revises: 002
Create Date: 2026-04-07 10:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '003'
down_revision: Union[str, None] = '002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('students', sa.Column('group_number', sa.String(length=20), nullable=True))
    op.add_column('students', sa.Column('enrollment_year', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('students', 'enrollment_year')
    op.drop_column('students', 'group_number')
