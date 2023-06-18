"""add user table

Revision ID: 619a357506f3
Revises: 8a7e82af7bf6
Create Date: 2023-06-17 12:05:28.142885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '619a357506f3'
down_revision = '8a7e82af7bf6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
