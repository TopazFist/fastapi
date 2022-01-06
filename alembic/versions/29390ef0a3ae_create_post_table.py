"""create post table

Revision ID: 29390ef0a3ae
Revises: 
Create Date: 2022-01-05 17:43:32.880769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29390ef0a3ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
