"""Initial migration

Revision ID: a2e9e7cf14c1
Revises: ac55934cdac2
Create Date: 2025-03-29 23:34:16.583283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2e9e7cf14c1'
down_revision: Union[str, None] = 'ac55934cdac2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
