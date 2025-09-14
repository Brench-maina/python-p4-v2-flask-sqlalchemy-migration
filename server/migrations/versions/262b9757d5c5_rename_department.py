"""rename department

Revision ID: 262b9757d5c5
Revises: e4ced078e72a
Create Date: 2025-09-14 13:45:33.124110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '262b9757d5c5'
down_revision = 'e4ced078e72a'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
