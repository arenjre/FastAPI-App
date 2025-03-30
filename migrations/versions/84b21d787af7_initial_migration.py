"""Initial migration

Revision ID: 84b21d787af7
Revises: 2d1767de8d39
Create Date: 2025-03-29 23:57:51.893186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84b21d787af7'
down_revision: Union[str, None] = '2d1767de8d39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
