"""Initial migration

Revision ID: d32aec583769
Revises: 83b6a2bfca92
Create Date: 2025-03-29 23:28:07.747024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd32aec583769'
down_revision: Union[str, None] = '83b6a2bfca92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
