"""Initial migration.

Revision ID: 7c1333923649
Revises: 
Create Date: 2024-06-15 01:25:56.646709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c1333923649'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospitals', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reg_date', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospitals', schema=None) as batch_op:
        batch_op.drop_column('reg_date')

    # ### end Alembic commands ###
