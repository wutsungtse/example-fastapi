"""add foreign key to posts table

Revision ID: 5f9eb7497027
Revises: 6e1c4f0e1195
Create Date: 2021-12-18 00:02:28.872615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f9eb7497027'
down_revision = '6e1c4f0e1195'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fkey', source_table="posts", referent_table="users",
                        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraint('post_user_fkey', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
