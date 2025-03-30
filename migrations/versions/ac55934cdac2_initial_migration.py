"""Initial migration

Revision ID: ac55934cdac2
Revises: d32aec583769
Create Date: 2025-03-29 23:31:44.944100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac55934cdac2'
down_revision: Union[str, None] = 'd32aec583769'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
