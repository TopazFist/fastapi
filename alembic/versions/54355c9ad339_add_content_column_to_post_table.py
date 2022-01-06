"""add content column to post table

Revision ID: 54355c9ad339
Revises: 783496944ec7
Create Date: 2022-01-05 18:21:22.378664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54355c9ad339'
down_revision = '783496944ec7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
