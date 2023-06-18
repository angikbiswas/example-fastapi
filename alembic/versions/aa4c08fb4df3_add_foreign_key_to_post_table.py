"""add foreign key to post table

Revision ID: aa4c08fb4df3
Revises: 619a357506f3
Create Date: 2023-06-17 12:23:19.948113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa4c08fb4df3'
down_revision = '619a357506f3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name= "posts")
    op.drop_column('posts', 'owner_id')
    pass
