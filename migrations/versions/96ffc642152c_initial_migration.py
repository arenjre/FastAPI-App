"""Initial migration

Revision ID: 96ffc642152c
Revises: 5ff027c852de
Create Date: 2025-03-29 23:38:53.679218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96ffc642152c'
down_revision: Union[str, None] = '5ff027c852de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
