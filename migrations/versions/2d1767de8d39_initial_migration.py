"""Initial migration

Revision ID: 2d1767de8d39
Revises: 96ffc642152c
Create Date: 2025-03-29 23:40:38.319586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d1767de8d39'
down_revision: Union[str, None] = '96ffc642152c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
