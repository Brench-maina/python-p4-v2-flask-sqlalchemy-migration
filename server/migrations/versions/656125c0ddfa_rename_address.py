"""rename address

Revision ID: 656125c0ddfa
Revises: 262b9757d5c5
Create Date: 2025-09-14 13:50:04.964051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '656125c0ddfa'
down_revision = '262b9757d5c5'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('departments', 'address', new_column_name='location')
   
def downgrade():
   op.alter_column('departments', 'location', new_column_name='address')