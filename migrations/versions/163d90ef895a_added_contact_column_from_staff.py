"""added contact column from staff

Revision ID: 163d90ef895a
Revises: 312876a26ae7
Create Date: 2024-06-24 12:21:10.601569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '163d90ef895a'
down_revision = '312876a26ae7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contact', sa.String(length=30), nullable=True))
        batch_op.create_unique_constraint(None, ['contact'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('contact')

    # ### end Alembic commands ###