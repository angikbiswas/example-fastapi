"""add last few column to post table

Revision ID: bebac2865bb4
Revises: aa4c08fb4df3
Create Date: 2023-06-17 12:51:22.190426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bebac2865bb4'
down_revision = 'aa4c08fb4df3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published', sa.Boolean(), nullable= False, server_default= 'TRUE'),)
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable= False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
