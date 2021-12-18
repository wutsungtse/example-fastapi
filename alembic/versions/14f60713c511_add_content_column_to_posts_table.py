"""add content column to posts table

Revision ID: 14f60713c511
Revises: 17985b9b97cb
Create Date: 2021-12-17 23:36:34.489617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14f60713c511'
down_revision = '17985b9b97cb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
