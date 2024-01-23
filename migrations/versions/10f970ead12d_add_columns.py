"""Add columns

Revision ID: 10f970ead12d
Revises: 
Create Date: 2023-10-30 16:21:33.366653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10f970ead12d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('holidays', sa.Column('day', sa.String()))
    op.add_column('holidays', sa.Column('link', sa.String()))


def downgrade() -> None:
    pass
