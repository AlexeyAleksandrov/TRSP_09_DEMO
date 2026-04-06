"""add department and position columns

Revision ID: 003
Revises: 002
Create Date: 2026-04-07 02:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '003'
down_revision: Union[str, None] = '002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('employees', sa.Column('department', sa.String(length=100), nullable=True))
    op.add_column('employees', sa.Column('position', sa.String(length=100), nullable=True))


def downgrade() -> None:
    op.drop_column('employees', 'position')
    op.drop_column('employees', 'department')
