"""add salary and hire_date columns

Revision ID: 004
Revises: 003
Create Date: 2026-04-07 02:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '004'
down_revision: Union[str, None] = '003'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('employees', sa.Column('salary', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('employees', sa.Column('hire_date', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('employees', 'hire_date')
    op.drop_column('employees', 'salary')
