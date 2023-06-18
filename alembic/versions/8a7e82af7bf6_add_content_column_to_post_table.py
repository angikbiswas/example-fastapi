"""add content column to post table

Revision ID: 8a7e82af7bf6
Revises: 80795058a53c
Create Date: 2023-06-17 11:53:49.631563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a7e82af7bf6'
down_revision = '80795058a53c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
