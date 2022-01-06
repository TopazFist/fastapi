"""add last few columns

Revision ID: 6550dde12592
Revises: a471db2fed49
Create Date: 2022-01-05 18:59:52.517316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6550dde12592'
down_revision = 'a471db2fed49'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')    
    pass
