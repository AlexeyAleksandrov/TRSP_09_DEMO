"""add is_active column

Revision ID: 005
Revises: 004
Create Date: 2026-04-07 02:40:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '005'
down_revision: Union[str, None] = '004'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('employees', sa.Column('is_active', sa.Boolean(), nullable=True, server_default='true'))


def downgrade() -> None:
    op.drop_column('employees', 'is_active')
