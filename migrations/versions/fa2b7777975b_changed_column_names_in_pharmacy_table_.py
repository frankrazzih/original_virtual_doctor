"""changed column names in pharmacy table and added reg_date column

Revision ID: fa2b7777975b
Revises: 7c1333923649
Create Date: 2024-06-15 01:40:17.791166

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa2b7777975b'
down_revision = '7c1333923649'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pharmacy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pharm_name', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('pharm_location', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('reg_date', sa.Date(), nullable=True))
        batch_op.drop_column('name')
        batch_op.drop_column('location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pharmacy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', mysql.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('name', mysql.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('reg_date')
        batch_op.drop_column('pharm_location')
        batch_op.drop_column('pharm_name')

    # ### end Alembic commands ###
