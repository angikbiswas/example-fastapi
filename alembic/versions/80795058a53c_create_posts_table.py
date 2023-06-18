"""create posts table

Revision ID: 80795058a53c
Revises: 
Create Date: 2023-06-16 20:31:23.338107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80795058a53c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,primary_key=True), sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
