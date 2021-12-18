"""add last few columns to posts table

Revision ID: f028f7797657
Revises: 5f9eb7497027
Create Date: 2021-12-18 00:09:33.489203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f028f7797657'
down_revision = '5f9eb7497027'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))

def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')