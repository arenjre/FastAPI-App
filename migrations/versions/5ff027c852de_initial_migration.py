"""Initial migration

Revision ID: 5ff027c852de
Revises: a2e9e7cf14c1
Create Date: 2025-03-29 23:35:24.754902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ff027c852de'
down_revision: Union[str, None] = 'a2e9e7cf14c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
