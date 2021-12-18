"""create posts table

Revision ID: 17985b9b97cb
Revises: 
Create Date: 2021-12-17 21:25:40.721871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17985b9b97cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
